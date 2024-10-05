from enum import Enum

from app.common import BaseSchema


class Position(str, Enum):
    MANAGER = "manager"
    DEVELOPER = "developer"

class Candidate(BaseSchema):
    id: int
    name: str
    phone: str
    email: str
    contacts: str
    skills: str
    experience: float
    position: Position
    grade: str
    speciality: str
    education: str
    summary: str
    is_cold: bool
    resume_link: str
