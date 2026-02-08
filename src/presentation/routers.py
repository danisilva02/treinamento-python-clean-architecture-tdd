from fastapi import APIRouter, HTTPException, Depends
from src.presentation.deps import get_current_user_id, get_driver
from src.infra.driver.contract import DriverContract

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
from src.presentation.controller.category import controller_delete_category

# Product
from src.presentation.controller.product import controller_create_product
from src.presentation.controller.product import controller_update_product
from src.presentation.controller.product import controller_list_product
from src.presentation.controller.product import controller_get_product
from src.presentation.controller.product import controller_delete_product

# DTO
from src.presentation.contract.user import (
    PresentationUserCreateRequestDTO,
    PresentationUserCreateResponseDTO,
    PresentationUserLoginRequestDTO,
    PresentationUserLoginResponseDTO,
    PresentationUserMeRequestDTO,
    PresentationUserMeResponseDTO,
    PresentationUserUpdateRequestDTO,
    PresentationUserUpdateResponseDTO,
)
from src.presentation.contract.category import (
    PresentationCategoryCreateRequestDTO,
    PresentationCategoryCreateResponseDTO,
    PresentationCategoryListResponseDTO,
    PresentationCategoryGetRequestDTO,
    PresentationCategoryGetResponseDTO,
    PresentationCategoryUpdateRequestDTO,
    PresentationCategoryUpdateResponseDTO,
)
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

router = APIRouter()

@router.post("/user", tags=["User"], response_model=PresentationUserCreateResponseDTO)
def create_user(
    user: PresentationUserCreateRequestDTO,
    driver: DriverContract = Depends(get_driver),
):
    create_user_error, create_user_success = controller_create_user(driver=driver, user=user)
    if create_user_error:
        raise HTTPException(
            status_code=create_user_error.status_code,
            detail=create_user_error.message
        )
    return create_user_success


@router.put("/user", tags=["User"], response_model=PresentationUserUpdateResponseDTO)
def update_user(
    update_user: PresentationUserUpdateRequestDTO,
    driver: DriverContract = Depends(get_driver),
    user_id: str = Depends(get_current_user_id),
):
    update_user_error, update_user_success = controller_update_user(
        driver=driver,
        user=update_user,
        user_id=user_id
    )
    if update_user_error:
        raise HTTPException(
            status_code=update_user_error.status_code,
            detail=update_user_error.message
        )
    return update_user_success


@router.get("/user", tags=["User"], response_model=PresentationUserMeResponseDTO)
def me(
    driver: DriverContract = Depends(get_driver),
    user_id: str = Depends(get_current_user_id)
):
    me_user_error, me_user_response = controller_me_user(
        driver=driver,
        me_user=PresentationUserMeRequestDTO(
            user_id=user_id
        )
    )
    
    if me_user_error:
        raise HTTPException(
            status_code=me_user_error.status_code,
            detail=me_user_error.message
        )
    
    return me_user_response


@router.post("/login", tags=["Login"], response_model=PresentationUserLoginResponseDTO)
def login_user(
    login_user: PresentationUserLoginRequestDTO,
    driver: DriverContract = Depends(get_driver),
):
    login_user_error, login_user_response = controller_login_user(
        driver=driver,
        login_user=login_user
    )
    
    if login_user_error:
        raise HTTPException(
            status_code=login_user_error.status_code,
            detail=login_user_error.message
        )
    
    return login_user_response


@router.post("/category", tags=["Category"], response_model=PresentationCategoryCreateResponseDTO)
def create_category(
    category: PresentationCategoryCreateRequestDTO,
    driver: DriverContract = Depends(get_driver),
    user_id: str = Depends(get_current_user_id),
):
    create_category_error, create_category_response = controller_create_category(
        driver=driver,
        category=category,
        user_id=user_id
    )
    
    if create_category_error:
        raise HTTPException(
            status_code=create_category_error.status_code,
            detail=create_category_error.message
        )

    return create_category_response


@router.get("/category", tags=["Category"], response_model=list[PresentationCategoryListResponseDTO])
def list_category(
    driver: DriverContract = Depends(get_driver),
    user_id: str = Depends(get_current_user_id),
):
    list_category_error, list_category_response = controller_list_category(
        driver=driver,
        user_id=user_id
    )
    
    if list_category_error:
        raise HTTPException(
            status_code=list_category_error.status_code,
            detail=list_category_error.message
        )

    return list_category_response


@router.get("/category/{id}", tags=["Category"], response_model=PresentationCategoryGetResponseDTO)
def get_category(
    id: str,
    driver: DriverContract = Depends(get_driver),
    user_id: str = Depends(get_current_user_id),
):
    get_category_error, get_category_response = controller_get_category(
        driver=driver,
        category=PresentationCategoryGetRequestDTO(id=id)
    )
    
    if get_category_error:
        raise HTTPException(
            status_code=get_category_error.status_code,
            detail=get_category_error.message
        )

    return get_category_response


@router.put("/category/{id}", tags=["Category"], response_model=PresentationCategoryUpdateResponseDTO)
def update_category(
    category: PresentationCategoryUpdateRequestDTO,
    id: str,
    driver: DriverContract = Depends(get_driver),
    user_id: str = Depends(get_current_user_id),
):
    update_category_error, update_category_response = controller_update_category(
        driver=driver,
        category=category,
        id=id
    )
    
    if update_category_error:
        raise HTTPException(
            status_code=update_category_error.status_code,
            detail=update_category_error.message
        )

    return update_category_response

@router.delete("/category/{id}", tags=["Category"], response_model=bool)
def delete_category(
    id: str,
    driver: DriverContract = Depends(get_driver),
    user_id: str = Depends(get_current_user_id),
):
    delete_category_error, delete_category_response = controller_delete_category(
        driver=driver,
        id=id
    )
    
    if delete_category_error:
        raise HTTPException(
            status_code=delete_category_error.status_code,
            detail=delete_category_error.message
        )

    return delete_category_response


@router.post("/product", tags=["Product"], response_model=PresentationProductCreateResponseDTO)
def create_product(
    product: PresentationProductCreateRequestDTO,
    driver: DriverContract = Depends(get_driver),
    user_id: str = Depends(get_current_user_id),
):
    create_product_error, create_product_response = controller_create_product(
        driver=driver,
        product=product,
        user_id=user_id
    )
    
    if create_product_error:
        raise HTTPException(
            status_code=create_product_error.status_code,
            detail=create_product_error.message
        )

    return create_product_response


@router.get("/product", tags=["Product"], response_model=list[PresentationProductListResponseDTO])
def list_product(
    driver: DriverContract = Depends(get_driver),
    user_id: str = Depends(get_current_user_id),
):
    list_product_error, list_product_response = controller_list_product(
        driver=driver,
        product=PresentationProductListRequestDTO(user_id=user_id)
    )
    
    if list_product_error:
        raise HTTPException(
            status_code=list_product_error.status_code,
            detail=list_product_error.message
        )

    return list_product_response


@router.get("/product/{id}", tags=["Product"], response_model=PresentationProductGetResponseDTO)
def get_product(
    id: str,
    driver: DriverContract = Depends(get_driver),
    user_id: str = Depends(get_current_user_id),
):
    get_product_error, get_product_response = controller_get_product(
        driver=driver,
        product=PresentationProductGetRequestDTO(id=id),
    )
    
    if get_product_error:
        raise HTTPException(
            status_code=get_product_error.status_code,
            detail=get_product_error.message
        )

    return get_product_response


@router.put("/product/{id}", tags=["Product"], response_model=PresentationProductUpdateResponseDTO)
def update_product(
    product: PresentationProductUpdateRequestDTO,
    id: str,
    driver: DriverContract = Depends(get_driver),
    user_id: str = Depends(get_current_user_id),
):
    update_product_error, update_product_response = controller_update_product(
        driver=driver,
        product=product,
        id=id,
        user_id=user_id
    )
    
    if update_product_error:
        raise HTTPException(
            status_code=update_product_error.status_code,
            detail=update_product_error.message
        )

    return update_product_response


@router.delete("/product/{id}", tags=["Product"], response_model=bool)
def delete_product(
    id: str,
    driver: DriverContract = Depends(get_driver),
    user_id: str = Depends(get_current_user_id),
):
    delete_product_error, delete_product_response = controller_delete_product(
        driver=driver,
        id=id
    )
    
    if delete_product_error:
        raise HTTPException(
            status_code=delete_product_error.status_code,
            detail=delete_product_error.message
        )

    return delete_product_response