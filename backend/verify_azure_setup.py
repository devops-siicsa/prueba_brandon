"""
Verify Azure Container and Test Upload
"""
import os
from dotenv import load_dotenv
from io import BytesIO

load_dotenv()

from azure.storage.blob import BlobServiceClient, PublicAccess

connection_string = os.getenv('AZURE_STORAGE_CONNECTION_STRING')
container_name = os.getenv('AZURE_CONTAINER_NAME', 'siicsa-invetarioti')

print("=" * 60)
print("AZURE BLOB STORAGE - CONTAINER SETUP & TEST")
print("=" * 60)

try:
    # Step 1: Connect
    print(f"\n1. Connecting to Azure Storage...")
    blob_service_client = BlobServiceClient.from_connection_string(connection_string)
    print("   ✓ Connected successfully")
    
    # Step 2: Get/Create container
    print(f"\n2. Checking container: {container_name}")
    container_client = blob_service_client.get_container_client(container_name)
    
    try:
        # Try to create
        container_client.create_container(public_access=PublicAccess.Blob)
        print(f"   ✓ Container created with public blob access")
    except Exception as e:
        if "ContainerAlreadyExists" in str(e) or "already exists" in str(e).lower():
            print(f"   ✓ Container already exists (OK)")
        else:
            print(f"   ✗ Error: {e}")
            raise
    
    # Step 3: Test upload
    print(f"\n3. Testing file upload...")
    test_blob_name = "test/hello.txt"
    test_content = b"Hello from Python! This is a test file."
    
    blob_client = container_client.get_blob_client(test_blob_name)
    blob_client.upload_blob(test_content, overwrite=True)
    
    test_url = blob_client.url
    print(f"   ✓ Test file uploaded successfully")
    print(f"   URL: {test_url}")
    
    # Step 4: Verify
    print(f"\n4. Verifying upload...")
    blob_properties = blob_client.get_blob_properties()
    print(f"   ✓ File size: {blob_properties.size} bytes")
    print(f"   ✓ Content type: {blob_properties.content_settings.content_type}")
    
    # Step 5: Cleanup test file
    print(f"\n5. Cleaning up test file...")
    blob_client.delete_blob()
    print(f"   ✓ Test file deleted")
    
    print("\n" + "=" * 60)
    print("✓ ALL TESTS PASSED - Azure Blob Storage is ready!")
    print("=" * 60)
    
except Exception as e:
    print(f"\n✗ ERROR: {type(e).__name__}")
    print(f"   {str(e)}")
    import traceback
    traceback.print_exc()
    print("\n" + "=" * 60)
