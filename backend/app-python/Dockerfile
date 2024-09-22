FROM tiangolo/uvicorn-gunicorn-fastapi:python3.12.6

WORKDIR /app/

COPY ./requirements.txt /app/

CMD ["fastapi", "run", "--workers", "4", "app/main.py"]