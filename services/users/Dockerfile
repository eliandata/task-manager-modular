# services/users/Dockerfile
FROM python:3.11-slim

# runtime basics recommendations
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# 1) Dependencies
# (this requirements.txt is located at services/users/requirements.txt)
COPY services/users/requirements.txt ./requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# 2) Shared and service code
# (both are copied from the root of the repo thanks to the context = .)
COPY shared ./shared
COPY services/users/ .

# 3) Port and command
EXPOSE 8001
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8001"]
