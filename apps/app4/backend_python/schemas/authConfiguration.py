from pydantic import BaseModel


class authConfiguration(BaseModel):
    server_url: str
    realm: str
    client_id: str
    authorization_url: str
    token_url: str
