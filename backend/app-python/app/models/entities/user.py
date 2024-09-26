from app.models.common import BaseEntity

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from typing import List

class User(BaseEntity):
    __tablename__ = "users"
    name: Mapped[str] = mapped_column()
    item_id: Mapped[int] = mapped_column()