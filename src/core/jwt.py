import os
import jwt

def decode_token(token: str) -> dict:
    token_decode = jwt.decode(token, os.getenv("JWT_SECRET"), algorithms=["HS256"])
    
    if token_decode == None:
        return {"message": "Token is invalid"}
    
    return token_decode