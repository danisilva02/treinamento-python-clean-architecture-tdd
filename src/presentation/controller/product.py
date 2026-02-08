# Core
from src.core.domain_error import DomainError

# Domain
from src.domain.product.usecase_create import UseCaseProductCreate, ProductCreateInputDTO
from src.domain.product.usecase_update import UsecaseProductUpdate, ProductUpdateInputDTO
from src.domain.product.usecase_list import UsecaseProductList, ProductListInputDTO
from src.domain.product.usecase_get import UsecaseProductGet, ProductGetInputDTO
from src.domain.product.usecase_delete import UsecaseProductDelete

# Infra
from src.infra.repository.product.repo import ProductRepo
from src.infra.driver.contract import DriverContract

# Presentation
from src.presentation.contract.product import (
    PresentationProductCreateRequestDTO,
    PresentationProductCreateResponseDTO,
    PresentationProductUpdateRequestDTO,
    PresentationProductUpdateResponseDTO,
    PresentationProductListRequestDTO,
    PresentationProductListResponseDTO,
    PresentationProductGetRequestDTO,
    PresentationProductGetResponseDTO,
)

def controller_create_product(
    driver: DriverContract,
    product: PresentationProductCreateRequestDTO,
    user_id: str
) -> tuple[DomainError, PresentationProductCreateResponseDTO]:
    product_repo = ProductRepo(driver=driver)
    product_create = UseCaseProductCreate(product_repository=product_repo)
    product_create_error, product_create_response = product_create.perform(
        params=ProductCreateInputDTO(
            name=product.name,
            description=product.description,
            price=product.price,
            status=product.status,
            category_id=product.category_id,
            user_id=user_id,
        )
    )
    
    if product_create_error:
        return DomainError(
            message=product_create_error.message,
            status_code=product_create_error.status_code
        ), None
    
    return None, PresentationProductCreateResponseDTO(
        id=product_create_response.id,
        name=product_create_response.name,
        description=product_create_response.description,
        price=product_create_response.price,
        status=product_create_response.status,
        category_id=product_create_response.category_id,
        user_id=product_create_response.user_id,
        created_at=product_create_response.created_at,
        updated_at=product_create_response.updated_at
    )
    
    
def controller_update_product(
    driver: DriverContract,
    product: PresentationProductUpdateRequestDTO,
    id: str,
    user_id: str
) -> tuple[DomainError, PresentationProductUpdateResponseDTO]:
    product_repo = ProductRepo(driver=driver)
    product_update = UsecaseProductUpdate(product_repository=product_repo)
    product_update_error, product_update_response = product_update.perform(
        product=ProductUpdateInputDTO(
            id=id,
            name=product.name,
            description=product.description,
            price=product.price,
            status=product.status,
            category_id=product.category_id,
            user_id=user_id
        )
    )
    
    if product_update_error:
        return DomainError(
            message=product_update_error.message,
            status_code=product_update_error.status_code
        ), None
    
    return None, PresentationProductUpdateResponseDTO(
        id=product_update_response.id,
        name=product_update_response.name,
        description=product_update_response.description,
        price=product_update_response.price,
        status=product_update_response.status,
        category_id=product_update_response.category_id,
        user_id=product_update_response.user_id,
        created_at=product_update_response.created_at,
        updated_at=product_update_response.updated_at
    )
    

def controller_list_product(
    driver: DriverContract,
    product: PresentationProductListRequestDTO
) -> tuple[DomainError, PresentationProductListResponseDTO]:
    product_repo = ProductRepo(driver=driver)
    product_list = UsecaseProductList(product_repository=product_repo)
    product_list_error, product_list_response = product_list.perform(
        product=ProductListInputDTO(
            user_id=product.user_id
        )
    )
    
    if product_list_error:
        return DomainError(
            message=product_list_error.message,
            status_code=product_list_error.status_code
        ), None
    
    return None, product_list_response


def controller_get_product(
    driver: DriverContract,
    product: PresentationProductGetRequestDTO
) -> tuple[DomainError, PresentationProductGetResponseDTO]:
    product_repo = ProductRepo(driver=driver)
    product_get = UsecaseProductGet(product_repository=product_repo)
    product_get_error, product_get_response = product_get.perform(
        product=ProductGetInputDTO(
            id=product.id
        )
    )
    
    if product_get_error:
        return DomainError(
            message=product_get_error.message,
            status_code=product_get_error.status_code
        ), None
    
    return None, PresentationProductGetResponseDTO(
        id=product_get_response.id,
        name=product_get_response.name,
        description=product_get_response.description,
        price=product_get_response.price,
        status=product_get_response.status,
        category_id=product_get_response.category_id,
        user_id=product_get_response.user_id,
        created_at=product_get_response.created_at,
        updated_at=product_get_response.updated_at
    )
    
def controller_delete_product(
    driver: DriverContract,
    id: str
) -> tuple[DomainError, bool]:
    product_repo = ProductRepo(driver=driver)
    product_delete = UsecaseProductDelete(product_repository=product_repo)
    product_delete_error, product_delete_response = product_delete.perform(
        id=id
    )
    
    if product_delete_error:
        return DomainError(
            message=product_delete_error.message,
            status_code=product_delete_error.status_code
        ), None
    
    return None, product_delete_response