FROM python:3.9-slim

WORKDIR /app

COPY main.py /app

RUN pip install --no-cache-dir fastapi uvicorn

EXPOSE 8081

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8081"]