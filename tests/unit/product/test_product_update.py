from unittest.mock import create_autospec
from src.core.domain_error import DomainError
from src.domain.product.entity import ProductEntity
from src.domain.product.dto import ProductUpdateInputDTO
from src.domain.product.usecase_update import UsecaseProductUpdate
from src.domain.product.contracts.repository import ProductRepositoryContract

            
def make_sut():
    product_repository_stub = create_autospec(ProductRepositoryContract, instance=True)
    product_repository_stub.get.return_value = (None, ProductEntity(
        id="123456abcd",
        name="Product 1",
        description="Product 1 description",
        price=100,
        status="active",
        category_id="1",
        user_id="1",
        created_at="2021-01-01",
        updated_at="2021-01-01"
    ))
    product_repository_stub.update.return_value = (None, ProductEntity(
        id="123456abcd",
        name="Product 1",
        description="Product 1 description",
        price=100,
        status="active",
        category_id="1",
        user_id="1",
        created_at="2021-01-01",
        updated_at="2021-01-01"
    ))
    return UsecaseProductUpdate(product_repository=product_repository_stub)


def test_product_update_not_id():
    sut = make_sut()
    error, response = sut.perform(product=ProductUpdateInputDTO(
        id=None,
        name="Product 1",
        description="Product 1 description",
        price=100,
        status="active",
        category_id="1",
        user_id="1"
    ))
    assert response is None
    assert error is not None
    assert error.message == "Id is required"
    assert isinstance(error, DomainError)
    
    
def test_product_update_not_params():
    sut = make_sut()
    error, response = sut.perform(product=ProductUpdateInputDTO(
        id="123456abcd",
        name=None,
        description=None,
        price=None,
        status=None,
        category_id=None,
        user_id=None
    ))
    assert response is None
    assert error is not None
    assert error.message == "Params is required"
    assert isinstance(error, DomainError)

    
def test_product_update_exception():
    sut = make_sut()
    sut.product_repository.update.side_effect = Exception("Error product update")
    error, response = sut.perform(product=ProductUpdateInputDTO(
        id="123456abcd",
        name="Product 1",
        description="Product 1 description",
        price=100,
        status="active",
        category_id="1",
        user_id="1"
    ))
    
    assert error.message == "Error product update"
    assert error is not None
    assert isinstance(error, DomainError)
    assert response is None

   
def test_product_update_success():
    sut = make_sut()
    error, response = sut.perform(product=ProductUpdateInputDTO(
        id="123456abcd",
        name="Product 1",
        description="Product 1 description",
        price=100,
        status="active",
        category_id="1",
        user_id="1"
    ))
    assert error is None
    assert response.id == "123456abcd"
    assert response.name == "Product 1"
    assert response.description == "Product 1 description"
    assert response.price == 100
    assert response.status == "active"
    assert response.category_id == "1"
    assert response.user_id == "1"
    assert response.created_at == "2021-01-01"
    assert response.updated_at == "2021-01-01"