import toml
from google.cloud import secretmanager

client = secretmanager.SecretManagerServiceClient()

def fetch_secret(secret_id):
    """Fetch latest version of a secret"""
    name = f"projects/musafir/secrets/{secret_id}/versions/latest"
    response = client.access_secret_version(request={"name": name})
    return response.payload.data.decode("utf-8")

def create_toml_file():
    """Fetch secrets and create secrets.toml"""
    
    toml_config = {
            "auth": {
                "redirect_uri": "http://localhost:8501/oauth2callback",  # static
                "cookie_secret": fetch_secret("COOKIE_SECRET"),
                "client_id": fetch_secret("CLIENT_ID"),
                "client_secret": fetch_secret("CLIENT_SECRET"),
                "server_metadata_url": "https://accounts.google.com/.well-known/openid-configuration",  # static
            },
            "google": {
                "GOOGLE_API_KEY": fetch_secret("GOOGLE_API_KEY"),
            },
        }   

    with open("./streamlit/secrets.toml", "w") as f:
        toml.dump(toml_config, f)