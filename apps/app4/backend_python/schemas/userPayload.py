from pydantic import BaseModel


class userPayload(BaseModel):
    sub: str
    realm_roles: list
