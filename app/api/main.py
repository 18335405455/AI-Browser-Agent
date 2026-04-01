import json

from fastapi import FastAPI, HTTPException

from app.main import run_task
from app.task.task_manager import load_task, list_tasks

app = FastAPI()


@app.get("/")
def root():
    return {"message": "AI Browser Agent API is running"}


@app.post("/tasks/run")
def run_new_task(pages: int = 2, mode: str = "local"):
    try:
        task_id = run_task(pages, mode)
        task = load_task(task_id)

        return {
            "message": "Task finished",
            "task_id": task_id,
            "pages": pages,
            "mode": task.get("mode", mode) if task else mode,
            "status": task.get("status", "unknown") if task else "unknown",
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/tasks")
def get_tasks():
    return {"tasks": list_tasks()}


@app.get("/tasks/{task_id}")
def get_task_detail(task_id: str):
    task = load_task(task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")

    result = task.get("result") or {}
    quotes = result.get("quotes", [])
    analysis_report = result.get("analysis_report", "")

    if isinstance(analysis_report, (dict, list)):
        report = json.dumps(analysis_report, ensure_ascii=False, indent=2)
    else:
        report = str(analysis_report) if analysis_report is not None else ""

    meta = {k: v for k, v in task.items() if k != "result"}

    return {
        "meta": meta,
        "quotes": quotes,
        "report": report
    }