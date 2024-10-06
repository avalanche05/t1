import os
import requests
from typing import List

from fastapi import APIRouter, HTTPException
from starlette import status

from app import models, schemas, serializers
from app.api.deps import SessionDep
from app.crud import candidate

router = APIRouter()


@router.get("")
async def get_candidates(
    session: SessionDep,
    position: str | None = None,
    grade: str | None = None,
    speciality: str | None = None,
    isCold: bool | None = None,
    city: str | None = None,
    work_format: str | None = None,
) -> List[schemas.Candidate]:

    db_candidates = candidate.get_all(
        session=session,
        position=position,
        grade=grade,
        speciality=speciality,
        isCold=isCold,
        city=city,
        work_format=work_format,
    )
    return serializers.get_candidates(db_candidates)


@router.get("/rank")
async def get_ranked_candidates(
        session: SessionDep,
        candidate_vacancy: schemas.CandidateVacancy
):
    response = requests.post(
        f"{os.environ.get('ML_RESUME_HOST', 'http://localhost')}:5000/resume/process",
        json={
            candidate_vacancy.dict()
        },
    )
    if response.status_code != status.HTTP_200_OK:
        raise HTTPException(status_code=404, detail=response.text)

    db_candidates = response.json()
    return serializers.get_candidates(db_candidates)
