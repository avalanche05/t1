import os
from uuid import uuid4

import requests
from fastapi import APIRouter

from app import serializers, crud
from app.api.deps import SessionDep
from app.common import BaseSchema

import requests
router = APIRouter()

class Feedback(BaseSchema):
    message: str

@router.get("/feedback/approve/vacancies/{vacancy_id}/candidates/{candidate_id}")
async def generate_approve_feedback(
    db_session: SessionDep,
    vacancy_id: int,
    candidate_id: int,
) -> Feedback:
    response = requests.post(
                f"{os.environ.get('ML_RESUME_HOST', 'http://localhost')}:5000/feedback/generate",
                json={
                    "action": "invite",
                    "vacancy": serializers.vacancy.get_vacancy(crud.vacancy.get_vacancy(db_session, vacancy_id)).dict(),
                    "candidate": serializers.candidate.get_candidate(crud.candidate.get_candidate(db_session, candidate_id)).dict(),
                },
            )
    return Feedback(message=response.json()["message"])