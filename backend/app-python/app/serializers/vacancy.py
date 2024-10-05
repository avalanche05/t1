from app import models, schemas

def get_vacancy(db_vacancy: models.Vacancy) -> schemas.Vacancy:
    return schemas.Vacancy(
        position=db_vacancy.position,
        grade=db_vacancy.grade,
        speciality=db_vacancy.speciality,
        description=db_vacancy.description,
        team=db_vacancy.team,
        created_at=db_vacancy.created_at,

    )

def get_vacancies(db_vacancies: list[models.Vacancy]) -> list[schemas.Vacancy]:
    return [get_vacancy(db_vacancy) for db_vacancy in db_vacancies]