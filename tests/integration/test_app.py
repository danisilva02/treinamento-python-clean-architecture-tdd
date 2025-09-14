import pytest

# Create
from src.domain.user.usecase_create import UseCaseUserCreate
from src.domain.user.dto import UserCreateDTO

# Login
from src.domain.user.usecase_login import UseCaseUserLogin
from src.domain.user.dto import UserLoginDTO

# Me
from src.domain.user.usecase_me import UseCaseUserMe
from src.domain.user.dto import UserMeDTO

# Category
from src.domain.category.usecase_create import UseCaseCategoryCreate
from src.domain.category.dto import CategoryCreateInputDTO

# Product
from src.domain.product.usecase_create import UseCaseProductCreate
from src.domain.product.dto import ProductCreateInputDTO

# Repository
from src.infra.repository.user.repo import UserRepo
from src.infra.repository.category.repo import CategoryRepo
from src.infra.repository.product.repo import ProductRepo

# Security
from src.infra.security.security import Security

# Driver
from src.infra.driver.driver import Driver

driver = Driver()

email = "test.integration@gmail.com"
name = "Test:Daniel 7"
password = "@P@ssw0rd"

def clean_database(email: str = email) -> bool:
    print("Entrou no clean_database")
    driver.execute(sql="""
        DELETE FROM categories
        WHERE user_id = (SELECT id FROM users WHERE email = :email)
        """, args={"email": email}
    )
    driver.execute(sql="""
        DELETE FROM products
        WHERE user_id = (SELECT id FROM users WHERE email = :email)
        """, args={"email": email}
    )
    driver.execute(sql="DELETE FROM users WHERE email = :email", args={"email": email})
    return True

@pytest.fixture
def before_and_after_all():
    files_before = clean_database()
    yield
    # files_after = clean_database()
    assert files_before == True
    # assert files_after == True

def test_user(before_and_after_all):
    user_repo = UserRepo(driver=driver)
    security_repo = Security()
    category_repo = CategoryRepo(driver=driver)
    product_repo = ProductRepo(driver=driver)
    
    user_error, user_success = UseCaseUserCreate(user_repo=user_repo, security=security_repo).perform(UserCreateDTO(
        email=email,
        name=name,
        password=password,
    ))
    
    assert user_error is None
    assert user_success.id is not None
    assert user_success.email == email
    assert user_success.name == name
    assert user_success.created_at is not None
    assert user_success.updated_at is not None
    
    user_login_error, user_login_success = UseCaseUserLogin(user_repo=user_repo, security=security_repo).perform(UserLoginDTO(
        email=email,
        password=password,
    ))
    
    assert user_login_error is None
    assert user_login_success.token is not None
    
    user_me_error, user_me_success = UseCaseUserMe(user_repo=user_repo).perform(UserMeDTO(
        user_id=user_success.id,
    ))
    
    assert user_me_error is None
    assert user_me_success.id is not None
    assert user_me_success.email == email
    assert user_me_success.name == name
    assert user_me_success.created_at is not None
    assert user_me_success.updated_at is not None
    
    category_error, category_success = UseCaseCategoryCreate(category_repository=category_repo).perform(CategoryCreateInputDTO(
        name="Test:Category 1",
        status="active",
        user_id=user_me_success.id,
    ))
    
    assert category_error is None
    assert category_success.id is not None
    assert category_success.name == "Test:Category 1"
    assert category_success.status == "active"
    assert category_success.user_id == user_me_success.id
    assert category_success.created_at is not None
    assert category_success.updated_at is not None
    
    product_error, product_success = UseCaseProductCreate(product_repository=product_repo).perform(ProductCreateInputDTO(
        name="Test:Product 2",
        description="Test:Product 2 description",
        price=100,
        status="active",
        category_id=category_success.id,
        user_id=user_me_success.id,
    ))
    
    assert product_error is None
    assert product_success.id is not None
    assert product_success.name == "Test:Product 2"
    assert product_success.description == "Test:Product 2 description"
    assert product_success.price == 100
    assert product_success.status == "active"
    assert product_success.category_id == category_success.id
    assert product_success.user_id == user_me_success.id
    assert product_success.created_at is not None
    assert product_success.updated_at is not None