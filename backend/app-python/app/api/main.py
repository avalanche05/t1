from fastapi import APIRouter

from app.api.routes import candidate, user

# from app.api.routes import items, login, users, utils
from app.api.routes.common import health

api_router = APIRouter()


api_router.include_router(health.router, prefix="/health", tags=["health"])
api_router.include_router(user.router, prefix="/users", tags=["user"])
api_router.include_router(candidate.router, prefix="/candidates", tags=["candidate"])
