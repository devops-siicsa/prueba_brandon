"""
Create Azure Blob Storage Container
"""
import os
from dotenv import load_dotenv

load_dotenv()

from azure.storage.blob import BlobServiceClient, PublicAccess

connection_string = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
container_name = os.getenv('AZURE_CONTAINER_NAME', 'siicsa-invetarioti')

print(f"Creating container: {container_name}")
print(f"Connection string starts with: {connection_string[:50]}...")

try:
    # Create client
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    
    # Get container client
    container_client = blob_service_client.get_container_client(container_name)
    
    # Create with public blob access
    container_client.create_container(public_access=PublicAccess.Blob)
    
    print(f"✓ Container '{container_name}' created successfully with public blob access!")
    
except Exception as e:
    if "ContainerAlreadyExists" in str(e):
        print(f"✓ Container '{container_name}' already exists!")
    else:
        print(f"✗ Error: {e}")
        import traceback
        traceback.print_exc()
