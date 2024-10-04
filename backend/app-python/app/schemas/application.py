from app.common import BaseSchema


class ApplicationCreate(BaseSchema):
    candidate_id: int
    vacancy_id: int
