# Core
from src.core.domain_error import DomainError

# Domain Create
from src.domain.category.usecase_create import UseCaseCategoryCreate
from src.domain.category.dto import CategoryCreateInputDTO

# Domain List
from src.domain.category.usecase_list import UsecaseCategoryList
from src.domain.category.dto import CategoryListInputDTO

# Domain Update
from src.domain.category.usecase_update import UsecaseCategoryUpdate
from src.domain.category.dto import CategoryUpdateInputDTO

# Domain Get
from src.domain.category.usecase_get import UsecaseCategoryGet

# Infra
from src.infra.repository.category.repo import CategoryRepo
from src.infra.driver.contract import DriverContract

# Presentation
from src.presentation.contract.category import PresentationCategoryCreateRequestDTO, PresentationCategoryCreateResponseDTO
from src.presentation.contract.category import PresentationCategoryListResponseDTO
from src.presentation.contract.category import PresentationCategoryUpdateRequestDTO, PresentationCategoryUpdateResponseDTO
from src.presentation.contract.category import PresentationCategoryGetRequestDTO, PresentationCategoryGetResponseDTO

def controller_create_category(driver: DriverContract, category: PresentationCategoryCreateRequestDTO, user_id: str) -> tuple[DomainError, PresentationCategoryCreateResponseDTO]:
    category_repo = CategoryRepo(driver=driver)
    category_create = UseCaseCategoryCreate(category_repository=category_repo)
    category_create_error, category_create_response = category_create.perform(
        params=CategoryCreateInputDTO(
            name=category.name,
            status=category.status,
            user_id=user_id,
        )
    )
    
    if category_create_error:
        return DomainError(
            message=category_create_error.message
        ), None
    
    return None, PresentationCategoryCreateResponseDTO(
        id=category_create_response.id,
        name=category_create_response.name,
        status=category_create_response.status,
        user_id=category_create_response.user_id,
        created_at=category_create_response.created_at,
        updated_at=category_create_response.updated_at
    )


def controller_get_category(driver: DriverContract, category: PresentationCategoryGetRequestDTO) -> tuple[DomainError, PresentationCategoryGetResponseDTO]:
    category_repo = CategoryRepo(driver=driver)
    category_get = UsecaseCategoryGet(category_repository=category_repo)
    category_get_error, category_get_response = category_get.perform(
        id=category.id,
    )
    
    if category_get_error:
        return DomainError(
            message=category_get_error.message
        ), None
    
    return None, PresentationCategoryGetResponseDTO(
        id=category_get_response.id,
        name=category_get_response.name,
        status=category_get_response.status,
        user_id=category_get_response.user_id,
        created_at=category_get_response.created_at,
        updated_at=category_get_response.updated_at
    )


def controller_list_category(driver: DriverContract, user_id: str) -> tuple[DomainError, list[PresentationCategoryListResponseDTO]]:
    category_repo = CategoryRepo(driver=driver)
    category_list = UsecaseCategoryList(category_repository=category_repo)
    category_list_error, category_list_response = category_list.perform(
        params=CategoryListInputDTO(
            user_id=user_id,
        )
    )
    
    if category_list_error:
        return DomainError(
            message=category_list_error.message
        ), None
    
    return None, category_list_response


def controller_update_category(driver: DriverContract, category: PresentationCategoryUpdateRequestDTO, id: str) -> tuple[DomainError, PresentationCategoryUpdateResponseDTO]:
    category_repo = CategoryRepo(driver=driver)
    category_update = UsecaseCategoryUpdate(category_repository=category_repo)
    category_update_error, category_update_response = category_update.perform(
        id=id,
        params=CategoryUpdateInputDTO(
            name=category.name,
            status=category.status,
        )
    )
    
    if category_update_error:
        return DomainError(
            message=category_update_error.message
        ), None
    
    return None, PresentationCategoryUpdateResponseDTO(
        id=category_update_response.id,
        name=category_update_response.name,
        status=category_update_response.status,
        user_id=category_update_response.user_id,
        created_at=category_update_response.created_at,
        updated_at=category_update_response.updated_at
    )