import os
from dotenv import load_dotenv
from schemas import authConfiguration

load_dotenv()

SERVER_URL = os.getenv("SERVER_URL")
REALM = os.getenv("REALM")
CLIENT_ID = os.getenv("CLIENT_ID")
AUTHORIZATION_URL = os.getenv("AUTHORIZATION_URL")
TOKEN_URL = os.getenv("TOKEN_URL")

settings = authConfiguration(
    server_url=SERVER_URL, 
    realm= REALM,
    client_id=CLIENT_ID,
    authorization_url= AUTHORIZATION_URL,
    token_url= TOKEN_URL
)