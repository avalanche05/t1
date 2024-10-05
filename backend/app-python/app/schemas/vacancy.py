from datetime import datetime
from typing import Literal

from app.common import BaseSchema


class VacancyCreate(BaseSchema):
    position: str
    grade: Literal["junior", "middle", "senior"]
    speciality: str
    description: str
    team: str
    city: str
    work_format: Literal["online", "hybrid", "offline"]


class Vacancy(VacancyCreate):
    id: int
    created_at: datetime
