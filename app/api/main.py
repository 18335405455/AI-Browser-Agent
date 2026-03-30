import json
import os
from fastapi import FastAPI
from app.main import run_task

app = FastAPI()


@app.get("/")
def root():
    return {"message": "AI Browser Agent API is running"}


@app.post("/tasks/run")
def run_new_task(pages: int = 2, mode: str = "local"):
    task_id = run_task(pages, mode)

    return {
        "message": "Task started successfully",
        "task_id": task_id,
        "pages": pages,
        "mode": mode
    }


@app.get("/tasks")
def list_tasks():
    tasks_dir = "data/tasks"

    if not os.path.exists(tasks_dir):
        return {"tasks": []}

    tasks = []

    for task_id in os.listdir(tasks_dir):
        meta_path = os.path.join(tasks_dir, task_id, "meta.json")

        if os.path.exists(meta_path):
            with open(meta_path, "r", encoding="utf-8") as f:
                meta = json.load(f)
                tasks.append(meta)

    tasks.sort(key=lambda x: x.get("created_at", ""), reverse=True)

    return {"tasks": tasks}


@app.get("/tasks/{task_id}")
def get_task(task_id: str):
    task_dir = os.path.join("data", "tasks", task_id)
    meta_path = os.path.join(task_dir, "meta.json")
    quotes_path = os.path.join(task_dir, "quotes_all.json")
    report_path = os.path.join(task_dir, "llm_report.txt")

    if not os.path.exists(meta_path):
        return {"error": "Task not found"}

    with open(meta_path, "r", encoding="utf-8") as f:
        meta = json.load(f)

    quotes = []
    if os.path.exists(quotes_path):
        with open(quotes_path, "r", encoding="utf-8") as f:
            quotes = json.load(f)

    report = ""
    if os.path.exists(report_path):
        with open(report_path, "r", encoding="utf-8") as f:
            report = f.read()

    return {
        "meta": meta,
        "quotes": quotes,
        "report": report
    }