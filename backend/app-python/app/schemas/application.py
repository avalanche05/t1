from datetime import datetime

from app.common import BaseSchema
from app.schemas.vacancy import Vacancy
from app.schemas.candidate import Candidate


class ApplicationCreate(BaseSchema):
    candidate_id: int
    vacancy_id: int


class Application(BaseSchema):
    vacancy: Vacancy
    candidate: Candidate
    status: str
    createdAt: datetime
