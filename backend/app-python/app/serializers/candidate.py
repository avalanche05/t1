from app import models, schemas


def get_candidate(db_candidate: models.Candidate) -> schemas.Candidate:
    return schemas.Candidate(
        name=db_candidate.name,
        phone=db_candidate.phone,
        email=db_candidate.email,
        contacts=db_candidate.contacts,
        skills=db_candidate.skills,
        experience=db_candidate.experience,
        position=schemas.Position(db_candidate.position),
        grade=db_candidate.grade,
        speciality=db_candidate.speciality,
        education=db_candidate.education,
        summary=db_candidate.summary,
        is_cold=db_candidate.is_cold,
        resume_link=db_candidate.resume_link,
    )


def get_candidates(db_candidates) -> list[schemas.Candidate]:
    return [get_candidate(db_candidate) for db_candidate in db_candidates]
