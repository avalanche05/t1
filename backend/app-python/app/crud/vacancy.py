from sqlalchemy.orm import Session

from app import schemas
from app.models import Candidate, Vacancy


def create(session: Session, vacancy: schemas.VacancyCreate) -> Vacancy:
    db_vacancy = Vacancy(
        position=vacancy.position,
        grade=vacancy.grade,
        specialty=vacancy.specialty,
        description=vacancy.description,
        team=vacancy.team,
    )

    return db_vacancy


def get_all(
    session: Session,
    position: str | None = None,
    grade: str | None = None,
    speciality: str | None = None,
) -> list[Vacancy]:
    query = session.query(Vacancy)

    if position is not None:
        query = query.filter(Vacancy.position == position)
    if grade is not None:
        query = query.filter(Vacancy.grade == grade)
    if speciality is not None:
        query = query.filter(Vacancy.speciality == speciality)

    return query.all()


def get_vacancy_cold_candidates(session: Session, vacancy_id: int) -> list[Candidate]:
    return session.query(Candidate).filter(Candidate.is_cold == True).all()
