from src.core.domain_error import DomainError
from src.domain.user.contracts.usecase import UseCaseLoginUserContract
from src.domain.user.dto import UserLoginDTO, UserLoginOutputDTO
from src.domain.user.contracts.repository import UserRepoContract
from src.domain.user.contracts.security import SecurityContract

class UseCaseUserLogin(UseCaseLoginUserContract):
    
    def __init__(self, user_repo: UserRepoContract, security: SecurityContract):
        self.user_repo = user_repo
        self.security = security
    
    def perform(self, user: UserLoginDTO) -> tuple[DomainError, UserLoginOutputDTO]:
        try:
            if user == None or user == {}:
                return DomainError(message="Params is required"), None
            
            email = user.email
            if email == None:
                return DomainError(message="Email is required"), None
            
            password = user.password
            if password == None:
                return DomainError(message="Password is required"), None

            error_login, success_login = self.user_repo.login(
                email=email,
                password_hash=self.security.hash_password(password),
            )
            
            if error_login:
                return DomainError(
                    message=error_login.message,
                    status_code=401
                ), None
            
            return None, UserLoginOutputDTO(token=self.security.generate_token(success_login.id))
        except Exception as e:
            return DomainError(
                message=str(e),
                status_code=500
            ), None