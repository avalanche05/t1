import os
import requests
import json
from datetime import datetime

from fastapi import APIRouter, Body, Path, HTTPException
from starlette import status

from app import models, schemas, serializers
from app.api.deps import SessionDep
from app.crud import application, vacancy

router = APIRouter()


@router.get(
    "", status_code=status.HTTP_200_OK, response_model=list[schemas.Application]
)
async def get_applications(
    session: SessionDep,
    position: str | None = None,
    grade: str | None = None,
    speciality: str | None = None,
    vacancy_id: int | None = None,
    sort_status: str | None = None,
    is_ranked: bool | None = False,
):
    db_applications = application.get_all(
        session=session,
        position=position,
        grade=grade,
        speciality=speciality,
        vacancy_id=vacancy_id,
        status=sort_status,
    )

    if vacancy_id and is_ranked:
        db_vacancy = vacancy.get_vacancy(session, vacancy_id)
        serialized_vacancy = serializers.get_vacancy(db_vacancy)
        serialized_applications = serializers.get_applications(db_applications)
        # return {
        #         "vacancy": serialized_vacancy.json(),
        #         "candidates": [serialized_application.candidate.json() for serialized_application in serialized_applications]
        #     }
        vacancy_dict = serialized_vacancy.dict()

        # Convert datetime fields to string
        if isinstance(vacancy_dict['created_at'], datetime):
            vacancy_dict['created_at'] = vacancy_dict['created_at'].isoformat()
        response = requests.post(
            f"{os.environ.get('ML_RESUME_HOST', 'http://localhost')}:5000/candidates/rank",
            json={
                "vacancy": vacancy_dict,
                "candidates": [serialized_application.candidate.dict() for serialized_application in serialized_applications]
            },
        )
        if response.status_code != status.HTTP_200_OK:
            raise HTTPException(status_code=404, detail=response.text)

        serialized_candidates = response.json()
        db_applications = [application.get_by_candidate_and_vaccancy(session, candidate["id"], vacancy_id) for candidate
                           in serialized_candidates]

    return serializers.get_applications(db_applications)


@router.post("", status_code=status.HTTP_200_OK, response_model=schemas.Application)
async def create_application(
    session: SessionDep, application_instance: schemas.ApplicationCreate = Body(...)
):
    db_application = application.create_or_update(
        session=session, application=application_instance
    )

    return serializers.get_application(db_application)


@router.post(
    "/applications/{application_id}/status", response_model=schemas.Application
)
async def update_application_status(
    session: SessionDep,
    application_id: int = Path(...),
    status_instance: schemas.ApplicationStatusUpdate = Body(...),
):
    db_application = application.update_status(
        session=session, application_id=application_id, status=status_instance
    )

    return serializers.get_application(db_application)
