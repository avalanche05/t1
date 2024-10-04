from enum import Enum

from app.common import BaseSchema


class Login(BaseSchema):
    username: str
    password: str


class Role(str, Enum):
    USER = "user"
    ADMIN = "admin"


class LoginResponse(BaseSchema):
    token: str
    roles: list[Role]
