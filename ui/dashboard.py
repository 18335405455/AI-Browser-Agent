import requests
import streamlit as st

API_BASE = "http://127.0.0.1:8000"

st.set_page_config(page_title="AI Browser Agent", layout="wide")
st.title("🤖 AI Browser Agent Dashboard")

# ===== 创建任务 =====
st.sidebar.header("Run New Task")
pages = st.sidebar.number_input("Pages", min_value=1, value=2)
mode = st.sidebar.selectbox("Mode", ["local", "llm"])

if st.sidebar.button("Run Task"):
    response = requests.post(
        f"{API_BASE}/tasks/run",
        params={"pages": pages, "mode": mode}
    )
    result = response.json()
    st.sidebar.success(f"Task created: {result['task_id']}")

# ===== 任务列表 =====
st.header("📋 Task History")

tasks_response = requests.get(f"{API_BASE}/tasks")
tasks = tasks_response.json().get("tasks", [])

for task in tasks:
    task_id = task["task_id"]

    with st.expander(f"Task {task_id} | {task['status']}"):
        detail = requests.get(f"{API_BASE}/tasks/{task_id}").json()

        st.json(detail["meta"])

        st.subheader("Quotes")
        st.write(detail["quotes"][:3])  # 只展示前3条

        st.subheader("Report")
        st.text(detail["report"][:1000])