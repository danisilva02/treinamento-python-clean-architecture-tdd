from src.core.domain_error import DomainError
from src.domain.category.contracts.usecase import UsecaseCategoryListContract
from src.domain.category.contracts.repository import CategoryRepositoryContract
from src.domain.category.dto import UsecaseCategoryListOutputDTO, CategoryListInputDTO

class UsecaseCategoryList(UsecaseCategoryListContract):
    
    def __init__(self, category_repository: CategoryRepositoryContract):
        self.category_repository = category_repository
        
    def perform(self, params: CategoryListInputDTO) -> tuple[DomainError, list[UsecaseCategoryListOutputDTO]]:
        try:
            if not params.user_id:
                return DomainError(
                    message="User id is required"
                ), None
                
            list_repo_error, list_repo_success = self.category_repository.list(params.user_id)
            if list_repo_error:
                return DomainError(
                    message=list_repo_error.message
                ), None
                
            return None, [
                UsecaseCategoryListOutputDTO(
                    id=c.id,
                    name=c.name,
                    status=c.status,
                    user_id=c.user_id,
                    created_at=c.created_at,
                    updated_at=c.updated_at,
                )
                for c in list_repo_success
            ]         
        except Exception as e:
            return DomainError(
                message=str(e)
            ), None