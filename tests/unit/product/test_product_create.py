from unittest.mock import create_autospec

# Contracts
from src.domain.product.contracts.repository import ProductRepositoryContract
from src.domain.product.dto import ProductCreateInputDTO

# Entity
from src.domain.product.entity import ProductEntity

# UseCase
from src.domain.product.usecase_create import UseCaseProductCreate

    
def make_sut():
    product_repository_stub = create_autospec(ProductRepositoryContract, instance=True)
    product_repository_stub.create.return_value = (None, ProductEntity(
        id="123454678oun",
        name="Product 1",
        description="Product 1 description",
        price=100,
        status="active",
        category_id="1",
        user_id="1",
        created_at="2021-01-01",
        updated_at="2021-01-01"
    ))
    return UseCaseProductCreate(product_repository=product_repository_stub)

     
def test_product_create_not_params():
    sut = make_sut()
    error, response = sut.perform(None)
    
    assert error.message == "Params is required"
    assert response is None

    
def test_product_create_not_name():
    sut = make_sut()
    error, response = sut.perform(ProductCreateInputDTO(**{
        "name": None,
        "description": "Product 1 description",
        "price": 100,
        "status": "active",
        "category_id": "1",
        "user_id": "1"
    }))
    assert response is None
    assert error.message == "Name is required"

    
def test_product_create_not_price():
    sut = make_sut()
    error, response = sut.perform(ProductCreateInputDTO(**{
        "name": "Product 1",
        "description": "Product 1 description",
        "price": None,
        "status": "active",
        "category_id": "1",
        "user_id": "1"
    }))
    assert response is None
    assert error.message == "Price is required and must be an integer"


def test_product_create_not_price_is_not_int():
    sut = make_sut()
    error, response = sut.perform(ProductCreateInputDTO(**{
        "name": "Product 1",
        "description": "Product 1 description",
        "price": "100",
        "status": "active",
        "category_id": "1",
        "user_id": "1"
    }))
    assert response is None
    assert error.message == "Price is required and must be an integer"

 
def test_product_create_not_price_is_not_positive():
    sut = make_sut()
    error, response = sut.perform(ProductCreateInputDTO(**{
        "name": "Product 1",
        "description": "Product 1 description",
        "price": 0,
        "status": "active",
        "category_id": "1",
        "user_id": "1"
    }))
    assert response is None
    assert error.message == "Price is required and must be an integer"

    
def test_product_create_not_status():
    sut = make_sut()
    error, response = sut.perform(ProductCreateInputDTO(**{
        "name": "Product 1",
        "description": "Product 1 description",
        "price": 100,
        "status": None,
        "category_id": "1",
        "user_id": "1"
    }))
    assert response is None
    assert error.message == "Status is required"

    
def test_product_create_status_is_invalid():
    sut = make_sut()
    error, response = sut.perform(ProductCreateInputDTO(**{
        "name": "Product 1",
        "description": "Product 1 description",
        "price": 100,
        "status": "invalid",
        "category_id": "1",
        "user_id": "1"
    }))
    assert response is None
    assert error.message == "Status is invalid"

    
def test_product_create_not_category_id():
    sut = make_sut()
    error, response = sut.perform(ProductCreateInputDTO(**{
        "name": "Product 1",
        "description": "Product 1 description",
        "price": 100,
        "status": "active",
        "category_id": None,
        "user_id": "1"
    }))
    assert response is None
    assert error.message == "Category id is required"

    
def test_product_create_not_user_id():
    sut = make_sut()
    error, response = sut.perform(ProductCreateInputDTO(**{
        "name": "Product 1",
        "description": "Product 1 description",
        "price": 100,
        "status": "active",
        "category_id": "1",
        "user_id": None
    }))
    assert response is None
    assert error.message == "User id is required"


def test_product_create_exception():
    sut = make_sut()
    sut.product_repository.create.side_effect = Exception("Error product create")
    error, response = sut.perform(ProductCreateInputDTO(**{
        "name": "Product 1",
        "description": "Product 1 description",
        "price": 100,
        "status": "active",
        "category_id": "1",
        "user_id": "1"
    }))
    assert error.message == "Error product create"
    assert response is None


def test_product_create_success():
    sut = make_sut()
    error, response = sut.perform(ProductCreateInputDTO(**{
        "name": "Product 1",
        "description": "Product 1 description",
        "price": 100,
        "status": "active",
        "category_id": "1",
        "user_id": "1"
    }))
    
    assert error is None
    assert response.id == "123454678oun"
    assert response.name == "Product 1"
    assert response.description == "Product 1 description"
    assert response.price == 100
    assert response.status == "active"
    assert response.category_id == "1"
    assert response.user_id == "1"
    assert response.created_at == "2021-01-01"
    assert response.updated_at == "2021-01-01"