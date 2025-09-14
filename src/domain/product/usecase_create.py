from src.core.domain_error import DomainError
from src.domain.product.contracts.repository import ProductRepositoryContract
from src.domain.product.dto import ProductCreateInputDTO, ProductOutputDTO

ALLOWED_STATUS = {"active", "inactive"}

class UseCaseProductCreate:
    def __init__(self, product_repository: ProductRepositoryContract):
        self.product_repository = product_repository
    
    def perform(self, params: ProductCreateInputDTO) -> tuple[DomainError, ProductOutputDTO]:
        try:
            if not params or params == {}:
                return DomainError(
                    message="Params is required"
                ), None
                
            name = params.name
            if not name:
                return DomainError(
                    message="Name is required"
                ), None
                
            description = params.description
            if not description:
                return DomainError(
                    message="Description is required"
                ), None
                
            price = params.price
            if price is None or not isinstance(price, int) or price <= 0:
                return DomainError(
                    message="Price is required and must be an integer"
                ), None
                
            status = params.status
            if not status:
                return DomainError(
                    message="Status is required"
                ), None
                
            if status not in ALLOWED_STATUS:
                return DomainError(
                    message="Status is invalid"
                ), None
                
            category_id = params.category_id
            if not category_id:
                return DomainError(
                    message="Category id is required"
                ), None
                
            user_id = params.user_id
            if not user_id:
                return DomainError(
                    message="User id is required"
                ), None
                
            create_product_error, create_product_success = self.product_repository.create(
                name=name,
                description=description,
                price=price,
                status=status,
                category_id=category_id,
                user_id=user_id,
            )
            if create_product_error:
                return DomainError(
                    message=create_product_error.message
                ), None
                
            return None, ProductOutputDTO(
                id=create_product_success.id,
                name=create_product_success.name,
                description=create_product_success.description,
                price=create_product_success.price,
                status=create_product_success.status,
                category_id=create_product_success.category_id,
                user_id=create_product_success.user_id,
                created_at=create_product_success.created_at,
                updated_at=create_product_success.updated_at
            )
        except:
            return DomainError(
                message=f"Error product create"
            ), None