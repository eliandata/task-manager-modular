from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Dict, List
from uuid import uuid4

app = FastAPI(title='Users Service', version='1.0.0')

class UserIn(BaseModel):
    email: str
    name: str

class UserOut(UserIn):
    id: str = Field(default_factory=lambda: str(uuid4()))

DB: Dict[str, UserOut] = {}

@app.get('/health')
def health():
    return {'status': 'ok', 'service': 'users'}

@app.post('/v1/users', response_model=UserOut, status_code=201)
def create_user(user: UserIn):
    if any(u.email == user.email for u in DB.values()):
        raise HTTPException(status_code=400, detail='Email already exists')
    u = UserOut(**user.model_dump())
    DB[u.id] = u
    return u

@app.get('/v1/users', response_model=List[UserOut])
def list_users():
    return list(DB.values())
