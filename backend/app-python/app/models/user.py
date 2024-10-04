from app.common import BaseEntity

from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from typing import List

class User(BaseEntity):
    __tablename__ = "users"
    name: Mapped[str] = mapped_column()
    hashed_password: Mapped[str] = mapped_column()
    role: Mapped[str] = mapped_column(), 

    tokens: Mapped[list['Token']] = relationship(
        cascade='all,delete-orphan',
        back_populates='user'
    )

    def set_password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)