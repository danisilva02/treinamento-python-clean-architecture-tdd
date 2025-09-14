from src.core.domain_error import DomainError
from src.domain.category.contracts.usecase import UsecaseCategoryUpdateContract
from src.domain.category.contracts.repository import CategoryRepositoryContract
from src.domain.category.dto import CategoryUpdateInputDTO, CategoryUpdateOutputDTO

class UsecaseCategoryUpdate(UsecaseCategoryUpdateContract):
    
    def __init__(self, category_repository: CategoryRepositoryContract):
        self.category_repository = category_repository
        
    def perform(self, id: str, params: CategoryUpdateInputDTO) -> tuple[DomainError, CategoryUpdateOutputDTO]:
        try:
            if not id:
                return DomainError(
                    message="Id is required"
                ), None
            
            if not params.name and not params.status:
                return DomainError(
                    message="Params is required"
                ), None
                
            update_repo_error, update_repo_success = self.category_repository.update(id, name=params.name, status=params.status)
            if update_repo_error:
                return DomainError(
                    message="Error category update"
                ), None
                
            return None, CategoryUpdateOutputDTO(
                id=update_repo_success.id,
                name=update_repo_success.name,
                status=update_repo_success.status,
                user_id=update_repo_success.user_id,
                created_at=update_repo_success.created_at,
                updated_at=update_repo_success.updated_at
            )
        except Exception as e:
            return DomainError(
                message=str(e)
            ), None