from src.core.domain_error import DomainError
from src.domain.category.contracts.usecase import UsecaseCategoryGetContract
from src.domain.category.contracts.repository import CategoryRepositoryContract
from src.domain.category.dto import UsecaseCategoryGetOutputDTO

class UsecaseCategoryGet(UsecaseCategoryGetContract):
    
    def __init__(self, category_repository: CategoryRepositoryContract):
        self.category_repository = category_repository
        
    def perform(self, id: str) -> tuple[DomainError, UsecaseCategoryGetOutputDTO]:
        try:
            if not id:
                return DomainError(
                    message="Id is required"
                ), None
            
            get_repo_error, get_repo_success = self.category_repository.get(id)
            if get_repo_error:
                return DomainError(
                    message=get_repo_error.message
                ), None

            return None, UsecaseCategoryGetOutputDTO(
                id=get_repo_success.id,
                name=get_repo_success.name,
                status=get_repo_success.status,
                user_id=get_repo_success.user_id,
                created_at=get_repo_success.created_at,
                updated_at=get_repo_success.updated_at
            )
        except Exception as e:
            return DomainError(
                message=str(e)
            ), None