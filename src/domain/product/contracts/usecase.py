from abc import ABC, abstractmethod
from src.core.domain_error import DomainError
from src.domain.product.dto import ProductGetInputDTO, ProductOutputDTO, ProductListInputDTO, ProductUpdateInputDTO

class UsecaseProductGetContract(ABC):
    @abstractmethod
    def perform(self, product: ProductGetInputDTO) -> tuple[DomainError, ProductOutputDTO]:
        pass
    
class UsecaseProductListContract(ABC):
    @abstractmethod
    def perform(self, product: ProductListInputDTO) -> tuple[DomainError, ProductOutputDTO]:
        pass
    
class UsecaseProductUpdateContract(ABC):
    @abstractmethod
    def perform(self, product: ProductUpdateInputDTO) -> tuple[DomainError, ProductOutputDTO]:
        pass
    
class UsecaseProductDeleteContract(ABC):
    @abstractmethod
    def perform(self, id: str) -> tuple[DomainError, bool]:
        pass