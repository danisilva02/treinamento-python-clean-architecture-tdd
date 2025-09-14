from dataclasses import dataclass
from abc import abstractmethod, ABC
from typing import Optional
from src.domain.category.entity import CategoryEntity
from src.core.domain_error import DomainError

@dataclass
class CategoryRepositoryContract(ABC):
    @abstractmethod
    def create(self, name: str, status: str, user_id: str) -> tuple[Optional[DomainError], Optional[CategoryEntity]]:
        pass
    
    @abstractmethod
    def list(self, user_id: str) -> tuple[Optional[DomainError], Optional[list[CategoryEntity]]]:
        pass
    
    @abstractmethod
    def update(self, id: str, name: str, status: str) -> tuple[Optional[DomainError], Optional[CategoryEntity]]:
        pass
    
    @abstractmethod
    def get(self, id: str) -> tuple[Optional[DomainError], Optional[CategoryEntity]]:
        pass