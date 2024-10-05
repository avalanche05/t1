from typing import List

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.common import BaseEntity


class Vacancy(BaseEntity):
    __tablename__ = "vacancies"
    position: Mapped[str] = mapped_column()
    grade: Mapped[str] = mapped_column()
    speciality: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    team: Mapped[str] = mapped_column()
    city: Mapped[str] = mapped_column()
    work_format: Mapped[str] = mapped_column()

    applications: Mapped[List["Application"]] = relationship(back_populates="vacancy")