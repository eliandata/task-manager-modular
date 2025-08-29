import os, httpx
from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from shared.config import get_settings
from shared.logging import setup_logger

settings = get_settings()
logger = setup_logger('gateway')

app = FastAPI(title='Gateway', version='1.0.0')

USERS_URL = os.getenv('USERS_SERVICE_URL', settings.users_service_url).rstrip('/')
TASKS_URL = os.getenv('TASKS_SERVICE_URL', settings.tasks_service_url).rstrip('/')

@app.get('/health')
def health():
    return {'status':'ok','service':'gateway'}

@app.post('/v1/users')
async def create_user(request: Request):
    payload = await request.json()
    async with httpx.AsyncClient() as client:
        r = await client.post(f'{USERS_URL}/v1/users', json=payload, timeout=10)
    if r.status_code >= 400:
        raise HTTPException(status_code=r.status_code, detail=r.json())
    return JSONResponse(status_code=201, content=r.json())

@app.get('/v1/users')
async def list_users():
    async with httpx.AsyncClient() as client:
        r = await client.get(f'{USERS_URL}/v1/users', timeout=10)
    return r.json()

@app.post('/v1/tasks')
async def create_task(request: Request):
    payload = await request.json()
    async with httpx.AsyncClient() as client:
        r = await client.post(f'{TASKS_URL}/v1/tasks', json=payload, timeout=10)
    if r.status_code >= 400:
        raise HTTPException(status_code=r.status_code, detail=r.json())
    return JSONResponse(status_code=201, content=r.json())

@app.get('/v1/tasks')
async def list_tasks(status: str | None = None, assignee_id: str | None = None):
    params = {}
    if status: params['status'] = status
    if assignee_id: params['assignee_id'] = assignee_id
    async with httpx.AsyncClient() as client:
        r = await client.get(f'{TASKS_URL}/v1/tasks', params=params, timeout=10)
    return r.json()

@app.patch('/v1/tasks/{task_id}')
async def update_task(task_id: str, request: Request):
    payload = await request.json()
    async with httpx.AsyncClient() as client:
        r = await client.patch(f'{TASKS_URL}/v1/tasks/{task_id}', json=payload, timeout=10)
    if r.status_code >= 400:
        raise HTTPException(status_code=r.status_code, detail=r.json())
    return r.json()
