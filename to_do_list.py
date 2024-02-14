from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import datetime
import uuid

app = FastAPI()

tasks = []

class TaskCreate(BaseModel):
    title: str
    description: Optional[str] = None
    created_by: Optional[str] = None

class Task(BaseModel):
    task_id: str
    title: str
    description: Optional[str] = None
    created_date: datetime.datetime
    created_by: Optional[str] = None

@app.get("/")
async def home():
    return {"status": "success", "message": "Welcome to the Task Manager API"}

@app.get("/tasks/", response_model=List[Task])
async def get_tasks():
    return tasks

@app.get("/tasks/{task_id}", response_model=Task)
async def get_task_by_id(task_id: str):
    try:
        return next(t for t in tasks if t.task_id == task_id)
    except StopIteration:
        raise HTTPException(status_code=404, detail="Task not found")

@app.post("/tasks/", response_model=Task)
async def create_task(task_create: TaskCreate):
    task_id = str(uuid.uuid4())
    task = Task(task_id=task_id, created_date=datetime.datetime.now(), **task_create.dict())
    tasks.append(task)
    return task

@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: str, updated_task: TaskCreate):
    try:
        existing_task = next(t for t in tasks if t.task_id == task_id)
    except StopIteration:
        raise HTTPException(status_code=404, detail="Task not found")

    tasks.remove(existing_task)
    updated_task_model = Task(task_id=task_id, created_date=existing_task.created_date, **updated_task.dict())
    tasks.append(updated_task_model)
    return updated_task_model

@app.delete("/tasks/{task_id}", response_model=dict)
async def delete_task(task_id: str):
    try:
        task = next(t for t in tasks if t.task_id == task_id)
    except StopIteration:
        raise HTTPException(status_code=404, detail="Task not found")

    tasks.remove(task)
    return {"status": "success", "message": "Task deleted successfully!"}
