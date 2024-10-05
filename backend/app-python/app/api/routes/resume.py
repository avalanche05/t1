from fastapi import APIRouter

from app.api.deps import SessionDep
from app.crud import auth
from app.schemas import Login, LoginResponse
from app.serializers.user import get_user

router = APIRouter()


@router.post("/")
async def upload_resume() -> list[str]:
    pass
