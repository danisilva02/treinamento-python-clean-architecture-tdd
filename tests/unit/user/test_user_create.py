from unittest.mock import create_autospec

# Core
from src.core.domain_error import DomainError

# UseCase
from src.domain.user.usecase_create import UseCaseUserCreate
from src.domain.user.dto import UserCreateDTO
from src.domain.user.entity import UserEntity

# Contracts
from src.domain.user.contracts.repository import UserRepoContract
from src.domain.user.contracts.security import SecurityContract

def make_sut():
    user_repo_stub = create_autospec(UserRepoContract, instance=True)
    user_repo_stub.create.return_value = (None, UserEntity(**{
        "id": "123456abcd",
        "email": "daniel@gmail.com",
        "name": "Daniel",
        "created_at": "2025-01-01",
        "updated_at": "2025-01-01",
    }))
        
    security_stub = create_autospec(SecurityContract, instance=True)
    security_stub.hash_password.return_value = "password"
    
    sut = UseCaseUserCreate(user_repo=user_repo_stub, security=security_stub)
    return sut


def test_user_create_not_params():
    error, response = make_sut().perform(None)
    
    assert response is None
    assert error.message == "Params is required"
    assert isinstance(error, DomainError)


def test_user_create_not_email():
    error, response = make_sut().perform(UserCreateDTO(
        email=None,
        name="Daniel",
        password="@Password123",
    ))
    
    assert response is None
    assert error.message == "Email is required"
    assert isinstance(error, DomainError)

 
def test_user_create_invalid_email():
    error, response = make_sut().perform(UserCreateDTO(
        email="danielgmail.com",
        name="Daniel",
        password="@Password123",
    ))
    
    assert response is None
    assert error.message == "Email is invalid"
    assert isinstance(error, DomainError)


def test_user_create_not_name():
    error, response = make_sut().perform(UserCreateDTO(
        email="daniel@gmail.com",
        name=None,
        password="@Password123",
    ))
    
    assert response is None
    assert error.message == "Name is required"
    assert isinstance(error, DomainError)


def test_user_create_not_password():
    error, response = make_sut().perform(UserCreateDTO(
        email="daniel@gmail.com",
        name="Daniel",
        password=None,
    ))
    
    assert response is None
    assert error.message == "Password is required"
    assert isinstance(error, DomainError)


def test_user_create_invalid_password():
    error, response = make_sut().perform(UserCreateDTO(
        email="daniel@gmail.com",
        name="Daniel",
        password="123467",
    ))
    
    assert response is None
    assert error.message == "Password is invalid"
    assert isinstance(error, DomainError)


def test_user_create_success():
    error, response = make_sut().perform(UserCreateDTO(
        email="daniel@gmail.com",
        name="Daniel",
        password="@Password123",
    ))
    
    assert error is None
    assert response.id == "123456abcd"
    assert response.email == "daniel@gmail.com"
    assert response.name == "Daniel"
    assert response.created_at == "2025-01-01"
    assert response.updated_at == "2025-01-01"


def test_user_create_exception():
    sut = make_sut()
    sut.user_repo.create.side_effect = Exception("Database error")
    error, response = sut.perform(UserCreateDTO(
        email="daniel@gmail.com",
        name="Daniel",
        password="@Password123",
    ))
    
    assert response is None
    assert error.message == "Database error"
    assert isinstance(error, DomainError)