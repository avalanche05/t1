from sqlalchemy.orm import Session
from sqlalchemy import or_, not_

from app import schemas
from app.models import Application, Candidate, Vacancy


def create(session: Session, vacancy: schemas.VacancyCreate) -> Vacancy:
    db_vacancy = Vacancy(
        position=vacancy.position,
        grade=vacancy.grade,
        speciality=vacancy.speciality,
        description=vacancy.description,
        team=vacancy.team,
    )

    session.add(db_vacancy)
    session.commit()
    session.refresh(db_vacancy)

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
    query = (
        session.query(Candidate)
        .filter(
            or_(
                Candidate.is_cold == True,
                not_(Candidate.applications.any(Application.vacancy_id == vacancy_id))
            )
        )
    )
    return query.all()
