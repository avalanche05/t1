from datetime import datetime

from app.common import BaseSchema


class VacancyCreate(BaseSchema):
    position: str
    grade: str
    speciality: str
    description: str
    team: str


class Vacancy(VacancyCreate):
    created_at: datetime
