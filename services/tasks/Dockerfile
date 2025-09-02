# services/tasks/Dockerfile
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# 1) Dependencies
# (this requirements.txt is located at services/tasks/requirements.txt)
COPY services/tasks/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 2) Shared and service code
COPY shared ./shared
COPY services/tasks/ .

# 3) Port and command
EXPOSE 8002
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8002"]

