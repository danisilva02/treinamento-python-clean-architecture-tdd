from unittest.mock import create_autospec

# UseCase
from src.domain.user.usecase_me import UseCaseUserMe
from src.domain.user.dto import UserMeDTO
from src.domain.user.entity import UserEntity

# Contracts
from src.domain.user.contracts.repository import UserRepoContract

def make_sut(is_exception: bool = False):
    user_repo_stub = create_autospec(UserRepoContract, instance=True)
    if is_exception:
        user_repo_stub.get_by_id.side_effect = Exception("Database error")
    else:
        user_repo_stub.get_by_id.return_value = (None, UserEntity(
            id="123456abcd",
            email="test@test.com",
            name="Test",
            created_at="2021-01-01",
            updated_at="2021-01-01"
        ))
        
    usecase = UseCaseUserMe(user_repo=user_repo_stub)
    return usecase


def test_user_me_not_params():
    sut = make_sut()
    
    error, success = sut.perform(user=None)
    
    assert error.message == "Params is required"
    assert success is None


def test_user_me_not_user_id():
    sut = make_sut()
    
    error, success = sut.perform(user=UserMeDTO(
        user_id=None,
    ))
    
    assert error.message == "User id is required"
    assert success is None
    

def test_user_me_success():
    sut = make_sut()
    
    error, success = sut.perform(user=UserMeDTO(
        user_id="123456abcd",
    ))
    
    assert error is None
    assert success.id == "123456abcd"
    assert success.email == "test@test.com"
    assert success.name == "Test"
    assert success.created_at == "2021-01-01"
    assert success.updated_at == "2021-01-01"


def test_user_me_exception():
    sut = make_sut(is_exception=True)
    
    error, success = sut.perform(user=UserMeDTO(
        user_id="123456abcd",
    ))
    
    assert error.message == "Error user me"
    assert success is None