from sqlalchemy.orm import Session
from sqlalchemy import or_, not_

from app import schemas
from app.models import User

def create(session: Session, user: schemas.User) -> User:
    db_user = session.query(User).filter(User.username == user.username).first()
    if db_user is not None:
        raise ValueError("Email already associated")

    db_user = User(
        username=user.username,
        name=user.name,
    )
    db_user.set_password(user.password)
    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user