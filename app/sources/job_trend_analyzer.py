from __future__ import annotations

import json
import re
from collections import Counter
from datetime import datetime
from pathlib import Path


STOPWORDS = {
    "senior",
    "sr",
    "staff",
    "manager",
    "lead",
    "director",
    "principal",
    "technical",
    "solutions",
    "solution",
    "engineer",
    "engineering",
    "specialist",
    "platform",
    "support",
    "product",
    "global",
    "regional",
    "backline",
    "team",
    "systems",
    "system",
    "data",
    "ai",
    "ml",
    "the",
    "and",
    "for",
    "of",
    "to",
    "in",
    "with",
    "apj",
    "emea",
    "greater",
    "china",
    "region",
}


CATEGORY_RULES = {
    "ai_ml": [
        "ai",
        "ml",
        "machine learning",
        "scientist",
        "research",
        "model",
        "llm",
    ],
    "data_platform": [
        "data",
        "spark",
        "analytics",
        "database",
        "platform",
    ],
    "infra_cloud": [
        "infrastructure",
        "infra",
        "cloud",
        "distributed",
        "systems",
        "devops",
        "sre",
        "site reliability",
        "security",
    ],
    "software_engineering": [
        "software",
        "developer",
        "frontend",
        "backend",
        "fullstack",
        "full stack",
    ],
    "customer_facing_technical": [
        "technical solutions",
        "solution engineer",
        "support",
        "backline",
        "enablement",
    ],
}


def _project_root() -> Path:
    return Path(__file__).resolve().parent.parent.parent


def _today_str() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def load_jobs(filename: str = "databricks_tech_jobs.json") -> list[dict]:
    input_path = _project_root() / "app" / "db" / filename
    if not input_path.exists():
        raise FileNotFoundError(f"Input file not found: {input_path}")
    return json.loads(input_path.read_text(encoding="utf-8"))


def normalize_location(location: str) -> str:
    if not location:
        return "Unknown"
    first = location.split(";")[0].strip()
    return first if first else "Unknown"


def extract_keywords_from_title(title: str) -> list[str]:
    text = title.lower()
    text = re.sub(r"[^a-zA-Z0-9\s\-\/]", " ", text)
    parts = re.split(r"[\s\/\-]+", text)

    keywords: list[str] = []
    for part in parts:
        part = part.strip()
        if not part:
            continue
        if len(part) <= 2:
            continue
        if part in STOPWORDS:
            continue
        keywords.append(part)

    return keywords


def classify_job(title: str) -> list[str]:
    title_lower = title.lower()
    matched_categories: list[str] = []

    for category, rules in CATEGORY_RULES.items():
        if any(rule in title_lower for rule in rules):
            matched_categories.append(category)

    if not matched_categories:
        matched_categories.append("other")

    return matched_categories


def analyze_jobs(jobs: list[dict]) -> dict:
    total_tech_jobs = len(jobs)

    location_counter: Counter[str] = Counter()
    keyword_counter: Counter[str] = Counter()
    category_counter: Counter[str] = Counter()

    captured_dates = [
        str(job.get("captured_at", "")).strip()
        for job in jobs
        if str(job.get("captured_at", "")).strip()
    ]
    captured_at = captured_dates[0] if captured_dates else _today_str()

    for job in jobs:
        title = str(job.get("job_title", "")).strip()
        location = normalize_location(str(job.get("location", "")).strip())

        location_counter[location] += 1
        keyword_counter.update(extract_keywords_from_title(title))
        category_counter.update(classify_job(title))

    summary = {
        "company": "Databricks",
        "captured_at": captured_at,
        "total_tech_jobs": total_tech_jobs,
        "top_locations": [
            {"name": name, "count": count}
            for name, count in location_counter.most_common(10)
        ],
        "top_keywords": [
            {"name": name, "count": count}
            for name, count in keyword_counter.most_common(20)
        ],
        "category_breakdown": dict(category_counter.most_common()),
    }
    return summary


def save_summary(summary: dict, filename: str = "databricks_trend_summary.json") -> Path:
    output_dir = _project_root() / "app" / "db"
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / filename
    output_path.write_text(
        json.dumps(summary, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return output_path


def append_history_snapshot(summary: dict, filename: str = "databricks_trend_history.json") -> Path:
    output_dir = _project_root() / "app" / "db"
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / filename

    history: list[dict] = []
    if output_path.exists():
        try:
            history = json.loads(output_path.read_text(encoding="utf-8"))
            if not isinstance(history, list):
                history = []
        except Exception:
            history = []

    snapshot = {
        "captured_at": summary.get("captured_at", _today_str()),
        "company": summary.get("company", "Databricks"),
        "total_tech_jobs": summary.get("total_tech_jobs", 0),
        "top_location": summary.get("top_locations", [{}])[0].get("name", "Unknown")
        if summary.get("top_locations")
        else "Unknown",
        "top_location_count": summary.get("top_locations", [{}])[0].get("count", 0)
        if summary.get("top_locations")
        else 0,
        "category_breakdown": summary.get("category_breakdown", {}),
        "top_keywords": [item.get("name", "") for item in summary.get("top_keywords", [])[:10]],
    }

    existing_dates = {str(item.get("captured_at", "")) for item in history}
    if snapshot["captured_at"] not in existing_dates:
        history.append(snapshot)

    history.sort(key=lambda x: str(x.get("captured_at", "")))

    output_path.write_text(
        json.dumps(history, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return output_path


if __name__ == "__main__":
    jobs = load_jobs("databricks_tech_jobs.json")
    summary = analyze_jobs(jobs)

    summary_path = save_summary(summary)
    history_path = append_history_snapshot(summary)

    print(f"Loaded tech jobs: {len(jobs)}")
    print(f"Saved trend summary to: {summary_path}")
    print(f"Saved / updated trend history to: {history_path}")

    print("\n=== Trend Summary Preview ===")
    print(f"Company: {summary['company']}")
    print(f"Captured at: {summary['captured_at']}")
    print(f"Total tech jobs: {summary['total_tech_jobs']}")

    print("\nTop Locations:")
    for item in summary["top_locations"][:5]:
        print(item)

    print("\nTop Keywords:")
    for item in summary["top_keywords"][:10]:
        print(item)

    print("\nCategory Breakdown:")
    for k, v in summary["category_breakdown"].items():
        print(f"{k}: {v}")