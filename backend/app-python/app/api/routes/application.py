import os
import requests
import json
from datetime import datetime

from fastapi import APIRouter, Body, Path, HTTPException
from starlette import status

from app import models, schemas, serializers
from app.crud import application, vacancy
from app.api.deps import SessionDep, CHClientDep

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
    session: SessionDep, ch_client: CHClientDep, application_instance: schemas.ApplicationCreate = Body(...)
):
    db_application = application.create_or_update(
        session=session, application=application_instance
    )
    db_vacancy = db_application.db_vacancy
    db_candidate = db_application.db_candidate

    ch_client.insert('vacancy_events',
                      [[db_vacancy.id, db_vacancy.position, db_vacancy.grade, db_vacancy.city, db_vacancy.work_format, "test_username", 1, 'pending', db_candidate.id]],
                      column_names=['PgID', 'Position', 'Grade', 'City', 'WorkFormat', 'Username', 'UserID', 'Event', 'CandidateID'])


    return serializers.get_application(db_application)


@router.post(
    "/applications/{application_id}/status", response_model=schemas.Application
)
async def update_application_status(
    session: SessionDep,
    ch_client: CHClientDep,
    application_id: int = Path(...),
    status_instance: schemas.ApplicationStatusUpdate = Body(...),
):
    db_application = application.update_status(
        session=session, application_id=application_id, status=status_instance
    )

    db_vacancy = db_application.vacancy
    db_candidate = db_application.candidate

    ch_client.insert('vacancy_events',
                      [[db_vacancy.id, db_vacancy.position, db_vacancy.grade, db_vacancy.city, db_vacancy.work_format, "test_username", 1, status_instance.status, db_candidate.id]],
                      column_names=['PgID', 'Position', 'Grade', 'City', 'WorkFormat', 'Username', 'UserID', 'Event', 'CandidateID'])


    return serializers.get_application(db_application)
