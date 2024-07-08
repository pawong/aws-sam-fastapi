import time

from fastapi import APIRouter

router = APIRouter()


@router.get("")
def health() -> str:
    """health check endpoint"""
    return f"OK - {int(time.time())}"
