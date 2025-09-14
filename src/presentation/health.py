"""Module providing a function to check the health of the API."""
from fastapi import APIRouter

router = APIRouter()

@router.get("")
def health():
    """Function to check the health of the API."""
    return {"status": "test"}

