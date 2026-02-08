from hashlib import md5
from typing import Optional
import os
import jwt
from datetime import timedelta, datetime, timezone
from src.domain.user.contracts.security import SecurityContract, Claims

JWT_SECRET = os.getenv("JWT_SECRET", "secret")

class Security(SecurityContract):
    def generate_token(self, user_id: str) -> str:
        return jwt.encode({"user_id": user_id, "exp": datetime.now(timezone.utc) + timedelta(days=1)}, JWT_SECRET, algorithm="HS256")
    
    def verify_token(self, token: str) -> tuple[Optional[dict], Optional[Claims]]:
        try:
            return None, jwt.decode(token, JWT_SECRET, algorithms=["HS256"])
        except Exception as e:
            return {"message": "Token is invalid"}, None
    
    def hash_password(self, password: str) -> str:
        return md5(password.encode('utf-8')).hexdigest()