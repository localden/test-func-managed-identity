from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient

default_credential = DefaultAzureCredential()

client = BlobServiceClient(https://teststoragemid.blob.core.windows.net, credential=default_credential)
container_name = str(uuid.uuid4())
container_client = client.create_container(container_name)