import uuid
from src.core.domain_error import DomainError
from src.domain.category.contracts.repository import CategoryRepositoryContract
from src.domain.category.entity import CategoryEntity
from src.infra.driver.contract import DriverContract

class CategoryRepo(CategoryRepositoryContract):
    
    def __init__(self, driver: DriverContract):
        self.driver = driver
    
    
    def create(self, user_id: str, name: str, status: str) -> tuple[DomainError, CategoryEntity]:
        try:
            sql = """
                INSERT INTO categories (id, user_id, name, status)
                VALUES (:id, :user_id, :name, :status)
                RETURNING
                    id AS id,
                    user_id AS user_id,
                    name AS name,
                    status AS status,
                    CAST(created_at AS VARCHAR) AS created_at,
                    CAST(updated_at AS VARCHAR) AS updated_at
            """
            args = {
                "id": str(uuid.uuid4()),
                "user_id": user_id,
                "name": name,
                "status": status
            }
            
            error, success = self.driver.execute(sql, args, returning="one")
            
            if error:
                return DomainError(
                    message=str(error.message)
                ), None
                
            return None, CategoryEntity(**{
                "id": success.get('id'),
                "user_id": success.get('user_id'),
                "name": success.get('name'),
                "status": success.get('status'),
                "created_at": str(success.get('created_at')),
                "updated_at": str(success.get('updated_at')),
            })
        except Exception as e:
            return DomainError(
                message=str(e)
            ), None
            
    
    def list(self, user_id: str) -> list[DomainError | None, tuple[CategoryEntity] | None]:
        try:
            sql = """
                SELECT
                    id AS id,
                    user_id AS user_id,
                    name AS name,
                    status AS status,
                    CAST(created_at AS VARCHAR) AS created_at,
                    CAST(updated_at AS VARCHAR) AS updated_at
                FROM categories WHERE user_id = :user_id
            """
            args = {
                "user_id": user_id
            }
            
            error, success = self.driver.execute(sql, args, returning="all")
            
            if error:
                return DomainError(
                    message=str(error.message)
                ), None
                
            if not success:
                return DomainError(
                    message="Categories not found"
                ), None
            
            return None, [
                CategoryEntity(**{
                    "id": category.get('id'),
                    "user_id": category.get('user_id'),
                    "name": category.get('name'),
                    "status": category.get('status'),
                    "created_at": category.get('created_at'),
                    "updated_at": category.get('updated_at'),
                })
                for category in success
            ]
        except Exception as e:
            return DomainError(
                message=str(e)
            ), None
            
    
    def update(self, id: str, name: str, status: str) -> tuple[DomainError, CategoryEntity]:
        try:
            args = {}
            sqset = ""
            
            if name:
                args["name"] = name
                sqset += "name = :name,"
            if status:
                args["status"] = status
                sqset += "status = :status,"
                
            args["id"] = id
            sqset = sqset.rstrip(',')
            
            sql = f"""
                UPDATE categories SET {sqset} WHERE id = :id
                RETURNING
                    id AS id,
                    user_id AS user_id,
                    name AS name,
                    status AS status,
                    CAST(created_at AS VARCHAR) AS created_at,
                    CAST(updated_at AS VARCHAR) AS updated_at
            """
            
            error, success = self.driver.execute(sql, args, returning="one")
            
            if error:
                return DomainError(
                    message=str(error.message)
                ), None
                
            
            return None, CategoryEntity(**{
                "id": success.get('id'),
                "user_id": success.get('user_id'),
                "name": success.get('name'),
                "status": success.get('status'),
                "created_at": success.get('created_at'),
                "updated_at": success.get('updated_at'),
            })
        except Exception as e:
            return DomainError(
                message=str(e)
            ), None
            
    
    def get(self, id: str) -> tuple[DomainError, CategoryEntity]:
        try:
            sql = """
                SELECT
                    id AS id,
                    user_id AS user_id,
                    name AS name,
                    status AS status,
                    CAST(created_at AS VARCHAR) AS created_at,
                    CAST(updated_at AS VARCHAR) AS updated_at
                FROM categories WHERE id = :id
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
                    message="Category not found"
                ), None
                
            return None, CategoryEntity(**{
                "id": success.get('id'),
                "user_id": success.get('user_id'),
                "name": success.get('name'),
                "status": success.get('status'),
                "created_at": success.get('created_at'),
                "updated_at": success.get('updated_at'),
            })
        except Exception as e:
            return DomainError(
                message=str(e)
            ), None