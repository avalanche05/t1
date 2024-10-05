from pydantic import BaseModel

class ResumeProcess(BaseModel):
    file_key: str


class Candidate(BaseModel):
    name: str
    phone: str
    email: str
    contacts: str
    skills: list[str]
    experience: float
    position: str
    grade: str
    speciality: str
    education: str
    summary: str
    is_cold: bool
    resume_link: str
    city: str
    work_format: str

class ResumeProcessResponse(BaseModel):
    candidate: Candidate