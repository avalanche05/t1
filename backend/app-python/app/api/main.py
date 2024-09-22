from fastapi import APIRouter

# from app.api.routes import items, login, users, utils
from app.api.routes.common import health

api_router = APIRouter()

api_router.include_router(health.router, prefix="/health", tags=["health"])