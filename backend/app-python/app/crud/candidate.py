from sqlalchemy.orm import Session

from app.models import Candidate


def get_all(
    session: Session,
    position: str | None = None,
    grade: str | None = None,
    speciality: str | None = None,
    isCold: bool | None = None,
    city: str | None = None,
    work_format: str | None = None
) -> list[Candidate]:
    query = session.query(Candidate)

    if position is not None:
        query = query.filter(Candidate.position == position)
    if grade is not None:
        query = query.filter(Candidate.grade == grade)
    if speciality is not None:
        query = query.filter(Candidate.speciality == speciality)
    if isCold is not None:
        query = query.filter(Candidate.is_cold == isCold)
    if city is not None:
        query = query.filter(Candidate.city == city)
    if work_format is not None:
        query = query.filter(Candidate.work_format == work_format)

    return query.all()
