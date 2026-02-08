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
                
            error_repo, success_repo = self.category_repository.update(
                id=id,
                name=params.name,
                status=params.status
            )
            if error_repo:
                return DomainError(
                    message=error_repo.message
                ), None
                
            return None, CategoryUpdateOutputDTO(
                id=success_repo.id,
                name=success_repo.name,
                status=success_repo.status,
                user_id=success_repo.user_id,
                created_at=success_repo.created_at,
                updated_at=success_repo.updated_at
            )
        except Exception as e:
            return DomainError(
                message=str(e)
            ), None