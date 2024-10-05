from sqlalchemy.orm import Session

from app import schemas
from app.models import Application


def create_or_update(
    session: Session, application: schemas.ApplicationCreate
) -> Application:
    db_appication = (
        session.query(Application)
        .filter(Application.candidate_id == application.candidate_id)
        .first()
    )
    if db_appication is None:
        db_appication = Application(
            candidate_id=application.candidate_id,
            vacancy_id=application.vacancy_id,
            status="pending",
        )
    else:
        db_appication.candidate_id = application.candidate_id
        db_appication.status = "pending"
    session.add(db_appication)
    session.commit()
    session.refresh(db_appication)
    return db_appication


def update_status(session: Session, application_id: int, status: str) -> Application:
    db_appication = session.query(Application).get(application_id)
    if db_appication is None:
        raise ValueError(f"Application with id: {application_id} not found")
    db_appication.status = status
    session.add(db_appication)
    session.commit()
    session.refresh(db_appication)
    return db_appication


def get_all(
    session: Session,
    position: str | None = None,
    grade: str | None = None,
    speciality: str | None = None,
    vacancy_id: int | None = None,
    status: str | None = None,
) -> list[Application]:
    query = session.query(Application).join(Application.candidate)

    if position is not None:
        query = query.filter(Application.candidate.position == position)
    if grade is not None:
        query = query.filter(Application.candidate.grade == grade)
    if speciality is not None:
        query = query.filter(Application.candidate.speciality == speciality)
    if vacancy_id is not None:
        query = query.filter(Application.vacancy_id == vacancy_id)
    if status is not None:
        query = query.filter(Application.status == status)

    return query.all()
