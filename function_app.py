from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
import azure.functions as func
import logging

app = func.FunctionApp()
default_credential = DefaultAzureCredential()

@app.function_name(name="TestTrigger")
@app.route(route="test")
def my_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    # Test
    client = BlobServiceClient(https://teststoragemid.blob.core.windows.net, credential=default_credential)
    container_name = str(uuid.uuid4())
    container_client = client.create_container(container_name)
    return func.HttpResponse(
        "Our work here is done!",
        status_code=200
    )