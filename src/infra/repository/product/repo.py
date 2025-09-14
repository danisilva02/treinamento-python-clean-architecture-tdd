import uuid
from src.core.domain_error import DomainError
from src.domain.product.contracts.repository import ProductRepositoryContract
from src.domain.product.entity import ProductEntity
from src.infra.driver.contract import DriverContract

class ProductRepo(ProductRepositoryContract):
    
    def __init__(self, driver: DriverContract):
        self.driver = driver
    
    def create(
        self,
        name: str,
        description: str,
        price: int,
        status: str,
        category_id: str,
        user_id: str    
    ) -> tuple[DomainError | None, ProductEntity | None]:
        try:
            sql = """
                INSERT INTO products (id, user_id, category_id, name, description, price, status)
                VALUES (:id, :user_id, :category_id, :name, :description, :price, :status)
                RETURNING
                    id AS id,
                    user_id AS user_id,
                    category_id AS category_id,
                    name AS name,
                    description AS description,
                    price AS price,
                    status AS status,
                    CAST(created_at AS VARCHAR) AS created_at,
                    CAST(updated_at AS VARCHAR) AS updated_at
            """
            args = {
                "id": str(uuid.uuid4()),
                "user_id": user_id,
                "category_id": category_id,
                "name": name,
                "description": description,
                "price": price,
                "status": status
            }

            error, success = self.driver.execute(sql, args, returning="one")

            if error:
                return DomainError(
                    message=str(error.message)
                ), None
                
            
            return None, ProductEntity(**{
                "id": success.get('id'),
                "user_id": success.get('user_id'),
                "category_id": success.get('category_id'),
                "name": success.get('name'),
                "description": success.get('description'),
                "price": success.get('price'),
                "status": success.get('status'),
                "created_at": success.get('created_at'),
                "updated_at": success.get('updated_at'),
            })
        except Exception as e:
            return DomainError(
                message=str(e)
            ), None
    
     
    def get(self, id: str) -> tuple[DomainError, ProductEntity]:
        try:
            sql = """
                SELECT
                    id AS id,
                    user_id AS user_id,
                    category_id AS category_id,
                    name AS name,
                    description AS description,
                    price AS price,
                    status AS status,
                    CAST(created_at AS VARCHAR) AS created_at,
                    CAST(updated_at AS VARCHAR) AS updated_at
                FROM products WHERE id = :id
            """
            args = {
                "id": id
            }
            
            error, success = self.driver.execute(sql, args, returning="first")
            
            if error:
                return DomainError(
                    message=str(error.message)
                ), None
                
            if not success:
                return DomainError(
                    message="Product not found"
                ), None
                
            return None, ProductEntity(**{
                "id": success.get('id'),
                "user_id": success.get('user_id'),
                "category_id": success.get('category_id'),
                "name": success.get('name'),
                "description": success.get('description'),
                "price": success.get('price'),
                "status": success.get('status'),
                "created_at": success.get('created_at'),
                "updated_at": success.get('updated_at'),
            })
        except Exception as e:
            return DomainError(
                message=str(e)
            ), None
            
    
    def update(self, product: ProductEntity) -> tuple[DomainError, ProductEntity]:
        try:
            sql = """
                UPDATE products SET name = :name, description = :description, price = :price, status = :status, category_id = :category_id, user_id = :user_id WHERE id = :id
                RETURNING
                    id AS id,
                    user_id AS user_id,
                    category_id AS category_id,
                    name AS name,
                    description AS description,
                    price AS price,
                    status AS status,
                    CAST(created_at AS VARCHAR) AS created_at,
                    CAST(updated_at AS VARCHAR) AS updated_at
            """
            args = {
                "id": product.id,
                "name": product.name,
                "description": product.description,
                "price": product.price,
                "status": product.status,
                "category_id": product.category_id,
                "user_id": product.user_id
            }
            error, success = self.driver.execute(sql, args, returning="one")
            if error:
                return DomainError(
                    message=str(error.message)
                ), None
                
            return None, ProductEntity(**{
                "id": success.get('id'),
                "user_id": success.get('user_id'),
                "category_id": success.get('category_id'),
                "name": success.get('name'),
                "description": success.get('description'),
                "price": success.get('price'),
                "status": success.get('status'),
                "created_at": success.get('created_at'),
                "updated_at": success.get('updated_at'),
            })
        except Exception as e:
            return DomainError(
                message=str(e)
            ), None
            
    
    def list(self, user_id: str) -> tuple[DomainError, list[ProductEntity]]:
        try:
            sql = """
                SELECT
                    id AS id,
                    user_id AS user_id,
                    category_id AS category_id,
                    name AS name,
                    description AS description,
                    price AS price,
                    status AS status,
                    CAST(created_at AS VARCHAR) AS created_at,
                    CAST(updated_at AS VARCHAR) AS updated_at
                FROM products WHERE user_id = :user_id
            """
            args = {
                "user_id": user_id
            }
            
            error, success = self.driver.execute(sql, args, returning="all")
            
            if error:
                return DomainError(
                    message=str(error.message)
                ), None
                
            return None, [ProductEntity(**{
                "id": product.get('id'),
                "user_id": product.get('user_id'),
                "category_id": product.get('category_id'),
                "name": product.get('name'),
                "description": product.get('description'),
                "price": product.get('price'),
                "status": product.get('status'),
                "created_at": product.get('created_at'),
                "updated_at": product.get('updated_at'),
            }) for product in success]
        except Exception as e:
            return DomainError(
                message=str(e)
            ), None