from fastapi.security import OAuth2PasswordBearer
from keycloak import KeycloakOpenID
from config.keycloakConfig import settings
from fastapi import Security, HTTPException, status, Depends
from schemas import userPayload

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl=settings.token_url
)

keycloak_openid = KeycloakOpenID(
    server_url=settings.server_url,
    client_id=settings.client_id,
    realm_name=settings.realm,
    verify=True
)
pub_key="-----BEGIN PUBLIC KEY-----\n" + keycloak_openid.public_key() + "\n-----END PUBLIC KEY-----"


async def get_payload(token: str = Security(oauth2_scheme)) -> dict:
    try: 
        return keycloak_openid.decode_token(
            token,
            validate = True
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
            headers={"WWW-Authenticate": "Bearer"},
        )


async def get_user_info(payload: dict = Depends(get_payload)) -> userPayload:
    try:
        return userPayload(
            sub=payload.get("sub"),
            realm_roles=payload.get("realm_access", {}).get("roles", [])
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=str(e),
            headers={"WWW-Authenticate": "Bearer"},
        )
