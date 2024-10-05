from app.common import BaseSchema


class Candidate(BaseSchema):
    name: str
    phone: str
    email: str
    contacts: str
    skills: str
    experience: float
    position: str
    grade: str
    speciality: str
    education: str
    summary: str
    is_cold: bool
    resume_link: str
