from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from app.common import BaseEntity

class Token(BaseEntity):
    __tablename__ = "tokens"
    access_token: Mapped[str] = mapped_column()
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))

    user: Mapped['User'] = relationship(back_populates='tokens')