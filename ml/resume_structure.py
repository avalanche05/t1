import json

from utils.extract_text_from_file import ReadResume
from utils.ollama_run import LlamaRun


def main(pdf_path: str):
    template = """Use the following pieces of context to expand text to fields in JSON-format: "name": string, "phone": string, "email": string, "contacts": string, "skills": string, "experience": float, "position": string, "grade": string, "speciality": string, "education":string, "summary": string, "work_format": string, "city": string.
    experience - get number how long he woked in years, if now - 2024
    summary - summarize his exeperience in two sentences
    work_format - offline or online
    answer with only JSON-format text
    Context:
    {context}

    Question: answer using language of original context"""

    reader = ReadResume(pdf_path)
    resume_text = reader.extract_text()

    model = LlamaRun(template=template,
                     ollama_url="https://useful-kite-settled.ngrok-free.app",
                     model_name="llama3.1:8b",
                     temperature=0)
    resume_structured = model.run(context=resume_text)

    data = json.loads(
        resume_structured.replace('json\n', "").replace("```", "").replace("\n", ""))
    return data