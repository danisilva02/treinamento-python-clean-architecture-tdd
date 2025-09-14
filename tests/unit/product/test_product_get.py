from unittest.mock import create_autospec

# Core
from src.core.domain_error import DomainError

# Domain
from src.domain.product.usecase_get import UsecaseProductGet
from src.domain.product.entity import ProductEntity
from src.domain.product.dto import ProductGetInputDTO

# Repository
from src.domain.product.contracts.repository import ProductRepositoryContract
        
def make_sut():
    product_repository_stub = create_autospec(ProductRepositoryContract, instance=True)
    product_repository_stub.get.return_value = (None, ProductEntity(
        id="1234567890",
        name="Product 1",
        description="Product 1 description",
        price=100,
        status="active",
        category_id="1",
        user_id="1",
        created_at="2021-01-01",
        updated_at="2021-01-01"
    ))
    return UsecaseProductGet(product_repository=product_repository_stub)


def test_product_not_id():
    sut = make_sut()
    error, response = sut.perform(product=ProductGetInputDTO(id=None))
    
    assert response is None
    assert error is not None
    assert error.message == "Id is required"
    assert isinstance(error, DomainError)
    

def test_product_exception_repository():
    sut = make_sut()
    sut.product_repository.get.side_effect = Exception("Error product get")
    error, response = sut.perform(product=ProductGetInputDTO(id="1234567890"))
    
    assert response is None
    assert error is not None
    assert error.message == "Error product get"
    assert isinstance(error, DomainError)
    

def test_product_success():
    sut = make_sut()
    error, response = sut.perform(product=ProductGetInputDTO(id="1234567890"))
    
    assert error is None
    assert response is not None
    assert response.id == "1234567890"
    assert response.name == "Product 1"
    assert response.description == "Product 1 description"
    assert response.price == 100
    assert response.status == "active"
    assert response.category_id == "1"
    assert response.user_id == "1"
    assert response.created_at == "2021-01-01"
    assert response.updated_at == "2021-01-01"