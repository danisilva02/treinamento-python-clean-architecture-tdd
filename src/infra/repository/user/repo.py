from src.core.domain_error import DomainError
from src.domain.user.contracts.repository import UserRepoContract
from src.domain.user.entity import UserEntity
from src.infra.driver.contract import DriverContract

class UserRepo(UserRepoContract):
    
    def __init__(self, driver: DriverContract):
        self.driver = driver
    
    def create(self, user: UserEntity) -> list[DomainError, UserEntity]:
        try:
            sql = """
                INSERT INTO users (id, email, name, password)
                VALUES (:id, :email, :name, :password)
                RETURNING
                    id AS id,
                    email AS email,
                    name AS name,
                    CAST(created_at AS VARCHAR) AS created_at,
                    CAST(updated_at AS VARCHAR) AS updated_at   
            """
            args = {
                "id": user.id,
                "email": user.email,
                "name": user.name,
                "password": user.password_hash
            }
            
            error, success = self.driver.execute(sql, args, returning="one")
            if error:
                return DomainError(
                    message=str(error.message)
                ), None
                
            return None, UserEntity(**{
                "id": success.get('id'),
                "email": success.get('email'),
                "name": success.get('name'),
                "created_at": success.get('created_at'),
                "updated_at": success.get('updated_at'),
            })
        except Exception as e:
            return DomainError(
                message=f"Repo: {str(e)}"
            ), None


    def update(self, user: UserEntity) -> list[DomainError, UserEntity]:
        try:
            sql = """
                UPDATE users SET name = :name, email = :email WHERE id = :id
                RETURNING
                    id AS id,
                    name AS name,
                    email AS email,
                    CAST(created_at AS VARCHAR) AS created_at,
                    CAST(updated_at AS VARCHAR) AS updated_at
            """
            args = {
                "id": user.id,
                "name": user.name,
                "email": user.email
            }
            error, success = self.driver.execute(sql, args, returning="first")
            
            if error:
                return DomainError(
                    message=str(error.message)
                ), None
                
            return None, UserEntity(**{
                "id": success.get('id'),
                "name": success.get('name'),
                "email": success.get('email'),
                "created_at": success.get('created_at'),
                "updated_at": success.get('updated_at'),
            })
        except Exception as e:
            return DomainError(
                message=str(e)
            ), None
          
            
    def login(self, email: str, password_hash: str) -> list[DomainError, UserEntity]:
        try:
            sql = f"""
                SELECT
                    id AS id
                    ,email AS email
                    ,name AS name
                    ,CAST(created_at AS VARCHAR) AS created_at
                    ,CAST(updated_at AS VARCHAR) AS updated_at
                FROM users WHERE 1=1
                AND email = :email
                AND password = :password
            """
            args = {
                "email": email,
                "password": password_hash
            }
            
            error, success = self.driver.execute(sql, args, returning="first")

            if error:
                return DomainError(
                    message=str(error.message)
                ), None
                
            return None, UserEntity(**{
                "id": success.get('id'),
                "email": success.get('email'),
                "name": success.get('name'),
                "created_at": success.get('created_at'),
                "updated_at": success.get('updated_at'),
            })
        except Exception as e:
            return DomainError(
                message=str(e)
            ), None
          
            
    def get_by_id(self, id: str) -> tuple[DomainError, UserEntity]:
        try:
            sql = f"""
                SELECT
                    id AS id
                    ,email AS email
                    ,name AS name
                    ,CAST(created_at AS VARCHAR) AS created_at
                    ,CAST(updated_at AS VARCHAR) AS updated_at
                FROM users WHERE id = :id
            """
            args = {
                "id": id
            }
            
            error, success = self.driver.execute(sql, args, returning="first")
            
            if error:
                return DomainError(
                    message=str(error.message)
                ), None

            return None, UserEntity(**{
                "id": success.get('id'),
                "email": success.get('email'),
                "name": success.get('name'),
                "created_at": success.get('created_at'),
                "updated_at": success.get('updated_at'),
            })
        except Exception as e:
            return DomainError(
                message=str(e)
            ), None