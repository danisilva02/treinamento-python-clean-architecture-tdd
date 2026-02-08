from unittest.mock import create_autospec
from src.domain.category.contracts.repository import CategoryRepositoryContract
from src.domain.category.usecase_delete import UsecaseCategoryDelete

def make_sut():
    category_repository_stub = create_autospec(CategoryRepositoryContract, instance=True)
    category_repository_stub.delete.return_value = (None, True)
        
    return UsecaseCategoryDelete(category_repository=category_repository_stub)
    
def test_category_delete_not_id():
    sut = make_sut()
    error, response = sut.perform(id=None)
    assert error.message == "Id is required"
    assert response is None
    
def test_category_delete_exception():
    sut = make_sut()
    sut.category_repository.delete.side_effect = Exception("Error category delete")
    error, response = sut.perform(id="123456abcd")
    assert error.message == "Error category delete"
    assert response is None
    
def test_category_delete_success():
    sut = make_sut()
    error, response = sut.perform(id="123456abcd")
    assert error is None
    assert response is True