from src.core.domain_error import DomainError
from src.domain.category.contracts.usecase import UsecaseCategoryCreateContract
from src.domain.category.contracts.repository import CategoryRepositoryContract
from src.domain.category.dto import CategoryCreateOutputDTO, CategoryCreateInputDTO

ALLOWED_STATUS = {"active", "inactive"}

class UseCaseCategoryCreate(UsecaseCategoryCreateContract):
    def __init__(self, category_repository: CategoryRepositoryContract):
        self.category_repository = category_repository
        
    def perform(self, params: CategoryCreateInputDTO) -> tuple[DomainError | None, CategoryCreateOutputDTO | None]:
        try:
            if params is None or params == {}:
                return DomainError(
                    message="Params is required"
                ), None
                
            name = params.name
            if not name:
                return DomainError(
                    message="Name is required"
                ), None
                
            status = params.status
            if not status:
                return DomainError(
                    message="Status is required"
                ), None
                
            if status.lower() not in ALLOWED_STATUS:
                return DomainError(
                    message="Status is invalid"
                ), None
            
            user_id = params.user_id
            if not user_id:
                return DomainError(
                    message="User id is required"
                ), None
                
            create_category_error, create_category_success = self.category_repository.create(
                name=name,
                status=status,
                user_id=user_id,
            )
            if create_category_error:
                return DomainError(
                    message=create_category_error.message
                ), None
                
            return None, CategoryCreateOutputDTO(
                id= create_category_success.id,
                name= create_category_success.name,
                status= create_category_success.status,
                user_id= create_category_success.user_id,
                created_at= create_category_success.created_at,
                updated_at= create_category_success.updated_at
            )
        except Exception as e:
            return DomainError(
                message=str(e)
            ), None