# 🤖 AI Browser Agent Workflow Platform

🚀 An AI-powered async browser workflow platform for structured crawling, LLM enrichment, task lifecycle orchestration, and real-time dashboard monitoring.

---

## 🌟 Overview

This project evolves a traditional Playwright crawler script into a **task-driven AI workflow platform**.

It supports:

* 🌐 Automated multi-page browser crawling
* ⚡ Async task lifecycle management
* 🧠 LLM-powered semantic enrichment
* 📊 Real-time auto-refresh dashboard
* 🔍 Historical task querying and observability
* 🔌 RESTful APIs with FastAPI
* 💾 Persistent JSON-based task storage
* 🛡️ Retry-ready fault-tolerant architecture

> 🧠 Workflow Pipeline:  
> **Browser Crawl → Async Task Lifecycle → LLM Enrichment → Analysis Report → Auto-Refresh Dashboard**

---

## 📸 System Preview

<img width="1919" height="965" alt="dashboard-home" src="https://github.com/user-attachments/assets/ad217ca0-7a14-49d1-b3a5-8080469093a4" />
<img width="1919" height="951" alt="task-running-success" src="https://github.com/user-attachments/assets/4c69b631-f527-415a-bcd9-f267d7fcc263" />
<img width="1919" height="924" alt="enriched-result" src="https://github.com/user-attachments/assets/ec387909-defb-4700-a1f3-87df08afa77b" />
<img width="1919" height="914" alt="analysis-report" src="https://github.com/user-attachments/assets/8ff7f053-47d5-48d6-bea2-c3522b2c5b27" />
<img width="1919" height="954" alt="swagger-ui" src="https://github.com/user-attachments/assets/2f67dcb0-862d-42ce-8e46-7489f83c420c" />

---

## 🔥 Core Features

### 🌐 Browser Automation (Playwright)

* Automated crawling of multi-page websites
* Dynamic pagination support
* Configurable crawl depth via `pages`
* Structured extraction of:
  * quote text
  * author
  * tags
  * page metadata

---

### ⚡ Async Task Lifecycle

Each task goes through a full lifecycle:

```text
pending → running → success / failed
```

Features include:

* 🆔 Unique `task_id`
* 📂 Persistent task storage
* 📜 Historical task traceability
* 🧠 Background execution with FastAPI
* 🔄 Auto-refresh polling dashboard
* 🛡️ Retry-ready fault-tolerant architecture

---

### 🧠 LLM Enrichment Pipeline

After crawling, each quote is AI-enhanced with:

* `ai_theme`
* `ai_sentiment`
* `ai_tone`
* `ai_summary`

System-level aggregated analysis:

* total quote count
* unique authors
* total tag statistics
* author list summary
* task-level report generation

---

### 📊 Real-Time Dashboard (Streamlit)

#### 📋 Task Control Panel
* configure crawl pages
* select mode
* create new task
* real-time feedback

#### 🔄 Auto Refresh UX
* automatic task polling
* no manual refresh required
* seamless transition from `running` to `success`
* real-time result visualization

#### 📂 Task History Viewer
* task list
* lifecycle status
* expandable details
* result JSON preview
* error traceback visibility
* analysis report visualization

---

### 🔌 FastAPI Backend APIs

RESTful endpoints:

* `/tasks/run` → create async task
* `/tasks` → list task history
* `/tasks/{task_id}` → retrieve task detail

Additional features:

* Swagger UI docs
* background task execution
* lifecycle orchestration
* API-friendly task querying

---

## 📊 Example Enriched Output

```json
{
  "text": "The world as we have created it is a process of our thinking.",
  "author": "Albert Einstein",
  "tags": ["change", "thinking"],
  "ai_theme": "deep-thoughts, change",
  "ai_sentiment": "neutral",
  "ai_tone": "philosophical",
  "ai_summary": "A reflective quote about how human thinking shapes reality."
}
```

---

## 📈 Example Task Report

```json
{
  "summary": "Successfully crawled and AI-enriched 100 quotes.",
  "quote_count": 100,
  "unique_authors": 50,
  "total_tags": 232,
  "mode": "default",
  "pages": 3
}
```

---

## 🛠️ Tech Stack

* Python
* Playwright
* FastAPI
* Streamlit
* JSON persistent storage
* Local LLM / optional API LLM
* requests
* Rule-based + LLM semantic analysis

---

## 📂 Project Structure

```text
AI-Browser-Agent/
├── app/
│   ├── crawler/
│   │   └── quotes_spider.py
│   ├── analyzer/
│   │   ├── llm_analyzer.py
│   │   └── enrich_quotes.py
│   ├── api/
│   │   └── server.py
│   └── task/
│       └── task_manager.py
├── ui/
│   └── dashboard.py
├── data/
│   ├── tasks/
│   ├── quotes.json
│   └── quotes_ai.json
├── requirements.txt
└── README.md
```

---

## ▶️ Getting Started

### 1️⃣ Create virtual environment

```bash
python -m venv venv
```

### 2️⃣ Activate

```bash
venv\Scripts\activate
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
playwright install
```

---

## 🚀 Run the Project

### 🧠 Start FastAPI Backend

```bash
python -m uvicorn app.api.server:app --reload
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

### 🎨 Start Streamlit Dashboard

```bash
streamlit run ui/dashboard.py
```

Dashboard:

```text
http://localhost:8501
```

---

## 📡 API Endpoints

| Endpoint | Description |
|---|---|
| `/tasks/run` | Create async task |
| `/tasks` | List task history |
| `/tasks/{task_id}` | Retrieve task detail |

---

## 📈 Workflow Example

```text
Create Task
→ Async Background Crawl
→ LLM Enrichment
→ Auto Refresh Dashboard
→ Analysis Report
→ Historical Query
```

---

## 🚧 Future Improvements

* PostgreSQL task persistence
* Celery / Redis distributed task queue
* Docker one-click deployment
* Multi-site crawling adapters
* Vector search + RAG retrieval layer
* Task-level export APIs
* Production observability metrics

---

## 👩‍💻 Author

Catherine ✨

---

## 💡 Notes

This project demonstrates:

* async workflow platform engineering
* browser automation system design
* FastAPI task lifecycle orchestration
* Streamlit real-time dashboard UX
* LLM-powered semantic enrichment
* task persistence and observability
* crawler → AI → backend → frontend full-stack workflow

> Not just a crawler — but a **mini AI workflow platform prototype**.
