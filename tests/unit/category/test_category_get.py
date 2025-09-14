from unittest.mock import create_autospec
from src.domain.category.contracts.repository import CategoryRepositoryContract
from src.domain.category.entity import CategoryEntity
from src.domain.category.usecase_get import UsecaseCategoryGet
        
def make_sut():
    category_repository_stub = create_autospec(CategoryRepositoryContract, instance=True)
    category_repository_stub.get.return_value = (None, CategoryEntity(
        id="123456abcd",
        name="Category 1",
        status="active",
        user_id="123456abcd",
        created_at="2021-01-01",
        updated_at="2021-01-01"
    ))
    return UsecaseCategoryGet(category_repository=category_repository_stub)


def test_category_get_not_id():
    sut = make_sut()
    error, response = sut.perform(id=None)
    
    assert error.message == "Id is required"
    assert response is None
    

def test_category_get_exception():
    sut = make_sut()
    sut.category_repository.get.side_effect = Exception("Error category get")
    error, response = sut.perform(id="123456abcd")
    
    assert error.message == "Error category get"
    assert response is None
    

def test_category_get_success():
    sut = make_sut()
    error, response = sut.perform(id="123456abcd")
    
    assert error is None
    assert response is not None
    assert response.id == "123456abcd"
    assert response.name == "Category 1"
    assert response.status == "active"
    assert response.user_id == "123456abcd"
    assert response.created_at == "2021-01-01"
    assert response.updated_at == "2021-01-01"