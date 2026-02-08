from abc import ABC, abstractmethod
from src.domain.product.entity import ProductEntity
from src.core.domain_error import DomainError

class ProductRepositoryContract(ABC):
    
    @abstractmethod
    def create(
        self,
        name: str,
        description: str,
        price: int,
        status: str,
        category_id: str,
        user_id: str
    ) -> tuple[DomainError, ProductEntity]:
        pass
    
    @abstractmethod
    def get(self, id: str) -> tuple[DomainError, ProductEntity]:
        pass
    
    @abstractmethod
    def list(self, user_id: str) -> tuple[DomainError, list[ProductEntity]]:
        pass
    
    @abstractmethod
    def update(self, product: ProductEntity) -> tuple[DomainError, ProductEntity]:
        pass
    
    @abstractmethod
    def delete(self, id: str) -> tuple[DomainError, bool]:
        pass