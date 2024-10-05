from fastapi import APIRouter, Body, Path
from starlette import status

from app import schemas, serializers
from app.api.deps import SessionDep
from app.crud import vacancy

router = APIRouter()


@router.get("", status_code=status.HTTP_200_OK, response_model=list[schemas.Vacancy])
async def get_vacancies(
    session: SessionDep,
    position: str | None = None,
    grade: str | None = None,
    speciality: str | None = None,
    city: str | None = None,
    work_format: str | None = None,
):
    db_vacancies = vacancy.get_all(
        session=session,
        position=position,
        grade=grade,
        speciality=speciality,
        city=city,
        work_format=work_format,
    )

    return serializers.get_vacancies(db_vacancies)


@router.post("", status_code=status.HTTP_201_CREATED, response_model=schemas.Vacancy)
async def create_vacancy(
    session: SessionDep, vacancy_instance: schemas.VacancyCreate = Body(...)
):
    db_vacancy = vacancy.create(session=session, vacancy=vacancy_instance)

    return serializers.get_vacancy(db_vacancy)


@router.get(
    "/vacancies/{vacancy_id}/cold-candidates",
    status_code=status.HTTP_200_OK,
    response_model=list[schemas.Candidate],
)
async def get_cold_candidates_by_vacancy_id(
    session: SessionDep, vacancy_id: int = Path(...)
):
    db_cold_candidates = vacancy.get_vacancy_cold_candidates(
        session=session, vacancy_id=vacancy_id
    )

    return serializers.get_candidates(db_cold_candidates)
