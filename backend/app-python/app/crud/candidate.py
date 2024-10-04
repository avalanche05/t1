from sqlalchemy.orm import Session

from app.models import Candidate


def get_all(
    session: Session,
    position: str | None = None,
    grade: str | None = None,
    speciality: str | None = None,
    isCold: bool | None = None,
) -> list[Candidate]:
    query = session.query(Candidate)

    if position is not None:
        query = query.filter(Candidate.position == position)
    if grade is not None:
        query = query.filter(Candidate.grade == grade)
    if speciality is not None:
        query = query.filter(Candidate.speciality == speciality)
    if isCold is not None:
        query = query.filter(Candidate.isCold == isCold)

    return query.all()
