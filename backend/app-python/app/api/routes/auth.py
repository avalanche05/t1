from fastapi import APIRouter
from app.api.deps import SessionDep
from app.schemas import Login, LoginResponse
from app.crud import auth

router = APIRouter()
@router.post("/login/")
async def login(login: Login, session: SessionDep) -> LoginResponse:
    db_user = auth.login(
        session=session,
        username=login.username,
        password=login.password,
    )

    db_token = auth.create_token(session=session, user_id=db_user.id)
    return LoginResponse(
        token=db_token.token,
        roles=[db_user.role],
    )
    
