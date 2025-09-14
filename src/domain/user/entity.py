import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from uuid import UUID, uuid4

_EMAIL_RE = re.compile(r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$")
_PWD_RE   = re.compile(r"^(?=.*[A-Z])(?=.*\d)\S{8,}$")

@dataclass
class UserEntity:
    email: str
    name: str
    password_hash: str | None = None

    id: UUID = field(default_factory=uuid4)
    created_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = field(default_factory=lambda: datetime.now(timezone.utc))

    @staticmethod
    def valid_email(email: str) -> bool:
        return _EMAIL_RE.fullmatch(email) is not None

    @staticmethod
    def valid_password(passwordh: str) -> bool:
        return _PWD_RE.fullmatch(passwordh) is not None