from src.core.domain_error import DomainError
from typing import Optional, Dict, Any
from abc import abstractmethod, ABC

JsonDict = Dict[str, Any]

class DriverContract(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def execute(self, sql: str, args: tuple, returning: str) -> tuple[DomainError, Optional[JsonDict]]:
        pass