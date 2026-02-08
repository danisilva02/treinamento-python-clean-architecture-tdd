"""Module providing a function to check the health of the API."""
from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()
class HealthResponse(BaseModel):
    status: str

@router.get("")
def health() -> HealthResponse:
    """Function to check the health of the API."""
    return HealthResponse(status="ok")

