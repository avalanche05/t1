from collections.abc import Generator
from typing import Annotated

from botocore.client import BaseClient
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBearer
from sqlalchemy.orm import Session

from app import crud
from app.core.db import engine
from app.core.s3 import s3_session
from app.models import User

# from app.main import app

storage = {}


def get_db() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


def get_s3() -> Generator[Session, None, None]:
    s3_client = s3_session.client(
        service_name="s3", endpoint_url="https://storage.yandexcloud.net"
    )
    yield s3_client


def get_storage() -> Generator[Session, None, None]:
    yield storage


SessionDep = Annotated[Session, Depends(get_db)]
S3ClientDep = Annotated[BaseClient, Depends(get_s3)]
TokenDep = Depends(HTTPBearer())
StorageDep = Annotated[dict, Depends(get_storage)]


def get_current_user(session: SessionDep, token: TokenDep) -> User:
    user = crud.get_user_by_token(session, token.credentials)
    # user = crud.get_user_by_token(session, token)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


CurrentUser = Annotated[User, Depends(get_current_user)]
