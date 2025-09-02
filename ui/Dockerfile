# ui/Dockerfile
FROM python:3.11-slim
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1
WORKDIR /app

COPY ui/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 2) Shared and service code
COPY ui/ .

EXPOSE 8501
CMD ["streamlit","run","/app/streamlit_app/app.py","--server.port=8501","--server.address=0.0.0.0"]

