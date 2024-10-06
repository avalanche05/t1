from pydantic import BaseModel
from typing import Literal
from datetime import datetime

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
    city: str
    work_format: str

class ResumeProcessResponse(BaseModel):
    candidate: Candidate

class Folder(BaseModel):
    id: int
    name: str
    candidates_count: int

class CandidateFeedback(BaseModel):
    name: str
    position: str
    summary: str

class Vacancy(BaseModel):
    position: str
    description: str

class FeedbackRequest(BaseModel):
    action: Literal["invite", "reject", "approve"]
    candidate: CandidateFeedback
    vacancy: Vacancy
    status: str

class Feedback(BaseModel):
    message: str