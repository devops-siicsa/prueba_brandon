"""
Azure Blob Storage Service
Manages file uploads and downloads to/from Azure Blob Storage
"""
import os
import uuid
import traceback
from pathlib import Path
from azure.storage.blob import BlobServiceClient, ContentSettings
from werkzeug.utils import secure_filename

class AzureStorageService:
    def __init__(self):
        """Initialize Azure Blob Storage client (lazy initialization)"""
        self._blob_service_client = None
        self._container_name = None
    
    def _get_client(self):
        """Lazy initialization of Azure client"""
        if self._blob_service_client is None:
            connection_string = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
            if not connection_string:
                raise ValueError("AZURE_STORAGE_CONNECTION_STRING not found in environment variables")
            
            self._blob_service_client = BlobServiceClient.from_connection_string(connection_string)
            self._container_name = os.getenv('AZURE_CONTAINER_NAME', 'siicsa-invetarioti')
            print(f"✓ Azure Blob Storage initialized. Container: {self._container_name}")
        
        return self._blob_service_client
    
    @property
    def blob_service_client(self):
        return self._get_client()
    
    @property
    def container_name(self):
        if self._container_name is None:
            self._get_client()
        return self._container_name
    
    def upload_file(self, file, equipo_id):
        """
        Upload a file to Azure Blob Storage (private container with SAS token)
        
        Args:
            file: FileStorage object from Flask request
            equipo_id: ID of the equipment for organizing files
            
        Returns:
            dict: {
                'url': str,  # URL with SAS token
                'blob_name': str,  # Name of the blob in Azure
                'original_name': str,  # Original filename
                'size': int,  # File size in bytes
                'content_type': str  # MIME type
            }
        """
        try:
            print(f"[Azure Upload] Starting upload for equipo {equipo_id}, file: {file.filename}")
            
            # Get container client
            container_client = self.blob_service_client.get_container_client(self.container_name)
            print(f"[Azure Upload] Got container client for: {self.container_name}")
            
            # Create container if it doesn't exist (PRIVATE - no public access)
            try:
                container_client.create_container()  # No public_access parameter = private
                print(f"[Azure Upload] Container created (private)")
            except Exception as create_error:
                if "ContainerAlreadyExists" in str(create_error) or "already exists" in str(create_error).lower():
                    print(f"[Azure Upload] Container already exists (OK)")
                else:
                    print(f"[Azure Upload] Container creation error (may already exist): {str(create_error)}")
            
            # Generate unique filename preserving original name
            original_filename = secure_filename(file.filename)
            # Use UUID prefix + original name to avoid collisions but keep readable name
            unique_filename = f"equipos/{equipo_id}/{uuid.uuid4()}_{original_filename}"
            print(f"[Azure Upload] Generated blob name: {unique_filename}")
            
            # Get blob client
            blob_client = container_client.get_blob_client(unique_filename)
            
            # Upload file with content type using stream (more memory efficient)
            content_type = file.content_type or 'application/octet-stream'
            content_settings = ContentSettings(content_type=content_type)
            
            # Get file size before uploading
            file.seek(0, 2)  # Seek to end
            file_size = file.tell()
            file.seek(0)  # Reset to beginning
            print(f"[Azure Upload] File size: {file_size} bytes")
            
            blob_client.upload_blob(
                file.stream,  # Use stream instead of reading into memory
                overwrite=True,
                content_settings=content_settings
            )
            print(f"[Azure Upload] ✓ File uploaded to blob storage")
            
            # Generate SAS token (10 years validity) with content disposition for correct filename
            from azure.storage.blob import generate_blob_sas, BlobSasPermissions
            from datetime import datetime, timedelta
            
            sas_token = generate_blob_sas(
                account_name=self.blob_service_client.account_name,
                container_name=self.container_name,
                blob_name=unique_filename,
                account_key=self.blob_service_client.credential.account_key,
                permission=BlobSasPermissions(read=True),
                expiry=datetime.utcnow() + timedelta(days=3650),  # 10 years
                content_disposition=f'inline; filename="{original_filename}"'  # Use inline instead of attachment
            )
            
            # Construct URL with SAS token
            url_with_sas = f"https://{self.blob_service_client.account_name}.blob.core.windows.net/{self.container_name}/{unique_filename}?{sas_token}"
            print(f"[Azure Upload] ✓ Upload successful with SAS token")
            
            # Return file info
            return {
                'url': url_with_sas,
                'blob_name': unique_filename,
                'original_name': original_filename,
                'size': file_size,
                'content_type': content_type
            }
            
        except Exception as e:
            error_msg = f"Error uploading file to Azure Blob Storage: {str(e)}"
            print(f"[Azure Upload] ✗ {error_msg}")
            import traceback
            traceback.print_exc()
            raise Exception(error_msg)
    
    def delete_file(self, blob_name):
        """
        Delete a file from Azure Blob Storage
        
        Args:
            blob_name: Name of the blob to delete
            
        Returns:
            bool: True if deleted successfully
        """
        try:
            container_client = self.blob_service_client.get_container_client(self.container_name)
            blob_client = container_client.get_blob_client(blob_name)
            blob_client.delete_blob()
            return True
        except Exception as e:
            print(f"Error deleting blob {blob_name}: {str(e)}")
            return False
    
    def get_file_url(self, blob_name):
        """
        Get public URL for a blob
        
        Args:
            blob_name: Name of the blob
            
        Returns:
            str: Public URL
        """
        container_client = self.blob_service_client.get_container_client(self.container_name)
        blob_client = container_client.get_blob_client(blob_name)
        return blob_client.url
    
    def download_file(self, blob_name):
        """
        Download a file from Azure Blob Storage
        
        Args:
            blob_name: Name of the blob to download
            
        Returns:
            bytes: File content
        """
        try:
            container_client = self.blob_service_client.get_container_client(self.container_name)
            blob_client = container_client.get_blob_client(blob_name)
            
            download_stream = blob_client.download_blob()
            return download_stream.readall()
        except Exception as e:
            raise Exception(f"Error downloading file from Azure Blob Storage: {str(e)}")

# Singleton instance
azure_storage = AzureStorageService()
