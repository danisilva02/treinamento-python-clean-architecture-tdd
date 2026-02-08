# Core
from src.core.domain_error import DomainError

# Domain
from src.domain.user.usecase_create import UseCaseUserCreate, UserCreateDTO
from src.domain.user.usecase_login import UseCaseUserLogin, UserLoginDTO
from src.domain.user.usecase_me import UseCaseUserMe, UserMeDTO
from src.domain.user.usecase_update import UsecaseUserUpdate, UserUpdateInputDTO

# Infra
from src.infra.repository.user.repo import UserRepo
from src.infra.security.security import Security
from src.infra.driver.contract import DriverContract

# Presentation
from src.presentation.contract.user import (
    PresentationUserCreateRequestDTO,
    PresentationUserCreateResponseDTO,
    PresentationUserLoginRequestDTO,
    PresentationUserLoginResponseDTO,
    PresentationUserMeRequestDTO,
    PresentationUserMeResponseDTO,
    PresentationUserUpdateRequestDTO,
    PresentationUserUpdateResponseDTO,
)

def controller_create_user(
    driver: DriverContract,
    user: PresentationUserCreateRequestDTO
) -> tuple[DomainError, PresentationUserCreateResponseDTO]:
    user_repo = UserRepo(driver=driver)
    security_repo = Security()
    usecase_user_create = UseCaseUserCreate(user_repo=user_repo, security=security_repo)
    user_create_error, user_create_success = usecase_user_create.perform(
        user=UserCreateDTO(
            email=user.email,
            name=user.name,
            password=user.password,
        )
    )
    
    if user_create_error:
        return DomainError(
            message=user_create_error.message,
            status_code=user_create_error.status_code
        ), None
    
    return None, PresentationUserCreateResponseDTO(
        id=user_create_success.id,
        email=user_create_success.email,
        name=user_create_success.name,
        created_at=user_create_success.created_at,
        updated_at=user_create_success.updated_at
    )

 
def controller_update_user(
    driver: DriverContract,
    user: PresentationUserUpdateRequestDTO,
    user_id: str
) -> tuple[DomainError, PresentationUserUpdateResponseDTO]:
    user_repo = UserRepo(driver=driver)
    usecase_user_update = UsecaseUserUpdate(user_repository=user_repo)
    user_update_error, user_update_response = usecase_user_update.perform(
        user=UserUpdateInputDTO(
            id=user_id,
            name=user.name,
            email=user.email,
        )
    )

    if user_update_error:
        return DomainError(
            message=user_update_error.message,
            status_code=user_update_error.status_code
        ), None
    
    return None, PresentationUserUpdateResponseDTO(
        id=user_update_response.id,
        name=user_update_response.name,
        email=user_update_response.email,
        created_at=user_update_response.created_at,
        updated_at=user_update_response.updated_at
    )


def controller_login_user(
    driver: DriverContract,
    login_user: PresentationUserLoginRequestDTO
) -> tuple[DomainError, PresentationUserLoginResponseDTO]:
    user_repo = UserRepo(driver=driver)
    security_repo = Security()
    usecase_user_login = UseCaseUserLogin(user_repo=user_repo, security=security_repo)
    user_login_error, user_login_success = usecase_user_login.perform(
        user=UserLoginDTO(
            email=login_user.email,
            password=login_user.password,
        )
    )
    
    if user_login_error:
        return DomainError(
            message=user_login_error.message,
            status_code=user_login_error.status_code
        ), None
    
    return None, PresentationUserLoginResponseDTO(
        token=user_login_success.token,
    )

   
def controller_me_user(
    driver: DriverContract,
    me_user: PresentationUserMeRequestDTO
) -> tuple[DomainError, PresentationUserMeResponseDTO]:
    user_repo = UserRepo(driver=driver)
    usecase_user_me = UseCaseUserMe(user_repo=user_repo)
    user_me_error, user_me_response = usecase_user_me.perform(
        user=UserMeDTO(
            user_id=me_user.user_id,
        )
    )
    
    if user_me_error:
        return DomainError(
            message=user_me_error.message,
            status_code=user_me_error.status_code
        ), None
    
    return None, PresentationUserMeResponseDTO(
        id=user_me_response.id,
        email=user_me_response.email,
        name=user_me_response.name,
        created_at=user_me_response.created_at,
        updated_at=user_me_response.updated_at
    )