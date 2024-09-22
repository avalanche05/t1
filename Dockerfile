FROM python:3.12.6-bookworm


RUN pip install -r requirements.txt

COPY ./app/ /app/app

CMD ["fastapi", "run", "--workers", "--host", "0.0.0.0", "--port", "8000", "4", "app/main.py"]
