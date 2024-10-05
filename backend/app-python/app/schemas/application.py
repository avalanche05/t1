from datetime import datetime

from app.common import BaseSchema
from app.schemas.candidate import Candidate
from app.schemas.vacancy import Vacancy


class ApplicationCreate(BaseSchema):
    candidate_id: int
    vacancy_id: int


class ApplicationStatusUpdate(BaseSchema):
    status: str


class Application(BaseSchema):
    id: int
    vacancy: Vacancy
    candidate: Candidate
    status: str
    created_at: datetime
