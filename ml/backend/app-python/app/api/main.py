import os

from fastapi import APIRouter

from app.schemas import ResumeProcess, ResumeProcessResponse, Candidate, Vacancy, CandidateVacancy
from app.api.deps import S3ClientDep
from app.utils.resume_structure import main as file_to_json
from app.utils.s3 import get_file as s3_get_file
from app.core.ranking_resume import Rank

router = APIRouter()

@router.post("/resume/process")
async def process_resume(resume_process: ResumeProcess, s3_client: S3ClientDep) -> ResumeProcessResponse:
    file_key = resume_process.file_key

    file_bytes = s3_get_file(s3_client, file_key)

    with open(f"data/{file_key}", "wb") as f:
        f.write(file_bytes)

    data = file_to_json(f"data/{file_key}")

    return ResumeProcessResponse(
        candidate=Candidate(
            name=data["name"],
            phone=data["phone"],
            email=data["email"],
            contacts=data["contacts"],
            skills=data["skills"].split(", "),
            experience=data["experience"],
            position=data["position"],
            grade=data["grade"],
            speciality=data["speciality"],
            education=data["education"],
            summary=data["summary"],
            city="Moscow",
            work_format="online",
        )
    )

@router.post("/candidate/rank")
async def get_ranked_candidates(vacancy: Vacancy, candidates: list[Candidate]):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    weights_path = os.path.join(current_dir, "../model_weight", "resume_ranking.pt")
    rank_model = Rank(weights=weights_path)
    weights = rank_model.rank(vacancy, candidates)
    zipped_candidates = sorted(list(zip(weights, candidates)), key=lambda x: x[0], reverse=True)

    return [Candidate(
        name=candidate.name,
        phone=candidate.phone,
        email=candidate.email,
        contacts=candidate.contacts,
        skills=candidate.skills,
        experience=candidate.experience,
        position=candidate.position,
        grade=candidate.grade,
        speciality=candidate.speciality,
        education=candidate.education,
        summary=candidate.summary,
        city=candidate.city,
        work_format=candidate.work_format
    ) for _, candidate in zipped_candidates]