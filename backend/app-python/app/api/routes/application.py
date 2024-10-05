from starlette import status
from fastapi import APIRouter, Body, Path

from app import models, schemas, serializers
from app.api.deps import SessionDep
from app.crud import application

router = APIRouter()

@router.get(
    "",
    status_code=status.HTTP_200_OK,
    response_model=list[schemas.Application]
)
async def get_applications(
    session: SessionDep,
    position: str | None = None,
    grade: str | None = None,
    speciality: str | None = None,
    vacancy_id: int | None = None,
    status: str | None = None,
):
    db_applications = application.get_all(
        session=session,
        position=position,
        grade=grade,
        speciality=speciality,
        vacancy_id=vacancy_id,
        status=status
    )

    return serializers.get_applications(db_applications)


@router.post(
    "/",
    status_code=status.HTTP_200_OK,
    response_model=schemas.Application
)
async def create_application(
        session: SessionDep,
        application_instance: schemas.ApplicationCreate = Body(...)
):
    db_application = application.create_or_update(
        session=session,
        application=application_instance
    )

    return serializers.get_application(db_application)


@router.post(
    "/applications/{application_id}/status/",
    response_model=schemas.Application
)
async def update_application_status(
        session: SessionDep,
        application_id: int = Path(...),
        status_instance: schemas.ApplicationStatusUpdate = Body(...)
):
    db_application = application.update_status(
        session=session,
        application_id=application_id,
        status=status_instance
    )

    return serializers.get_application(db_application)
