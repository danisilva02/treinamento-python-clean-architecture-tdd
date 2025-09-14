from unittest.mock import create_autospec

# Core
from src.core.domain_error import DomainError

# UseCase
from src.domain.user.usecase_login import UseCaseUserLogin
from src.domain.user.dto import UserLoginDTO
from src.domain.user.entity import UserEntity

# Contracts
from src.domain.user.contracts.repository import UserRepoContract
from src.domain.user.contracts.security import SecurityContract

def make_sut(is_exception: bool = False):
    user_repo_stub = create_autospec(UserRepoContract, instance=True)
    if is_exception:
        user_repo_stub.login.side_effect = Exception("Database error")
    else:
        user_repo_stub.login.return_value = (None, UserEntity(**{
            "id": "123456abcd",
            "email": "daniel@gmail.com",
            "name": "Daniel",
            "created_at": "2025-01-01",
            "updated_at": "2025-01-01",
        }))
        
    security_stub = create_autospec(SecurityContract, instance=True)
    security_stub.generate_token.return_value = "token"
    
    sut = UseCaseUserLogin(user_repo=user_repo_stub, security=security_stub)
    return sut


def test_user_login_not_params():
    sut = make_sut()
    error, success = sut.perform(user=None)
    
    assert success is None
    assert error.message == "Params is required"
    assert isinstance(error, DomainError)
    

def test_user_login_not_email():
    sut = make_sut()
    error, success = sut.perform(user=UserLoginDTO(
        email=None,
        password="12345678",
    ))
    
    assert success is None
    assert error.message == "Email is required"
    assert isinstance(error, DomainError)
    

def test_user_login_not_password():
    sut = make_sut()
    error, success = sut.perform(user=UserLoginDTO(
        email="daniel@gmail.com",
        password=None,
    ))
    
    assert success is None
    assert error.message == "Password is required"
    assert isinstance(error, DomainError)


def test_user_login_success():
    sut = make_sut()
    error, success = sut.perform(user=UserLoginDTO(
        email="daniel@gmail.com",
        password="@P4ssw0rd",
    ))
    
    assert error is None
    assert success.token is not None
    

def test_user_login_exception():
    sut = make_sut(is_exception=True)
    error, success = sut.perform(UserLoginDTO(
        email="daniel@gmail.com",
        password="@P4ssw0rd",
    ))
    
    assert error.message == "Database error"
    assert isinstance(error, DomainError)
    assert success is None