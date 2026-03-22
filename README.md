````md
# 🤖 AI-Browser-Agent

✨ A browser automation data collection and AI-powered analysis system built with Playwright, FastAPI, and Streamlit.

---

## 🚀 Project Overview

This project automates browser interactions to crawl structured quote data, performs statistical analysis, exposes RESTful APIs, and visualizes results through an interactive dashboard.

> 🧠 End-to-end pipeline:  
> Playwright → Data Processing → FastAPI → Streamlit Dashboard

---

## 🔥 Features

### 🌐 Browser Automation
- Automated browser control using Playwright
- Multi-page crawling (pagination support)

### 📥 Data Extraction
- Extract structured fields:
  - 📄 page
  - 💬 quote text
  - 👤 author
  - 🏷️ tags

### 💾 Data Storage
- Save raw data to `data/quotes_all.json`

### 📊 Statistical Analysis
- Total number of quotes
- Top 10 authors
- Top 10 tags
- Quotes per page distribution
- Output saved to `data/analysis_report.json`

### 🔌 API Service (FastAPI)
- `/quotes` → return all quotes
- `/analysis` → return analysis results
- Swagger UI for API testing

### 🎨 Interactive Dashboard (Streamlit)
- Overview metrics
- Top authors & tags visualization
- Quotes per page chart
- Search & filter quotes
- API connection status display

### 🤖 LLM Integration (with fallback)
- Optional AI-based analysis
- Graceful fallback when quota unavailable

---

## 🛠️ Tech Stack

- 🐍 Python
- 🎭 Playwright
- ⚡ FastAPI
- 🎨 Streamlit
- 📦 JSON
- 🔢 collections.Counter

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
│   │   └── server.py
│   └── main.py
├── ui/
│   └── dashboard.py
├── data/
│   ├── quotes_all.json
│   ├── analysis_report.json
│   └── llm_report.txt
├── README.md
└── requirements.txt
````

---

## ▶️ How to Run

### 1️⃣ Create virtual environment

```bash
python -m venv venv
```

### 2️⃣ Activate environment

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

### 🧠 Step 1: Run crawler + analysis

```bash
python app/main.py
```

---

### 🔌 Step 2: Start FastAPI backend

```bash
uvicorn app.api.server:app --reload
```

👉 Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

### 🎨 Step 3: Start dashboard

```bash
streamlit run ui/dashboard.py
```

---

## 📊 API Endpoints

| Endpoint    | Description          |
| ----------- | -------------------- |
| `/quotes`   | Get all quotes       |
| `/analysis` | Get analysis results |

---

## 📌 Sample Output

### 💬 Quote Example

```json
{
  "page": 1,
  "text": "The world as we have created it is a process of our thinking.",
  "author": "Albert Einstein",
  "tags": ["thinking", "world"]
}
```

---

### 📊 Analysis Example

```json
{
  "total_quotes": 100,
  "top_10_authors": [["Albert Einstein", 10]],
  "top_10_tags": [["love", 14]]
}
```

---

## 📸 Demo

> Dashboard UI preview (see screenshots in repository)

---

## 🔮 Future Improvements

* 🧠 Enhance LLM-based insights
* 🗄️ Add PostgreSQL storage
* 🌍 Support multiple websites
* 🛡️ Add login / anti-bot handling
* 🐳 Docker deployment
* ⚡ FastAPI → production-ready service

---

## 👩‍💻 Author

Catherine 💅

```
```
