import time
import requests
import streamlit as st

API_BASE = "http://127.0.0.1:8000"

st.set_page_config(page_title="AI Browser Agent Dashboard", layout="wide")
st.title("AI Browser Agent Dashboard")

if "auto_refresh" not in st.session_state:
    st.session_state.auto_refresh = False

if "last_task_id" not in st.session_state:
    st.session_state.last_task_id = None

st.markdown("### Create Task")

col1, col2, col3 = st.columns([2, 2, 1])

with col1:
    mode = st.selectbox("Mode", ["default", "fast", "deep"], index=0)

with col2:
    pages = st.number_input("Pages", min_value=1, max_value=20, value=3, step=1)

with col3:
    st.write("")
    st.write("")
    create_btn = st.button("Run Task", use_container_width=True)

if create_btn:
    try:
        resp = requests.post(
            f"{API_BASE}/tasks/run",
            json={"mode": mode, "pages": pages},
            timeout=10,
        )
        data = resp.json()
        st.success(f"Task created: {data['task_id']} | status={data['status']}")
        st.session_state.last_task_id = data["task_id"]
        st.session_state.auto_refresh = True
    except Exception as e:
        st.error(f"Create task failed: {e}")

st.divider()

st.markdown("### Task List")

status_filter = st.selectbox(
    "Filter by status",
    ["all", "pending", "running", "success", "failed"],
    index=0,
)

manual_refresh = st.button("Refresh")

try:
    resp = requests.get(f"{API_BASE}/tasks", timeout=10)
    tasks = resp.json().get("tasks", [])
except Exception as e:
    st.error(f"Load tasks failed: {e}")
    tasks = []

if status_filter != "all":
    tasks = [t for t in tasks if t.get("status") == status_filter]

current_task_status = None
if st.session_state.last_task_id:
    for t in tasks:
        if t.get("task_id") == st.session_state.last_task_id:
            current_task_status = t.get("status")
            break

if not tasks:
    st.info("No tasks found.")
else:
    for task in tasks:
        with st.expander(
            f"[{task.get('status', 'unknown')}] {task.get('task_id')} | "
            f"mode={task.get('mode')} | pages={task.get('pages')}"
        ):
            st.write("**Created At:**", task.get("created_at"))
            st.write("**Updated At:**", task.get("updated_at"))
            st.write("**Started At:**", task.get("started_at"))
            st.write("**Finished At:**", task.get("finished_at"))

            result = task.get("result")
            error = task.get("error")

            if result:
                st.write("**Result:**")
                st.json(result)

            if error:
                st.write("**Error:**")
                st.code(error)

if st.session_state.auto_refresh and current_task_status in ["pending", "running"]:
    st.info(f"Task {st.session_state.last_task_id} is {current_task_status}... auto refreshing")
    time.sleep(2)
    st.rerun()

if current_task_status in ["success", "failed"]:
    st.session_state.auto_refresh = False