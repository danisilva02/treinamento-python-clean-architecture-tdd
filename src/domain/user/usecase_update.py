from src.core.domain_error import DomainError
from src.domain.user.entity import UserEntity
from src.domain.user.contracts.usecase import UseCaseUserUpdateContract
from src.domain.user.dto import UserUpdateInputDTO, UserUpdateOutputDTO
from src.domain.user.contracts.repository import UserRepoContract

class UsecaseUserUpdate(UseCaseUserUpdateContract):
    
    def __init__(self, user_repository: UserRepoContract):
        self.user_repository = user_repository
        
    def perform(self, user: UserUpdateInputDTO) -> tuple[DomainError, UserUpdateOutputDTO]:
        try:
            if not user.id:
                return DomainError(
                    message="Id is required"
                ), None
                
            exist_user_error, exist_user_success = self.user_repository.get_by_id(id=user.id)
            if exist_user_error:
                return DomainError(
                    message="User not found"
                ), None
                
            if not user.name and not user.email:
                return DomainError(
                    message="Params is required"
                ), None
                
            error_repo, success_repo = self.user_repository.update(user=UserEntity(
                id=user.id,
                name=user.name or exist_user_success.name,
                email=user.email or exist_user_success.email,
            ))
            
            if error_repo:
                return DomainError(
                    message=error_repo.message
                ), None
            
            return None, UserUpdateOutputDTO(
                id=success_repo.id,
                name=success_repo.name,
                email=success_repo.email,
                created_at=success_repo.created_at,
                updated_at=success_repo.updated_at
            )
        except Exception as e:
            return DomainError(
                message=str(e)
            ), None