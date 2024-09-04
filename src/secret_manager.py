from google.cloud import secretmanager

def get_secret(version_id="latest"):
    client = secretmanager.SecretManagerServiceClient()
    name = f"projects/74699748159/secrets/gmail_app_password/versions/{version_id}"
    response = client.access_secret_version(name=name)
    return response.payload.data.decode("UTF-8")