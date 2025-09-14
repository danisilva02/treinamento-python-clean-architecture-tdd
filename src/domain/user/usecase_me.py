from src.core.domain_error import DomainError
from src.domain.user.dto import UserMeDTO, UserMeOutputDTO
from src.domain.user.contracts.usecase import UseCaseUserMeContract
from src.domain.user.contracts.repository import UserRepoContract

class UseCaseUserMe(UseCaseUserMeContract):
    
    def __init__(self, user_repo: UserRepoContract):
        self.user_repo = user_repo
    
    def perform(self, user: UserMeDTO) -> tuple[DomainError, UserMeOutputDTO]:
        try:
            if not user or user == {}:
                return DomainError(message="Params is required"), None
            
            user_id = user.user_id
            if not user_id:
                return DomainError(message="User id is required"), None
            
            error_repo, success_repo = self.user_repo.get_by_id(id=user_id)
            if error_repo:
                return DomainError(message=error_repo.message), None
            
            return None, success_repo
        except Exception as e:
            return DomainError(message="Error user me"), None