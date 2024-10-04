from datetime import datetime
from functools import lru_cache

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy import create_engine
from sqlalchemy import select

from pydantic import BaseModel

class BaseSchema(BaseModel):
    pass

class BaseEntity(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)
    created_at: Mapped[datetime] = mapped_column(default=datetime.now( ))
    updated_at: Mapped[datetime] = mapped_column(default=datetime.now())