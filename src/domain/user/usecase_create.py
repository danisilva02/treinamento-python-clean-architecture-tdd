from src.core.domain_error import DomainError
from src.domain.user.entity import UserEntity
from src.domain.user.contracts.usecase import UseCaseCreateUserContract
from src.domain.user.dto import UserCreateDTO, UserCreateOutputDTO
from src.domain.user.contracts.repository import UserRepoContract
from src.domain.user.contracts.security import SecurityContract

class UseCaseUserCreate(UseCaseCreateUserContract):
    
    def __init__(self, user_repo: UserRepoContract, security: SecurityContract):
        self.user_repo = user_repo
        self.security = security
    
    def perform(self, user: UserCreateDTO) -> tuple[DomainError, UserCreateOutputDTO]:
        try:
            if user == None or user == {}:
                return DomainError(**{
                    "message": "Params is required"
                }), None
            
            email = user.email
            if email == None:
                return DomainError(**{
                    "message": "Email is required"
                }), None
            
            if not UserEntity.valid_email(email):
                return DomainError(**{
                    "message": "Email is invalid"
                }), None
            
            name = user.name
            if name == None:
                return DomainError(**{
                    "message": "Name is required"
                }), None
            
            password = user.password
            if password == None:
                return DomainError(**{
                    "message": "Password is required"
                }), None
            
            if not UserEntity.valid_password(password):
                return DomainError(**{
                    "message": "Password is invalid"
                }), None
        
            error, user_return = self.user_repo.create(user=UserEntity(
                email=email,
                name=name,
                password_hash=self.security.hash_password(password),
            ))
            
            if error:
                return DomainError(**{
                    "message": str(error.message)
                }), None
            
            return None, UserCreateOutputDTO(
                id=user_return.id,
                email=user_return.email,
                name=user_return.name,
                created_at=user_return.created_at,
                updated_at=user_return.updated_at
            )
        except Exception as e:
            return DomainError(**{
                "message": str(e)
            }), None