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

def create(session: Session, candidate: dict, resume_link: str, is_cold: bool = True) -> Candidate:
     db_candidate = Candidate(
                    name=candidate["name"],
                    phone=candidate["phone"],
                    email=candidate["email"],
                    contacts=candidate["contacts"],
                    skills=candidate["skills"],
                    experience=candidate["experience"],
                    position=candidate["position"],
                    grade=candidate["grade"],
                    speciality=candidate["speciality"],
                    education=candidate["education"],
                    summary=candidate["summary"],
                    is_cold=is_cold,
                    resume_link=resume_link,
                    city=candidate["city"],
                    work_format=candidate["work_format"],
                )
     session.add(db_candidate)
     session.commit()
     session.refresh(db_candidate)
     return db_candidate