"""
Test Azure Blob Storage Connection
"""
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

try:
    from azure.storage.blob import BlobServiceClient
    
    connection_string = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
    container_name = os.getenv('AZURE_CONTAINER_NAME', 'siicsa-invetarioti')
    
    print(f"Testing Azure Blob Storage connection...")
    print(f"Container name: {container_name}")
    
    # Create client
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    print("✓ BlobServiceClient created successfully")
    
    # Try to get container
    container_client = blob_service_client.get_container_client(container_name)
    
    # Try to create container if it doesn't exist
    try:
        container_client.create_container(public_access='blob')
        print(f"✓ Container '{container_name}' created successfully")
    except Exception as e:
        if "ContainerAlreadyExists" in str(e) or "already exists" in str(e).lower():
            print(f"✓ Container '{container_name}' already exists")
        else:
            print(f"✗ Error creating/accessing container: {type(e).__name__}: {str(e)}")
            raise
    
    # List containers to verify
    print("\nAvailable containers:")
    containers = blob_service_client.list_containers()
    for container in containers:
        print(f"  - {container.name}")
    
    print("\n✓ Azure Blob Storage connection test successful!")
    
except Exception as e:
    print(f"\n✗ Error testing Azure connection:")
    print(f"  Type: {type(e).__name__}")
    print(f"  Message: {str(e)}")
    import traceback
    traceback.print_exc()
