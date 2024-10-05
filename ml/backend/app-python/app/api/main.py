from fastapi import APIRouter

from app.schemas import ResumeProcess, ResumeProcessResponse, Candidate
from app.api.deps import S3ClientDep
from app.utils.resume_structure import main as file_to_json
from app.utils.s3 import get_file as s3_get_file

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