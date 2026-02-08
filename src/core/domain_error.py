from dataclasses import dataclass
from typing import Optional

@dataclass
class DomainError:
    message: str
    status_code: Optional[int] = 400
    error_code: Optional[str] = "BAD_REQUEST"