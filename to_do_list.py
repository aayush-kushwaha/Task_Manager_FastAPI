from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from typing import Optional
import datetime

app = FastAPI()

tasks = []
task_id_counter = 1

class Task(BaseModel):
    task_id: str
    title: str
    description: Optional[str] = None
    # created_date: datetime = datetime.datetime.now()
    created_by: Optional[str] = None

@app.get("/")
async def home():
    return {"status": "success", "message": "Welcome to the Task Manager API"}
    
@app.get("/tasks/", response_model = List[Task])
async def get_tasks():
    return tasks

@app.get("/tasks/task_by_id")
async def get_task_by_id(task_id: str):
    for i,t in enumerate(tasks):
        if t.task_id == task_id:
            return t

@app.post("/tasks/")
async def create_task(task: Task):
    for t in tasks:
        if t.task_id == task.task_id:
            return {"status": "failed", "message": "Task with same id already exist. Version Conflict"}
    tasks.append(task)
    return {"status": "success", "message": "Task created successfully", "data": tasks}

@app.put("/tasks/{task_id}")
async def update_task(task_id: str, updated_task: Task):
    for i, t in enumerate(tasks):
        if t.task_id == task_id:
            updated_task.task_id = task_id
            tasks[i] = updated_task 
            return {"status":"success", "message": "Task updated successfully", "data": updated_task}
        
@app.delete("/tasks/{task_id}")
async def delete_task(task_id: str):
    for i, t in enumerate(tasks):
        if t.task_id == task_id:
            del tasks[i]
            return {"status": "success", "message": "Task deleted successfully!"}