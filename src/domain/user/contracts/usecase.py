from src.core.domain_error import DomainError
from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Optional, Tuple

from src.domain.user.dto import (
    # User
    UserCreateDTO,
    UserCreateOutputDTO,
    # Login
    UserLoginDTO,
    UserLoginOutputDTO,
    # Me
    UserMeDTO,
    UserMeOutputDTO,
    # Update
    UserUpdateInputDTO,
    UserUpdateOutputDTO,
)

@dataclass
class UseCaseUserCreateInput:
    email: str
    name: str
    password: str

class UseCaseCreateUserContract(ABC):
    @abstractmethod
    def perform(self, user: UserCreateDTO) -> Tuple[Optional[DomainError], Optional[UserCreateOutputDTO]]:
        pass
 
   
class UseCaseLoginUserContract(ABC):
    @abstractmethod
    def perform(self, user: UserLoginDTO) -> Tuple[Optional[DomainError], Optional[UserLoginOutputDTO]]:
        pass

    
class UseCaseUserMeContract(ABC):
    @abstractmethod
    def perform(self, user: UserMeDTO) -> Tuple[Optional[DomainError], Optional[UserMeOutputDTO]]:
        pass
    
class UseCaseUserUpdateContract(ABC):
    @abstractmethod
    def perform(self, user: UserUpdateInputDTO) -> Tuple[Optional[DomainError], Optional[UserUpdateOutputDTO]]:
        pass