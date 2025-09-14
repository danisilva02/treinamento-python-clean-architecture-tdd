from unittest.mock import create_autospec

# Core
from src.core.domain_error import DomainError

# UseCase
from src.domain.user.usecase_update import UsecaseUserUpdate
from src.domain.user.dto import UserUpdateInputDTO
from src.domain.user.contracts.repository import UserRepoContract
from src.domain.user.entity import UserEntity
    
def make_sut():
    user_repository_stub = create_autospec(UserRepoContract, instance=True)
    user_repository_stub.get_by_id.return_value = (None, UserEntity(
        id="123456abcd",
        name="John Doe",
        email="john.doe@example.com",
        created_at="2021-01-01",
        updated_at="2021-01-01"
    ))
    user_repository_stub.update.return_value = (None, UserEntity(
        id="123456abcd",
        name="John Doe",
        email="john.doe@example.com",
        created_at="2021-01-01",
        updated_at="2021-01-01"
    ))
    sut = UsecaseUserUpdate(user_repository=user_repository_stub)
    return sut

def test_user_update_not_id():
    sut = make_sut()
    error, response = sut.perform(user=UserUpdateInputDTO(id=None, name="John Doe", email="john.doe@example.com"))
    assert error.message == "Id is required"
    assert response is None
    
def test_user_update_not_params():
    sut = make_sut()
    error, response = sut.perform(user=UserUpdateInputDTO(id="123456abcd", name=None, email=None))
    assert error.message == "Params is required"
    assert response is None
    
def test_user_update_exception():
    sut = make_sut()
    sut.user_repository.update.side_effect = Exception("Error user update")
    error, response = sut.perform(user=UserUpdateInputDTO(id="12346abcd", name="John Doe", email="john.doe@example.com"))
    assert error.message == "Error user update"
    assert response is None
    
def test_user_update_not_found():
    sut = make_sut()
    sut.user_repository.get_by_id.return_value = (DomainError(message="User not found"), None)
    error, response = sut.perform(user=UserUpdateInputDTO(id="123456abcd", name="John Doe", email="john.doe@example.com"))
    assert error.message == "User not found"
    assert response is None
    
def test_user_update_success():
    sut = make_sut()
    error, response = sut.perform(user=UserUpdateInputDTO(id="123456abcd", name="John Doe", email="john.doe@example.com"))
    
    assert error is None
    assert response is not None
    assert response.id == "123456abcd"
    assert response.name == "John Doe"
    assert response.email == "john.doe@example.com"
    assert response.created_at == "2021-01-01"
    assert response.updated_at == "2021-01-01"