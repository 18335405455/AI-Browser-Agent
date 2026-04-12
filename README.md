# 🚀 AI Browser Agent Workflow Platform

An end-to-end **AI-powered browser workflow and technical hiring radar platform** built with **FastAPI, Playwright, Streamlit, and structured trend analytics pipelines**.

This platform transforms global career pages into **actionable technical hiring intelligence**, enabling task-driven crawling, role filtering, trend summarization, historical snapshot accumulation, and visual dashboard monitoring.

---

## ✨ Key Highlights

- 🌍 Global tech hiring source parsing
- 🤖 Playwright-powered structured job extraction
- 🧠 Technical role filtering pipeline
- 📈 Hiring trend analytics and keyword mining
- 🕒 Historical snapshot persistence
- 📊 Streamlit visual hiring radar dashboard
- 🔌 FastAPI backend with Swagger workflow APIs
- 📦 Task lifecycle orchestration and async scheduling

---

## 🖥️ Dashboard Overview

The platform provides a polished **AI workflow dashboard** for technical hiring intelligence monitoring.

![Dashboard Overview](./assets/01-dashboard-overview.png)

---

## 📈 Hiring Trend Analysis

A dedicated trend analysis panel highlights:

- total technical jobs
- top hiring locations
- recurring keywords
- category distribution
- latest snapshot metrics

![Trend Analysis](./assets/02-trend-analysis-panel.png)

---

## 🕒 Category & History Insights

The dashboard also supports:

- category breakdown table
- top keywords panel
- trend history table
- historical snapshot timeline

![Category History](./assets/03-category-history-panel.png)

---

## 📋 Task Lifecycle Management

All browser workflow tasks are persisted and visualized through a structured task lifecycle table.

Features include:

- task id tracking
- execution source
- updated time
- success status
- lifecycle history

![Task Lifecycle](./assets/04-task-lifecycle-table.png)

---

## 🧠 System Architecture

The entire platform follows a complete data pipeline:

Career Source → Parser → Storage → Filter → Analyzer → Summary + History → Dashboard

![System Architecture](./assets/05-system-architecture.png)

### Pipeline Modules

- **Career Pages** → global hiring sources
- **Playwright Job Parser** → structured extraction
- **Raw Jobs Storage** → JSON persistence
- **Tech Job Filter** → AI / backend / infra role selection
- **Trend Analyzer** → location + keyword + category mining
- **Trend Summary** → latest hiring snapshot
- **Trend History** → daily accumulation
- **Dashboard** → visual intelligence delivery

---

## 🔌 Backend API Surface

The FastAPI backend exposes a production-style API workflow.

### Swagger Overview
![Swagger API](./assets/06-api-swagger-overview.png)

### Task Run Request
A task can be created dynamically for a technical hiring radar workflow.

![Task Run Request](./assets/07-api-task-run-request.png)

### Task Run Response
Successful task creation returns:

- `task_id`
- `pending` lifecycle state
- background scheduling confirmation

![Task Run Response](./assets/08-api-task-run-response.png)

---

## ⚙️ Tech Stack

### Backend
- FastAPI
- Uvicorn
- Playwright
- Python 3.11

### Frontend
- Streamlit
- Custom dashboard components
- Metrics panels
- Trend history visual blocks

### Data Layer
- JSON persistence
- task snapshots
- trend summaries
- historical timeline accumulation

### Workflow
- task lifecycle orchestration
- async scheduling
- source-based pipelines
- hiring trend analytics

---

## 📊 Example Use Case

### Global Technical Hiring Radar
Currently tracks:

- Databricks
- global technical roles
- AI / backend / infra / platform trends
- hiring hotspot cities
- keyword demand evolution

Future tracked sources can be expanded to:

- Anthropic
- OpenAI
- Cloudflare
- Vercel

---

## 🎯 Project Value

This project demonstrates end-to-end capability across:

- browser automation
- backend API engineering
- data pipeline design
- trend analytics
- task orchestration
- dashboard productization
- portfolio-grade documentation

It is designed as a **resume-ready AI engineering showcase project** for:

- AI Application Engineer
- Full Stack AI Engineer
- AI Workflow Engineer
- Platform Engineer Intern roles

---

## 🚀 Run Locally

### 1) Backend
```bash
uvicorn app.api.main:app --reload
```

### 2) Dashboard
```bash
streamlit run ui/dashboard.py
```

### 3) Swagger Docs
```text
http://127.0.0.1:8000/docs
```

---

## 📌 Future Roadmap

- multi-company source expansion
- trend delta comparison
- time-series line charts
- hiring growth alerts
- AI-generated trend reports
- recruiter intelligence workflows
- scheduled daily automation
- cloud deployment pipeline

---

## ⭐ Portfolio Note

This repository is intentionally designed as a **portfolio-grade AI workflow platform case study**, emphasizing:

- engineering clarity
- product-level UX
- system architecture transparency
- API execution proof
- visual storytelling for technical interviews
