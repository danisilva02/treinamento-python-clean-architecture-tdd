from src.core.domain_error import DomainError
from src.domain.product.contracts.usecase import UsecaseProductUpdateContract
from src.domain.product.entity import ProductEntity
from src.domain.product.dto import ProductUpdateInputDTO, ProductOutputDTO

from src.domain.product.contracts.repository import ProductRepositoryContract

class UsecaseProductUpdate(UsecaseProductUpdateContract):
    
    def __init__(self, product_repository: ProductRepositoryContract):
        self.product_repository = product_repository
        
    def perform(self, product: ProductUpdateInputDTO) -> tuple[DomainError, ProductOutputDTO]:
        try:
            if not product.id:
                return DomainError(
                    message="Id is required"
                ), None
                
            if not product.name and not product.description and not product.price and not product.status and not product.category_id and not product.user_id:
                return DomainError(
                    message="Params is required"
                ), None
                
            get_product_error, get_product_success = self.product_repository.get(id=product.id)
            if get_product_error:
                return DomainError(
                    message=get_product_error.message
                ), None
                
            print(get_product_success)
                
            update_repo_error, update_repo_success = self.product_repository.update(product=ProductEntity(
                id=product.id,
                name=product.name or get_product_success.name,
                description=product.description or get_product_success.description,
                price=product.price or get_product_success.price,
                status=product.status or get_product_success.status,
                category_id=product.category_id or get_product_success.category_id,
                user_id=product.user_id or get_product_success.user_id,
                created_at=get_product_success.created_at,
                updated_at=get_product_success.updated_at
            ))

            if update_repo_error:
                return DomainError(
                    message=update_repo_error.message
                ), None
                
            return None, ProductOutputDTO(
                id=update_repo_success.id,
                name=update_repo_success.name,
                description=update_repo_success.description,
                price=update_repo_success.price,
                status=update_repo_success.status,
                category_id=update_repo_success.category_id,
                user_id=update_repo_success.user_id,
                created_at=update_repo_success.created_at,
                updated_at=update_repo_success.updated_at
            )
        except Exception as e:
            return DomainError(
                message=str(e)
            ), None