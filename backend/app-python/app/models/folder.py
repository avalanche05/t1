from typing import List

from sqlalchemy import Column, ForeignKey, Integer, Table
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.common import BaseEntity

FolderCandidate = Table(
    "folders_candidates",
    BaseEntity.metadata,
    Column("folder_id", Integer, ForeignKey("folders.id")),
    Column("candidate_id", Integer, ForeignKey("candidates.id")),
)


class Folder(BaseEntity):
    __tablename__ = "folders"
    name: Mapped[str] = mapped_column()

    candidates: Mapped[List["Candidate"]] = relationship(
        secondary=FolderCandidate, back_populates="folders"
    )
