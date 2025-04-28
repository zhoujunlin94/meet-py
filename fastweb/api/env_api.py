from fastapi import APIRouter
from config.env import settings

router = APIRouter()

@router.get("/")
def get_configs():
    return {
        "database_url": settings.DATABASE_URL,
        "api_key": settings.API_KEY,
        "debug": settings.DEBUG
    }

