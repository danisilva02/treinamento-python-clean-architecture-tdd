from unittest.mock import create_autospec

# Contracts
from src.domain.category.contracts.repository import CategoryRepositoryContract
from src.domain.category.dto import CategoryCreateInputDTO

# Entity
from src.domain.category.entity import CategoryEntity

# UseCase
from src.domain.category.usecase_create import UseCaseCategoryCreate

        
def make_sut(is_exception: bool = False):
    category_repository_stub = create_autospec(CategoryRepositoryContract, instance=True)
    if is_exception:
        category_repository_stub.create.side_effect = Exception("Error category create")
    else:
        category_repository_stub.create.return_value = (None, CategoryEntity(
            id="123456abcd",
            name="Category 1",
            status="active",
            user_id="123456abcd",
            created_at="2021-01-01",
            updated_at="2021-01-01"
        ))
    sut = UseCaseCategoryCreate(category_repository=category_repository_stub)
    return sut
    
        
def test_categoty_create_not_params():
    sut = make_sut()

    error, response = sut.perform(params=None)

    assert error.message == "Params is required"
    assert response is None


def test_categoty_create_not_name():
    sut = make_sut()
    
    error, response = sut.perform(CategoryCreateInputDTO(
        name=None,
        status="active",
        user_id="123456abcd",
    ))
    
    assert error.message == "Name is required"
    assert response is None
    

def test_categoty_create_not_status():
    sut = make_sut()
    
    error, response = sut.perform(CategoryCreateInputDTO(
        name="Category 1",
        status=None,
        user_id="123456abcd",
    ))
    
    assert error.message == "Status is required"
    assert response is None
    

def test_categoty_create_status_is_invalid():
    sut = make_sut()
    
    error, response = sut.perform(CategoryCreateInputDTO(
        name="Category 1",
        status="INvalid",
        user_id="123456abcd",
    ))
    
    assert error.message == "Status is invalid"
    assert response is None
    

def test_categoty_create_not_user_id():
    sut = make_sut()
    
    error, response = sut.perform(CategoryCreateInputDTO(
        name="Category 1",
        status="active",
        user_id=None,
    ))
    
    assert error.message == "User id is required"
    assert response is None
    
    
def test_categoty_create_exception():
    sut = make_sut(is_exception=True)
    
    error, response = sut.perform(CategoryCreateInputDTO(
        name="Category 1",
        status="active",
        user_id="123456abcd",
    ))
    
    assert error.message == "Error category create"
    assert response is None


def test_categoty_create_success():
    sut = make_sut()
    
    error, response = sut.perform(CategoryCreateInputDTO(
        name="Category 1",
        status="active",
        user_id="123456abcd",
    ))
    
    assert error is None
    assert response is not None
    
    assert response.id == "123456abcd"
    assert response.name == "Category 1"
    assert response.status == "active"
    assert response.user_id == "123456abcd"
    assert response.created_at == "2021-01-01"
    assert response.updated_at == "2021-01-01"