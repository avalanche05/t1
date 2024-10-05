from app import models, schemas
from app.serializers import candidate, vacancy

def get_application(db_application: models.Application) -> schemas.Application:
    return schemas.Application(
        vacancy=vacancy.get_vacancy(db_application.vacancy),
        candidate=candidate.get_candidate(db_application.candidate),
        status=db_application.status,
        createdAt=db_application.createdAt,
    )


def get_applications(db_applications: list[models.Application]) -> list[schemas.Application]:
    return [get_application(db_application) for db_application in db_applications]