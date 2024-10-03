from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from app.core.config import settings
from app.common import BaseEntity
engine = create_engine(str(settings.SQLALCHEMY_DATABASE_URI))

BaseEntity.metadata.create_all(bind=engine)