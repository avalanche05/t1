from typing import List

from fastapi import APIRouter

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
