from abc import abstractmethod, ABC
from src.domain.category.dto import (
    CategoryCreateInputDTO,
    CategoryCreateOutputDTO,
    UsecaseCategoryListOutputDTO,
    CategoryUpdateInputDTO,
    CategoryUpdateOutputDTO,
    UsecaseCategoryGetOutputDTO
)
from src.core.domain_error import DomainError

class UsecaseCategoryCreateContract(ABC):
    @abstractmethod
    def perform(self, params: CategoryCreateInputDTO) -> tuple[DomainError, CategoryCreateOutputDTO]:
        pass

class UsecaseCategoryListContract(ABC):
    @abstractmethod
    def perform(self, user_id: str) -> tuple[DomainError, list[UsecaseCategoryListOutputDTO]]:
        pass
    
class UsecaseCategoryUpdateContract(ABC):
    @abstractmethod
    def perform(self, id: str, params: CategoryUpdateInputDTO) -> tuple[DomainError, CategoryUpdateOutputDTO]:
        pass
    
class UsecaseCategoryGetContract(ABC):
    @abstractmethod
    def perform(self, id: str) -> tuple[DomainError, UsecaseCategoryGetOutputDTO]:
        pass