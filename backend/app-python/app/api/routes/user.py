from typing import List

from fastapi import APIRouter, Body, HTTPException, Depends

from app.api.deps import SessionDep, get_current_user
from app.crud import auth, user
from app import schemas, serializers, models

router = APIRouter()


@router.post("/login")
async def login(login: schemas.Login, session: SessionDep) -> schemas.LoginResponse:
    db_user = auth.login(
        session=session,
        username=login.username,
        password=login.password,
    )

    db_token = auth.create_token(session=session, user_id=db_user.id)
    return schemas.LoginResponse(
        token=db_token.token,
        user=serializers.get_user(db_user),
    )


@router.post("/register")
def register_user(
    session: SessionDep,
    user_instance: schemas.UserCreateRequest = Body(...),
) -> schemas.Token:
    try:
        db_user = user.create(
            session=session,
            user=user_instance)
    except ValueError as e:
        raise HTTPException(status_code=409, detail=str(e))
    db_token = auth.create_token(
        session=session,
        user_id=db_user.id)

    return serializers.get_token(db_token)
