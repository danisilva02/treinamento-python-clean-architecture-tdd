from unittest.mock import create_autospec

from src.core.domain_error import DomainError
from src.domain.product.entity import ProductEntity
from src.domain.product.dto import ProductListInputDTO
from src.domain.product.contracts.repository import ProductRepositoryContract
from src.domain.product.usecase_list import UsecaseProductList

        
def make_sut():
    product_repository_stub = create_autospec(ProductRepositoryContract, instance=True)
    product_repository_stub.list.return_value = (None, [
        ProductEntity(
            id="1",
            name="Product 1",
            description="Product 1 description",
            price=100,
            status="active",
            category_id="1",
            user_id="1",
            created_at="2021-01-01",
            updated_at="2021-01-01",
        ),
        ProductEntity(
            id="2",
            name="Product 2",
            description="Product 2 description",
            price=200,
            status="active",
            category_id="2",
            user_id="1",
            created_at="2021-01-01",
            updated_at="2021-01-01",
        )
    ])
    sut = UsecaseProductList(product_repository=product_repository_stub)
    return sut


def test_product_not_user_id():
    sut = make_sut()
    error, response = sut.perform(product=ProductListInputDTO(user_id=None))
    
    assert response is None
    assert error is not None
    assert error.message == "User id is required"
    assert isinstance(error, DomainError)
    

def test_product_exception():
    sut = make_sut()
    sut.product_repository.list.side_effect = Exception("Error product list")
    error, response = sut.perform(product=ProductListInputDTO(user_id="1"))
    
    assert response is None
    assert error is not None
    assert error.message == "Error product list"
    assert isinstance(error, DomainError)
    
def test_product_success():
    sut = make_sut()
    error, response = sut.perform(product=ProductListInputDTO(user_id="1"))
    
    assert error is None
    assert response is not None
    assert len(response) == 2
    
    # First product
    assert response[0].id == "1"
    assert response[0].name == "Product 1"
    assert response[0].description == "Product 1 description"
    assert response[0].price == 100
    assert response[0].status == "active"
    assert response[0].category_id == "1"
    assert response[0].user_id == "1"
    assert response[0].created_at == "2021-01-01"
    assert response[0].updated_at == "2021-01-01"
    
    # Second product
    assert response[1].name == "Product 2"
    assert response[1].description == "Product 2 description"
    assert response[1].price == 200
    assert response[1].status == "active"
    assert response[1].category_id == "2"
    assert response[1].user_id == "1"
    assert response[1].created_at == "2021-01-01"
    assert response[1].updated_at == "2021-01-01"