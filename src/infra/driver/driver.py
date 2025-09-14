import os
from sqlalchemy import create_engine, text
from sqlalchemy.exc import SQLAlchemyError
from src.core.domain_error import DomainError
from typing import Optional, Dict, Any
from .contract import DriverContract

JsonDict = Dict[str, Any]

DATABASE_URL = os.getenv('DATABASE_URL')
DATABASE_MIN_CONN = os.getenv('DATABASE_MIN_CONN')
DATABASE_MAX_CONN = os.getenv('DATABASE_MAX_CONN')

class Driver(DriverContract):
    def __init__(self):
        self.engine = create_engine(
            url=DATABASE_URL,
            pool_pre_ping=True,
            pool_size=10,
            max_overflow=20,
            pool_timeout=30,
            pool_recycle=1800
        )

    def execute(self, sql: str, args: Any = None, returning: str = None) -> tuple[DomainError, Optional[JsonDict]]:
        try:
            with self.engine.begin() as conn:
                res = conn.execute(text(sql), args)
                maps = res.mappings()
                
                if returning == "one":
                    return None, maps.one()
                
                if returning == "all":
                    return None, maps.all()
                
                if returning == "first":
                    return None, maps.first()
                
                conn.commit()
                conn.close()
                
                return None, {"message": "ok"} 
        except Exception as e:
            if isinstance(e, SQLAlchemyError):
                return DomainError(
                    message=f"Driver: {str(e)}"
                ), None
            
            