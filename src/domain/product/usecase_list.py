from src.core.domain_error import DomainError
from src.domain.product.dto import ProductOutputDTO, ProductListInputDTO
from src.domain.product.contracts.usecase import UsecaseProductListContract
from src.domain.product.contracts.repository import ProductRepositoryContract

class UsecaseProductList(UsecaseProductListContract):
    
    def __init__(self, product_repository: ProductRepositoryContract):
        self.product_repository = product_repository
        
    def perform(self, product: ProductListInputDTO) -> tuple[DomainError, ProductOutputDTO]:
        try:
            if not product.user_id:
                return DomainError(
                    message="User id is required"
                ), None
                
            list_repo_error, list_repo_success = self.product_repository.list(product.user_id)
            if list_repo_error:
                return DomainError(
                    message=list_repo_error.message
                ), None
                
            return None, [ProductOutputDTO(
                id=p.id,
                name=p.name,
                description=p.description,
                price=p.price,
                status=p.status,
                category_id=p.category_id,
                user_id=p.user_id,
                created_at=p.created_at,
                updated_at=p.updated_at,
            ) for p in list_repo_success]
        except Exception as e:
            return DomainError(
                message=str(e)
            ), None