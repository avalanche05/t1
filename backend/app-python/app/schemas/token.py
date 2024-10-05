from app.common import BaseSchema


class TokenCreate(BaseSchema):
    username: str
    password: str
