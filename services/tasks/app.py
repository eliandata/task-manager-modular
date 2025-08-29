from typing import Dict, List, Literal
from uuid import uuid4

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Tasks Service", version="1.0.0")


Status = Literal["todo", "in_progress", "done"]


class TaskIn(BaseModel):
    title: str
    description: str | None = None
    assignee_id: str | None = None
    status: Status = "todo"


class TaskOut(TaskIn):
    id: str = Field(default_factory=lambda: str(uuid4()))


DB: Dict[str, TaskOut] = {}


@app.get("/health")
def health():
    return {"status": "ok", "service": "tasks"}


@app.post("/v1/tasks", response_model=TaskOut, status_code=201)
def create_task(task: TaskIn):
    t = TaskOut(**task.model_dump())
    DB[t.id] = t
    return t


@app.get("/v1/tasks", response_model=List[TaskOut])
def list_tasks(status: Status | None = None, assignee_id: str | None = None):
    items = list(DB.values())
    if status:
        items = [t for t in items if t.status == status]
    if assignee_id:
        items = [t for t in items if t.assignee_id == assignee_id]
    return items


@app.patch("/v1/tasks/{task_id}", response_model=TaskOut)
def update_task(task_id: str, patch: TaskIn):
    if task_id not in DB:
        raise HTTPException(status_code=404, detail="Task not found")
    cur = DB[task_id]
    data = patch.model_dump(exclude_unset=True)
    upd = cur.model_copy(update=data)
    DB[task_id] = upd
    return upd
