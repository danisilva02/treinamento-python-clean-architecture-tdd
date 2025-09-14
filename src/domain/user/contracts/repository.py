from src.core.domain_error import DomainError
from abc import ABC, abstractmethod
from typing import Optional, Tuple
from src.domain.user.entity import UserEntity

class UserRepoContract(ABC):
    
    @abstractmethod
    def create(self, user: UserEntity) -> Tuple[Optional[DomainError], Optional[UserEntity]]:
        pass

    @abstractmethod
    def login(self, email: str, password_hash: str) -> Tuple[Optional[DomainError], Optional[UserEntity]]:
        pass
    
    @abstractmethod
    def get_by_id(self, id: int) -> Tuple[Optional[DomainError], Optional[UserEntity]]:
        pass
    
    @abstractmethod
    def update(self, user: UserEntity) -> Tuple[Optional[DomainError], Optional[UserEntity]]:
        pass