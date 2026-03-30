# 🤖 AI Browser Agent

🚀 A task-based AI-powered browser automation platform for structured data extraction, task lifecycle management, API services, and interactive visualization.

---

## 🌟 Overview

This project upgrades a traditional crawler script into a **task-driven AI data platform**.

It supports:

* Automated browser interaction using Playwright
* Task-based execution with unique `task_id`
* Persistent task result storage
* RESTful APIs powered by FastAPI
* Interactive task dashboard via Streamlit
* Historical task querying and result traceability
* Local / optional LLM dual analysis modes

> 🧠 Pipeline:
> **Playwright → Task Pipeline → FastAPI → Streamlit Dashboard**

---

## 📸 System Preview

<img width="1919" height="965" alt="dca7bbcff0db6669db87f0e34dbfcc3e" src="https://github.com/user-attachments/assets/ad217ca0-7a14-49d1-b3a5-8080469093a4" />
<img width="1919" height="951" alt="1f15aca86caae514f79034199381b1ac" src="https://github.com/user-attachments/assets/4c69b631-f527-415a-bcd9-f267d7fcc263" />
<img width="1919" height="924" alt="80564177ecaff58f28426b304099491e" src="https://github.com/user-attachments/assets/ec387909-defb-4700-a1f3-87df08afa77b" />
<img width="1919" height="914" alt="61026ec5e7ec7e695f038cd3760e5fea" src="https://github.com/user-attachments/assets/8ff7f053-47d5-48d6-bea2-c3522b2c5b27" />
<img width="1919" height="954" alt="e9a78090c76ca018cdf7e738a3f7d3a6" src="https://github.com/user-attachments/assets/2f67dcb0-862d-42ce-8e46-7489f83c420c" />

<img width="1919" height="948" alt="ae50b060b9cfbe0ceb052bc363632bf3" src="https://github.com/user-attachments/assets/25a018ea-92b4-4511-b6ea-b5946e064875" />
<img width="1919" height="922" alt="0300f763fd9d8e057c4e39b5b8c20adc" src="https://github.com/user-attachments/assets/b310ddfc-98a9-432d-b210-a1e1f90bbd20" />
<img width="1919" height="916" alt="858f867dcaf27837bd38e7defb49838b" src="https://github.com/user-attachments/assets/cb79fa4d-a545-43b8-a117-f38dad13ab98" />
<img width="1919" height="921" alt="1d16c65fa1fc170bccf838cf82d9b901" src="https://github.com/user-attachments/assets/073f316c-4af8-4d5e-a338-19dfe1fc9a6f" />

---

## 🔥 Key Features

### 🌐 Browser Automation (Playwright)

* Automated crawling of multi-page websites
* Handles pagination dynamically
* Extracts structured content reliably
* Supports configurable page depth (`pages`)

### 🧠 Task-Based Pipeline

Each execution generates:

* 🆔 Unique `task_id`
* 📂 Independent task directory
* 📄 `meta.json` for task metadata
* 📥 `quotes_all.json` for raw data
* 📝 `llm_report.txt` for analysis output
* ✅ Task status tracking (`success / failed`)

### 📊 Data Extraction

Each quote contains:

* 📄 Page number
* 💬 Quote text
* 👤 Author
* 🏷️ Tags

### 🧠 Analysis Modes

#### `local`

* Statistical analysis
* Tag / author aggregation
* Lightweight reporting
* Fast demo-friendly mode

#### `llm`

* Theme extraction
* Sentiment analysis
* Tone classification
* AI-generated summaries

### 🔌 FastAPI Backend

* RESTful task APIs
* Auto-generated Swagger docs
* Task creation
* Task history querying
* Task detail retrieval

Endpoints:

* `/tasks/run` → create new task
* `/tasks` → list all tasks
* `/tasks/{task_id}` → get task details

### 🎨 Interactive Dashboard (Streamlit)

#### 📋 Task Control Panel

* Configure crawl pages
* Select analysis mode
* Trigger new task
* Real-time task created feedback

#### 📂 Task History Viewer

* Historical task list
* Task status visualization
* Expandable task details
* Metadata inspection
* Raw quote browsing
* Report visualization

---

## 🛠️ Tech Stack

* Python
* Playwright
* FastAPI
* Streamlit
* JSON task storage
* collections.Counter
* Rule-based NLP
* Optional LLM semantic analysis

---

## 📂 Project Structure

```text
AI-Browser-Agent/
├── app/
│   ├── crawler/
│   │   └── quotes_spider.py
│   ├── analyzer/
│   │   ├── quotes_analyzer.py
│   │   └── llm_analyzer.py
│   ├── api/
│   │   └── main.py
│   └── main.py
├── ui/
│   └── dashboard.py
├── data/
│   └── tasks/
│       └── <task_id>/
│           ├── meta.json
│           ├── quotes_all.json
│           └── llm_report.txt
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

### 🧠 Step 1: Run FastAPI Backend

```bash
uvicorn app.api.main:app --reload
```

Swagger UI:

```text
http://127.0.0.1:8000/docs
```

### 🎨 Step 2: Start Dashboard

```bash
streamlit run ui/dashboard.py
```

```text
http://localhost:8501
```

---

## 📡 API Endpoints

| Endpoint           | Description       |
| ------------------ | ----------------- |
| `/tasks/run`       | Create new task   |
| `/tasks`           | List task history |
| `/tasks/{task_id}` | Get task detail   |

---

## 📊 Example Task Metadata

```json
{
  "task_id": "8be74a50",
  "pages": 2,
  "mode": "local",
  "status": "success",
  "created_at": "2026-03-30T11:36:28"
}
```

---

## 📈 Example Task Workflow

```text
Configure task → Run task → Persist result → Query history → Visualize output
```

---

## 🚧 Future Improvements

* Replace JSON storage with PostgreSQL
* Add async task queue
* Support multi-site crawling
* Add vector search and RAG
* Docker deployment
* Production-ready background workers
* Task retry mechanism

---

## 👩‍💻 Author

Catherine ✨

---

## 💡 Notes

This project demonstrates:

* Task-based data platform architecture
* Browser automation engineering
* Backend API service design
* Interactive visualization dashboard
* End-to-end crawler → backend → frontend workflow
* Real-world task persistence and observability

Not just a crawler — but a **mini AI task-driven data platform**.
