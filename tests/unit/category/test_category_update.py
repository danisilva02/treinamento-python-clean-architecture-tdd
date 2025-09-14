from unittest.mock import create_autospec

from src.domain.category.entity import CategoryEntity
from src.domain.category.contracts.repository import CategoryRepositoryContract
from src.domain.category.usecase_update import UsecaseCategoryUpdate
from src.domain.category.dto import CategoryUpdateInputDTO
    
def make_sut(is_exception: bool = False):
    category_repository_stub = create_autospec(CategoryRepositoryContract, instance=True)
    if is_exception:
        category_repository_stub.update.side_effect = Exception("Error category update")
    else:
        category_repository_stub.update.return_value = (None, CategoryEntity(
            id="123456abcd",
            name="Category 1",
            status="active",
            user_id="123456abcd",
            created_at="2021-01-01",
            updated_at="2021-01-01"
        ))
    sut = UsecaseCategoryUpdate(category_repository=category_repository_stub)
    return sut

def test_category_update_not_id():
    sut = make_sut()
    error, response = sut.perform(id=None, params=CategoryUpdateInputDTO(name=None, status=None))
    assert error.message == "Id is required"
    assert response is None
    
def test_category_update_not_params():
    sut = make_sut()
    error, response = sut.perform(id="123456abcd", params=CategoryUpdateInputDTO(name=None, status=None))
    assert error.message == "Params is required"
    assert response is None

def test_category_update_exception():
    sut = make_sut(is_exception=True)
    error, response = sut.perform(id="123456abcd", params=CategoryUpdateInputDTO(name="Category 1", status="active"))
    assert error.message == "Error category update"
    assert response is None

def test_category_update_success():
    sut = make_sut()
    error, response = sut.perform(id="123456abcd", params=CategoryUpdateInputDTO(name="Category 1", status="active"))
    assert error is None
    assert response is not None
    assert response.id == "123456abcd"
    assert response.name == "Category 1"
    assert response.status == "active"
    assert response.user_id == "123456abcd"
    assert response.created_at == "2021-01-01"
    assert response.updated_at == "2021-01-01"
    
    