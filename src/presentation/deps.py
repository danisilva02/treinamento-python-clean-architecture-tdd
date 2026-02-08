from fastapi import Request, HTTPException, status, Security
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from src.core.jwt import decode_token
from src.infra.driver.contract import DriverContract

# JWT
bearer = HTTPBearer(auto_error=False)

def get_current_user_id(creds: HTTPAuthorizationCredentials = Security(bearer)) -> str:
    try:
        if not creds or not creds.credentials or not creds.credentials.strip():
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing token")

        claims = decode_token(creds.credentials)
        if not isinstance(claims, dict) or not claims.get("user_id"):
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token is invalid")

        return claims["user_id"]
    except Exception:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Missing token")

# Driver Database
def get_driver(request: Request) -> DriverContract:
    return request.app.state.driver