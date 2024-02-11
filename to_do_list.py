from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

tasks = []

class Task(BaseModel):
    task_id: int
    title: str
    description: str = None

@app.get("/")
async def home():
    return {"status": "success", "message": "Welcome to the Task Manager API"}
    
@app.get("/tasks/", response_model = List[Task])
async def get_tasks():
    return tasks

@app.get("tasks/task_by_id")
async def get_task_by_id(task_id: str):
    for i in tasks:
        if i.task_id == task_id:
            return i

@app.post("/tasks/")
async def create_task(task: Task):
    tasks.append(task)
    return {"status": "success", "message": "Task created successfully", "data": tasks}

@app.put("/tasks/{task_id}")
async def update_task(task_id: int, task: Task):
    for i, t in enumerate(tasks):
        if t.task_id == task_id:
            tasks[i] = task
            return {"status":"success", "message": "Task updated successfully", "data": task}
        
@app.delete("/tasks/{task_id}")
async def delete_task(task_id: int):
    for i, t in enumerate(tasks):
        if t.task_id == task_id:
            del tasks[i]
            return {"status": "success", "message": "Task deleted successfully!"}