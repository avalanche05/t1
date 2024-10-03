from fastapi import APIRouter
from app.api.deps import SessionDep
from app.models import User

router = APIRouter()
@router.get("/check/")
async def health_check() -> bool:
    return True

@router.get("/create/")
async def create(session: SessionDep) -> bool:
    user = User(
        name="test",
        hashed_password="test",
    )

    session.add(user)
    session.commit()

    return True