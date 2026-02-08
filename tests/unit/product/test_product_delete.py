from unittest.mock import create_autospec
from src.domain.product.contracts.repository import ProductRepositoryContract
from src.domain.product.usecase_delete import UsecaseProductDelete

def make_sut():
    product_repository_stub = create_autospec(ProductRepositoryContract, instance=True)
    product_repository_stub.delete.return_value = (None, True)
        
    return UsecaseProductDelete(product_repository=product_repository_stub)
    
def test_product_delete_not_id():
    sut = make_sut()
    error, response = sut.perform(id=None)
    assert error.message == "Id is required"
    assert response is None
    
def test_product_delete_exception():
    sut = make_sut()
    sut.product_repository.delete.side_effect = Exception("Error product delete")
    error, response = sut.perform(id="123456abcd")
    assert error.message == "Error product delete"
    assert response is None
    
def test_product_delete_success():
    sut = make_sut()
    error, response = sut.perform(id="123456abcd")
    assert error is None
    assert response is True