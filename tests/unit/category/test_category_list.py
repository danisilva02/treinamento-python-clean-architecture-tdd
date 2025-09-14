from unittest.mock import create_autospec

from src.core.domain_error import DomainError
from src.domain.category.contracts.repository import CategoryRepositoryContract
from src.domain.category.dto import CategoryListInputDTO
from src.domain.category.entity import CategoryEntity
from src.domain.category.usecase_list import UsecaseCategoryList
 
def make_sut(is_exception: bool = False):
    category_repository_stub = create_autospec(CategoryRepositoryContract, instance=True)
    if is_exception:
        category_repository_stub.list.side_effect = Exception("Error category list")
    else:
        category_repository_stub.list.return_value = (None, [
            CategoryEntity(
                id="cat-1",
                name="Category 1",
                status="active",
                user_id="u-1",
                created_at="2021-01-01",
                updated_at="2021-01-01",
            ),
            CategoryEntity(
                id="cat-2",
                name="Category 2",
                status="active",
                user_id="u-1",
                created_at="2021-01-01",
                updated_at="2021-01-01",
            ),
        ])
    sut = UsecaseCategoryList(category_repository=category_repository_stub)
    return sut, category_repository_stub
        
def test_category_list_not_user_id():
    sut, category_repository_stub = make_sut()
    list_error, list_success = sut.perform(params=CategoryListInputDTO(user_id=None))
    
    assert isinstance(list_error, DomainError)
    assert list_success is None
    category_repository_stub.list.assert_not_called()
    
def test_category_list_exception():
    sut, category_repository_stub = make_sut(is_exception=True)
    list_error, list_success = sut.perform(params=CategoryListInputDTO(user_id="u-1"))
    
    assert isinstance(list_error, DomainError)
    assert list_success is None
    category_repository_stub.list.assert_called_once_with(user_id="u-1")
    
def test_category_list_success():
    sut, category_repository_stub = make_sut()
    list_error, list_success = sut.perform(params=CategoryListInputDTO(user_id="u-1"))
    
    assert list_error is None
    assert list_success is not None
    category_repository_stub.list.assert_called_once_with(user_id="u-1")
    
    assert len(list_success) == 2
    assert list_success[0].id == "cat-1"
    assert list_success[0].name == "Category 1"
    assert list_success[0].status == "active"
    assert list_success[0].user_id == "u-1"
    assert list_success[0].created_at == "2021-01-01"
    assert list_success[0].updated_at == "2021-01-01"
    assert list_success[1].id == "cat-2"
    assert list_success[1].name == "Category 2"
    assert list_success[1].status == "active"
    assert list_success[1].user_id == "u-1"
    assert list_success[1].created_at == "2021-01-01"
    assert list_success[1].updated_at == "2021-01-01"
        