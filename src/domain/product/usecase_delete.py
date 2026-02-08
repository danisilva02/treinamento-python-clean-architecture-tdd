from src.domain.product.contracts.repository import ProductRepositoryContract
from src.domain.product.contracts.usecase import UsecaseProductDeleteContract
from src.core.domain_error import DomainError

class UsecaseProductDelete(UsecaseProductDeleteContract):
    def __init__(self, product_repository: ProductRepositoryContract):
        self.product_repository = product_repository
        
    def perform(self, id: str) -> tuple[DomainError, bool]:
        try:
            if not id:
                return DomainError(
                    message="Id is required"
                ), None
            delete_repo_error, _ = self.product_repository.delete(id)
            if delete_repo_error:
                return DomainError(
                    message=delete_repo_error.message
                ), None
            return None, True
        except Exception as e:
            return DomainError(
                message=str(e)
            ), None