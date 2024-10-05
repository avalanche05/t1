from fastapi import APIRouter

from app.schemas import ResumeProcess, ResumeProcessResponse


router = APIRouter()

@router.post("/resume/process")
async def process_resume(resume_process: ResumeProcess) -> ResumeProcessResponse:
    file_key = resume_process.file_key

    print(file_key)

    return ResumeProcessResponse()