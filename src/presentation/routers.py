import os
from fastapi import APIRouter, HTTPException, Depends, Security
from fastapi.security import APIKeyHeader

api_key_header = APIKeyHeader(name="Authorization", auto_error=False)

def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header != os.getenv("API_KEY"):
        raise HTTPException(status_code=401, detail="Invalid API Key")
    return api_key_header

# User
from src.presentation.controller.user import controller_create_user
from src.presentation.controller.user import controller_login_user
from src.presentation.controller.user import controller_me_user
from src.presentation.controller.user import controller_update_user

# Category
from src.presentation.controller.category import controller_create_category
from src.presentation.controller.category import controller_list_category
from src.presentation.controller.category import controller_update_category
from src.presentation.controller.category import controller_get_category

# Product
from src.presentation.controller.product import controller_create_product
from src.presentation.controller.product import controller_update_product
from src.presentation.controller.product import controller_list_product
from src.presentation.controller.product import controller_get_product
from src.presentation.contract.user import (
    PresentationUserCreateRequestDTO,
    PresentationUserLoginRequestDTO,
    PresentationUserMeRequestDTO,
    PresentationUserUpdateRequestDTO,
)
from src.presentation.contract.category import PresentationCategoryCreateRequestDTO, PresentationCategoryGetRequestDTO, PresentationCategoryUpdateRequestDTO
from src.presentation.contract.product import PresentationProductCreateRequestDTO, PresentationProductUpdateRequestDTO, PresentationProductListRequestDTO, PresentationProductGetRequestDTO

# Driver
from src.infra.driver.driver import Driver

router = APIRouter()
driver = Driver()

@router.post("", tags=["User"], status_code=201)
def create_user(user: PresentationUserCreateRequestDTO):
    create_user_error, create_user_response = controller_create_user(driver=driver, user=user)
    if create_user_error:
        raise HTTPException(status_code=400, detail=create_user_error.message)
    return create_user_response


@router.put("/{user_id}", tags=["User"])
def update_user(user_id: str, update_user: PresentationUserUpdateRequestDTO):
    update_user_error, update_user_response = controller_update_user(driver=driver, user=update_user, user_id=user_id)
    if update_user_error:
        raise HTTPException(status_code=400, detail=update_user_error.message)
    return update_user_response


@router.get("/{user_id}", tags=["User"])
def me(user_id: str, api_key: str = Depends(api_key_header)):
    me_user_error, me_user_response = controller_me_user(driver=driver, me_user=PresentationUserMeRequestDTO(user_id=user_id))
    
    if me_user_error:
        raise HTTPException(status_code=400, detail=me_user_error.message)
    
    return me_user_response


@router.post("/login", tags=["Login"])
def login_user(login_user: PresentationUserLoginRequestDTO):
    login_user_error, login_user_response = controller_login_user(driver=driver, login_user=login_user)
    
    if login_user_error:
        raise HTTPException(status_code=401, detail=login_user_error.message)
    
    return login_user_response


@router.post("/{user_id}/category", tags=["Category"])
def create_category(category: PresentationCategoryCreateRequestDTO, user_id: str):
    create_category_error, create_category_response = controller_create_category(driver=driver, category=category, user_id=user_id)
    
    if create_category_error:
        raise HTTPException(status_code=400, detail=create_category_error.message)

    return create_category_response


@router.get("/{user_id}/category", tags=["Category"])
def list_category(user_id: str):
    list_category_error, list_category_response = controller_list_category(driver=driver, user_id=user_id)
    
    if list_category_error:
        raise HTTPException(status_code=400, detail=list_category_error.message)

    return list_category_response


@router.get("/{user_id}/category/{id}", tags=["Category"])
def get_category(user_id: str, id: str):
    get_category_error, get_category_response = controller_get_category(driver=driver, category=PresentationCategoryGetRequestDTO(id=id))
    
    if get_category_error:
        raise HTTPException(status_code=400, detail=get_category_error.message)

    return get_category_response


@router.put("/{user_id}/category/{id}", tags=["Category"])
def update_category(category: PresentationCategoryUpdateRequestDTO, id: str, user_id: str):
    update_category_error, update_category_response = controller_update_category(driver=driver, category=category, id=id)
    
    if update_category_error:
        raise HTTPException(status_code=400, detail=update_category_error.message)

    return update_category_response


@router.post("/{user_id}/product", tags=["Product"])
def create_product(product: PresentationProductCreateRequestDTO, user_id: str):
    create_product_error, create_product_response = controller_create_product(driver=driver, product=product, user_id=user_id)
    
    if create_product_error:
        raise HTTPException(status_code=400, detail=create_product_error.message)

    return create_product_response


@router.get("/{user_id}/product", tags=["Product"])
def list_product(user_id: str):
    list_product_error, list_product_response = controller_list_product(driver=driver, product=PresentationProductListRequestDTO(user_id=user_id))
    
    if list_product_error:
        raise HTTPException(status_code=400, detail=list_product_error.message)

    return list_product_response


@router.get("/{user_id}/product/{id}", tags=["Product"])
def get_product(user_id: str, id: str):
    get_product_error, get_product_response = controller_get_product(driver=driver, product=PresentationProductGetRequestDTO(id=id))
    
    if get_product_error:
        raise HTTPException(status_code=400, detail=get_product_error.message)

    return get_product_response


@router.put("/{user_id}/product/{id}", tags=["Product"])
def update_product(product: PresentationProductUpdateRequestDTO, id: str, user_id: str):
    update_product_error, update_product_response = controller_update_product(driver=driver, product=product, id=id, user_id=user_id)
    
    if update_product_error:
        raise HTTPException(status_code=400, detail=update_product_error.message)

    return update_product_response
