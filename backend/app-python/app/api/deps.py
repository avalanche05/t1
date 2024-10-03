from collections.abc import Generator
from typing import Annotated

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer
from pydantic import ValidationError
from sqlalchemy.orm import Session

from app.core.config import settings
from app.core.db import engine
from app.models import User


def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_db)]
TokenDep = Depends(HTTPBearer())


# def get_current_user(session: SessionDep, token: TokenDep) -> User:
#     user = crud.get_user_by_token(session, token.credentials)
#     # user = crud.get_user_by_token(session, token)
#     if not user:
#         raise HTTPException(status_code=404, detail="User not found")
#     return user


# CurrentUser = Annotated[User, Depends(get_current_user)]