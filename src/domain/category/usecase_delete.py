from src.domain.category.contracts.repository import CategoryRepositoryContract
from src.domain.category.contracts.usecase import UsecaseCategoryDeleteContract
from src.core.domain_error import DomainError

class UsecaseCategoryDelete(UsecaseCategoryDeleteContract):
    def __init__(self, category_repository: CategoryRepositoryContract):
        self.category_repository = category_repository
        
    def perform(self, id: str) -> tuple[DomainError | None, bool | None]:
        try:
            if not id:
                return DomainError(
                    message="Id is required"
                ), None
            delete_repo_error, _ = self.category_repository.delete(id)
            if delete_repo_error:
                return DomainError(
                    message=delete_repo_error.message
                ), None
            return None, True
        except Exception as e:
            return DomainError(
                message=str(e)
            ), None