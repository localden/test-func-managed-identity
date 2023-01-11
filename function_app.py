from azure.identity import DefaultAzureCredential
from azure.storage.blob import BlobServiceClient
import azure.functions as func
import logging
import uuid

app = func.FunctionApp()
default_credential = DefaultAzureCredential()

@app.function_name(name="TestTrigger")
@app.route(route="test")
def my_function(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')
    # Test2Redeploy-Test
    client = BlobServiceClient("https://teststoragemid.blob.core.windows.net", credential=default_credential)
    container_name = str(uuid.uuid4())
    container_client = client.create_container(container_name)
    return func.HttpResponse(
        "Our work here is done!",
        status_code=200
    )

@app.function_name(name="HttpTrigger1")
@app.route(route="hello")
def test_function(req: func.HttpRequest) -> func.HttpResponse:
     logging.info('Python HTTP trigger function processed a request.')

     name = req.params.get('name')
     if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

     if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
     else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
