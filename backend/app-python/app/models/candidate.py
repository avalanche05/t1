from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.common import BaseEntity


class Candidate(BaseEntity):
    __tablename__ = "candidates"
    name: Mapped[str] = mapped_column()
    phone: Mapped[str] = mapped_column()
    email: Mapped[str] = mapped_column()
    contacts: Mapped[str] = mapped_column()
    skills: Mapped[str] = mapped_column()
    experience: Mapped[float] = mapped_column()
    position: Mapped[str] = mapped_column()
    grade: Mapped[str] = mapped_column()
    speciality: Mapped[str] = mapped_column()
    education: Mapped[str] = mapped_column()
    summary: Mapped[str] = mapped_column()
    is_cold: Mapped[bool] = mapped_column()
    resume_link: Mapped[str] = mapped_column()

    applications: Mapped[list["Application"]] = relationship(back_populates="candidate")
