from __future__ import annotations

import json
from datetime import datetime
from pathlib import Path

from playwright.sync_api import sync_playwright


TECH_KEYWORDS = [
    "engineer",
    "engineering",
    "developer",
    "software",
    "platform",
    "infrastructure",
    "infra",
    "data",
    "ai",
    "ml",
    "machine learning",
    "scientist",
    "research",
    "analytics",
    "security",
    "cloud",
    "devops",
    "site reliability",
    "sre",
    "backend",
    "frontend",
    "full stack",
    "fullstack",
    "distributed",
    "systems",
    "technical solutions",
    "technical solution",
    "supportability",
    "backline",
    "spark",
    "network",
]


def _today_str() -> str:
    return datetime.now().strftime("%Y-%m-%d")


def parse_databricks_jobs(url: str) -> list[dict]:
    jobs: list[dict] = []
    captured_at = _today_str()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url, wait_until="networkidle")

        links = page.locator('a[href*="/company/careers/"]').all()

        seen: set[tuple[str, str, str]] = set()

        bad_titles = {
            "Open Jobs",
            "Open Positions",
            "Engineering",
            "Overview",
            "Culture",
            "Benefits",
            "Inclusion",
            "Go to Market",
            "Interviewing With Us",
            "Internships & Early Careers",
            "Recruitment Fraud",
        }

        for link in links:
            text = link.inner_text().strip()
            href = link.get_attribute("href")

            if not text or not href:
                continue

            if href.startswith("/"):
                href = "https://www.databricks.com" + href

            lines = [line.strip() for line in text.split("\n") if line.strip()]
            if not lines:
                continue

            title = lines[0]
            location = lines[1] if len(lines) > 1 else ""

            if title in bad_titles:
                continue

            if len(title) < 8 or len(title) > 120:
                continue

            if "/company/careers/open-positions" in href:
                continue
            if href.endswith("/engineering-at-databricks"):
                continue

            key = (title, location, href)
            if key in seen:
                continue
            seen.add(key)

            jobs.append(
                {
                    "job_title": title,
                    "company": "Databricks",
                    "location": location,
                    "apply_url": href,
                    "source": "databricks",
                    "captured_at": captured_at,
                }
            )

        browser.close()

    return jobs


def parse_cloudflare_jobs(url: str) -> list[dict]:
    jobs: list[dict] = []
    captured_at = _today_str()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(url, wait_until="networkidle")

        links = page.locator('a[href*="/careers/jobs/"]').all()

        seen: set[tuple[str, str, str]] = set()

        bad_titles = {
            "Search jobs",
            "View all jobs",
            "All jobs",
            "Apply now",
            "Learn more",
        }

        for link in links:
            text = link.inner_text().strip()
            href = link.get_attribute("href")

            if not text or not href:
                continue

            if href.startswith("/"):
                href = "https://www.cloudflare.com" + href

            if href.rstrip("/") == "https://www.cloudflare.com/careers/jobs":
                continue
            if href.rstrip("/") == "https://www.cloudflare.com/careers/jobs/":
                continue

            lines = [line.strip() for line in text.split("\n") if line.strip()]
            if not lines:
                continue

            title = lines[0]
            location = ""

            if len(lines) >= 3:
                location = lines[-1]
            elif len(lines) == 2:
                location = lines[1]

            if title in bad_titles:
                continue

            if len(title) < 6 or len(title) > 140:
                continue

            bad_title_keywords = [
                "benefits",
                "culture",
                "internships",
                "program",
                "team",
                "about",
                "blog",
            ]
            title_lower = title.lower()
            if any(keyword in title_lower for keyword in bad_title_keywords):
                continue

            key = (title, location, href)
            if key in seen:
                continue
            seen.add(key)

            jobs.append(
                {
                    "job_title": title,
                    "company": "Cloudflare",
                    "location": location,
                    "apply_url": href,
                    "source": "cloudflare",
                    "captured_at": captured_at,
                }
            )

        browser.close()

    return jobs


def filter_tech_jobs(jobs: list[dict]) -> list[dict]:
    filtered: list[dict] = []

    seen: set[tuple[str, str, str]] = set()

    for job in jobs:
        title = str(job.get("job_title", "")).strip()
        location = str(job.get("location", "")).strip()
        apply_url = str(job.get("apply_url", "")).strip()

        if not title or not apply_url:
            continue

        title_lower = title.lower()

        if not any(keyword in title_lower for keyword in TECH_KEYWORDS):
            continue

        key = (title.lower(), location.lower(), apply_url)
        if key in seen:
            continue
        seen.add(key)

        filtered.append(job)

    return filtered


def save_jobs_to_json(jobs: list[dict], filename: str) -> Path:
    project_root = Path(__file__).resolve().parent.parent.parent
    output_dir = project_root / "app" / "db"
    output_dir.mkdir(parents=True, exist_ok=True)

    output_path = output_dir / filename
    output_path.write_text(
        json.dumps(jobs, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )
    return output_path


def run_databricks_pipeline() -> None:
    url = "https://www.databricks.com/company/careers/open-positions"

    all_jobs = parse_databricks_jobs(url)
    tech_jobs = filter_tech_jobs(all_jobs)

    all_jobs_path = save_jobs_to_json(all_jobs, "databricks_jobs.json")
    tech_jobs_path = save_jobs_to_json(tech_jobs, "databricks_tech_jobs.json")

    print("\n=== Databricks ===")
    print(f"Total raw jobs found: {len(all_jobs)}")
    print(f"Total tech jobs found: {len(tech_jobs)}")
    print(f"Saved raw jobs to: {all_jobs_path}")
    print(f"Saved tech jobs to: {tech_jobs_path}")

    print("\n=== Sample Databricks Tech Jobs ===")
    for job in tech_jobs[:10]:
        print(job)


def run_cloudflare_pipeline() -> None:
    url = "https://www.cloudflare.com/careers/jobs/"

    all_jobs = parse_cloudflare_jobs(url)
    tech_jobs = filter_tech_jobs(all_jobs)

    all_jobs_path = save_jobs_to_json(all_jobs, "cloudflare_jobs.json")
    tech_jobs_path = save_jobs_to_json(tech_jobs, "cloudflare_tech_jobs.json")

    print("\n=== Cloudflare ===")
    print(f"Total raw jobs found: {len(all_jobs)}")
    print(f"Total tech jobs found: {len(tech_jobs)}")
    print(f"Saved raw jobs to: {all_jobs_path}")
    print(f"Saved tech jobs to: {tech_jobs_path}")

    print("\n=== Sample Cloudflare Tech Jobs ===")
    for job in tech_jobs[:10]:
        print(job)


if __name__ == "__main__":
    run_databricks_pipeline()