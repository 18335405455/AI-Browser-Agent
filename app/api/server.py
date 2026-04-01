from fastapi import BackgroundTasks, FastAPI, HTTPException
from pydantic import BaseModel

from app.task.task_manager import (
    create_task,
    list_tasks,
    load_task,
    run_task,
)

app = FastAPI(title="AI Browser Agent API")


class CreateTaskRequest(BaseModel):
    mode: str = "default"
    pages: int = 3


@app.get("/")
def root():
    return {"message": "AI Browser Agent API is running"}


@app.post("/tasks/run")
def create_and_run_task(req: CreateTaskRequest, background_tasks: BackgroundTasks):
    task = create_task(mode=req.mode, pages=req.pages)
    background_tasks.add_task(run_task, task["task_id"])

    return {
        "message": "Task created successfully",
        "task_id": task["task_id"],
        "status": task["status"],
    }


@app.get("/tasks")
def get_tasks():
    return {"tasks": list_tasks()}


@app.get("/tasks/{task_id}")
def get_task_detail(task_id: str):
    task = load_task(task_id)
    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    return task