from app import models
from app import schemas


def get_user(db_user: models.User) -> schemas.User:
    return schemas.User(
        id=db_user.id,
        name=db_user.name,
    )