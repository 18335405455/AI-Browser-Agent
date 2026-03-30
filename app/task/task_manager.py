import os
import json
import uuid
from datetime import datetime


def create_task(pages, mode):
    task_id = str(uuid.uuid4())[:8]
    task_dir = f"data/tasks/{task_id}"

    os.makedirs(task_dir, exist_ok=True)

    meta = {
        "task_id": task_id,
        "pages": pages,
        "mode": mode,
        "status": "running",
        "created_at": datetime.now().isoformat()
    }

    with open(f"{task_dir}/meta.json", "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)

    return task_id, task_dir


def update_task_status(task_dir, status, error=None):
    meta_path = f"{task_dir}/meta.json"

    with open(meta_path, "r", encoding="utf-8") as f:
        meta = json.load(f)

    meta["status"] = status

    if error:
        meta["error"] = str(error)

    with open(meta_path, "w", encoding="utf-8") as f:
        json.dump(meta, f, indent=2)