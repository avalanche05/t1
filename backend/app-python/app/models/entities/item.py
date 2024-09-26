from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from app.models.common import BaseEntity

class Item(BaseEntity):
    __tablename__ = "items"
    title: Mapped[str] = mapped_column()