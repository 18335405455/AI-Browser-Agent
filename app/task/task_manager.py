import json
import traceback
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional
from uuid import uuid4

TASKS_DIR = Path("data/tasks")
TASKS_DIR.mkdir(parents=True, exist_ok=True)


def now_str() -> str:
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")


def normalize_mode(mode: Optional[str]) -> str:
    """
    兼容前端可能传来的 default。
    """
    if mode in (None, "", "default"):
        return "local"
    return str(mode)


def get_task_file(task_id: str) -> Path:
    return TASKS_DIR / f"{task_id}.json"


def save_task(task: Dict[str, Any]) -> None:
    task["updated_at"] = now_str()
    task_file = get_task_file(task["task_id"])
    with open(task_file, "w", encoding="utf-8") as f:
        json.dump(task, f, ensure_ascii=False, indent=2)


def load_task(task_id: str) -> Optional[Dict[str, Any]]:
    task_file = get_task_file(task_id)
    if not task_file.exists():
        return None
    with open(task_file, "r", encoding="utf-8") as f:
        return json.load(f)


def list_tasks() -> List[Dict[str, Any]]:
    tasks = []
    for file in TASKS_DIR.glob("*.json"):
        try:
            with open(file, "r", encoding="utf-8") as f:
                tasks.append(json.load(f))
        except Exception:
            continue

    tasks.sort(key=lambda x: x.get("created_at", ""), reverse=True)
    return tasks


def create_task(mode: str = "local", pages: int = 3) -> Dict[str, Any]:
    mode = normalize_mode(mode)
    task_id = str(uuid4())[:8]

    task = {
        "task_id": task_id,
        "status": "pending",   # pending / running / success / failed
        "mode": mode,
        "pages": pages,
        "created_at": now_str(),
        "updated_at": now_str(),
        "started_at": None,
        "finished_at": None,
        "result": None,
        "error": None,
    }
    save_task(task)
    return task


def update_task_status(task_id: str, status: str) -> None:
    task = load_task(task_id)
    if not task:
        return

    task["status"] = status

    if status == "running":
        task["started_at"] = now_str()

    if status in ("success", "failed"):
        task["finished_at"] = now_str()

    save_task(task)


def update_task_result(task_id: str, result: Dict[str, Any]) -> None:
    task = load_task(task_id)
    if not task:
        return
    task["result"] = result
    save_task(task)


def update_task_error(task_id: str, error: str) -> None:
    task = load_task(task_id)
    if not task:
        return
    task["error"] = error
    save_task(task)


def run_pipeline(mode: str, pages: int) -> Dict[str, Any]:
    """
    完整业务链路：
    crawl -> save raw -> enrich(file mode) -> load ai result
    """
    from app.crawler.quotes_spider import crawl_quotes
    from app.analyzer.enrich_quotes import enrich_quotes

    mode = normalize_mode(mode)

    # 1) crawl quotes
    quotes = crawl_quotes(pages=pages)

    if not isinstance(quotes, list):
        raise ValueError("crawl_quotes(pages=...) should return a list")

    # 2) save raw quotes for old analyzer compatibility
    raw_path = Path("data/quotes.json")
    raw_path.parent.mkdir(parents=True, exist_ok=True)

    with open(raw_path, "w", encoding="utf-8") as f:
        json.dump(quotes, f, ensure_ascii=False, indent=2)

    # 3) run old enrich pipeline (file-based)
    enrich_quotes()

    # 4) load enriched output
    ai_path = Path("data/quotes_ai.json")
    if ai_path.exists():
        with open(ai_path, "r", encoding="utf-8") as f:
            enriched_quotes = json.load(f)
    else:
        enriched_quotes = quotes

    # 5) build report
    authors = sorted(list({q.get("author", "Unknown") for q in enriched_quotes}))
    total_tags = sum(len(q.get("tags", [])) for q in enriched_quotes)

    analysis_report = {
        "summary": f"Successfully crawled and AI-enriched {len(enriched_quotes)} quotes.",
        "quote_count": len(enriched_quotes),
        "unique_authors": len(authors),
        "authors": authors[:10],
        "total_tags": total_tags,
        "mode": mode,
        "pages": pages,
    }

    return {
        "quotes": enriched_quotes,
        "analysis_report": analysis_report,
    }


def run_task(task_id: str) -> None:
    max_retries = 3

    for attempt in range(1, max_retries + 1):
        try:
            task = load_task(task_id)
            if not task:
                return

            update_task_status(task_id, "running")

            mode = normalize_mode(task.get("mode", "local"))
            pages = int(task.get("pages", 3))

            result = run_pipeline(mode=mode, pages=pages)

            result["retry_attempt"] = attempt
            update_task_result(task_id, result)
            update_task_status(task_id, "success")
            return

        except Exception as e:
            error_msg = f"[Attempt {attempt}/{max_retries}] {str(e)}\n\n{traceback.format_exc()}"

            if attempt == max_retries:
                update_task_error(task_id, error_msg)
                update_task_status(task_id, "failed")
            else:
                print(f"Retrying task {task_id}... attempt {attempt + 1}")