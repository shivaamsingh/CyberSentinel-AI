FROM python:3.11-slim

WORKDIR /app

COPY requirements_docker.txt .
RUN pip install --default-timeout=1000 --no-cache-dir -r requirements_docker.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "src.api.main:app", "--host", "0.0.0.0", "--port", "8000"]