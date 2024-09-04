from google.cloud import secretmanager
from config import SECRET_PASSWORD

def get_secret():
    client = secretmanager.SecretManagerServiceClient()
    response = client.access_secret_version(name=SECRET_PASSWORD)
    return response.payload.data.decode("UTF-8")