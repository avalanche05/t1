from app.api.deps import get_db
from app.models import User
from app.common import BaseEntity
from app.core.db import engine

BaseEntity.metadata.create_all(bind=engine)
session = next(get_db())
user = User(
    name="test",
    hashed_password="test",
)

session.add(user)
session.commit()