from dataclasses import dataclass
from typing import Optional

@dataclass
class DomainError:
    message: str
    status_code: Optional[int] = None
    error_code: Optional[str] = None