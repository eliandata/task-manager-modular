# gateway/Dockerfile
FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# 1) Dependencies
# (this requirements.txt is located at gateway/requirements.txt)
COPY gateway/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 2) Shared and service code
COPY shared ./shared
COPY gateway/ .

# 3) Port and command
EXPOSE 8080
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]


