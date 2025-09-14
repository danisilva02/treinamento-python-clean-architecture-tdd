from src.core.domain_error import DomainError
from src.domain.product.contracts.usecase import UsecaseProductGetContract
from src.domain.product.contracts.repository import ProductRepositoryContract
from src.domain.product.dto import ProductGetInputDTO, ProductOutputDTO

class UsecaseProductGet(UsecaseProductGetContract):
    
    def __init__(self, product_repository: ProductRepositoryContract):
        self.product_repository = product_repository
    
    def perform(self, product: ProductGetInputDTO) -> tuple[DomainError, ProductOutputDTO]:
        try:
            if not product.id:
                return DomainError(
                    message="Id is required"
                ), None
                
            get_repo_error, get_repo_success = self.product_repository.get(product.id)
            if get_repo_error:
                return DomainError(
                    message=get_repo_error.message
                ), None
            
            return None, ProductOutputDTO(
                id=get_repo_success.id,
                name=get_repo_success.name,
                description=get_repo_success.description,
                price=get_repo_success.price,
                status=get_repo_success.status,
                category_id=get_repo_success.category_id,
                user_id=get_repo_success.user_id,
                created_at=get_repo_success.created_at,
                updated_at=get_repo_success.updated_at
            )
        except Exception as e:
            return DomainError(
                message=str(e)
            ), None