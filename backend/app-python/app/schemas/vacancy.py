from app.common import BaseSchema


class VacancyCreate(BaseSchema):
    position: str
    grade: str
    speciality: str
    description: str
    team: str
