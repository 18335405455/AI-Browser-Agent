from __future__ import annotations

from typing import Any
import json
from pathlib import Path

import pandas as pd
import streamlit as st

from styles import inject_global_styles
from components import (
    analysis_summary_panel,
    browser_shell_header,
    build_demo_table,
    build_demo_tasks,
    earnings_chart,
    heatmap_chart,
    line_performance_chart,
    metric_card,
    render_ai_workspace_panel,
    render_manage_projects_panel,
    render_priority_tasks_panel,
    side_nav,
)


st.set_page_config(
    page_title="AI Browser Agent Dashboard",
    page_icon="🖥️",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def safe_get_real_data() -> dict[str, Any]:
    data: dict[str, Any] = {
        "metrics": {
            "clients": "14",
            "revenue": "$3.52",
            "projects": "22",
            "priority": "03",
        },
        "task_queue": build_demo_tasks(),
        "table": build_demo_table(),
    }

    try:
        from api_client import get_tasks  # type: ignore

        try:
            tasks_payload = get_tasks()
            if isinstance(tasks_payload, list) and tasks_payload:
                rows: list[dict[str, Any]] = []
                queue: list[dict[str, Any]] = []

                for idx, item in enumerate(tasks_payload[:10]):
                    task_id = item.get("task_id", f"T-{idx + 1:03d}")
                    status = str(item.get("status", "pending"))
                    updated = item.get("updated_at") or item.get("created_at") or "--"
                    task_type = item.get("task_type") or item.get("mode") or "workflow"
                    source = item.get("source") or "browser"

                    rows.append(
                        {
                            "task_name": task_id,
                            "task_type": task_type,
                            "source": source,
                            "updated_at": str(updated)[:10],
                            "price": "$--",
                            "status": status,
                        }
                    )

                    queue.append(
                        {
                            "name": task_id,
                            "date": str(updated)[:10],
                            "progress": f"{idx + 1}/{len(tasks_payload)} Active",
                            "desc": f"{task_type} / {status}",
                        }
                    )

                if rows:
                    data["table"] = pd.DataFrame(rows)
                if queue:
                    data["task_queue"] = queue[:3]

                data["metrics"]["projects"] = str(len(tasks_payload))
        except Exception:
            pass

    except Exception:
        pass

    return data


def top_metrics(metrics: dict[str, str]) -> None:
    c1, c2, c3, c4 = st.columns(4, gap="small")

    with c1:
        metric_card("Clients", metrics.get("clients", "14"), "Compare 10 last month", featured=True)
    with c2:
        metric_card("Revenue", metrics.get("revenue", "$3.52"), "$3720.00 last month")
    with c3:
        metric_card("Projects", metrics.get("projects", "22"), "Compare 16 last month")
    with c4:
        metric_card("Priority Tasks", metrics.get("priority", "03"), "Queue synced")


def simple_panel_title(title: str, subtitle: str = "", badge: str = "") -> None:
    if badge:
        st.markdown(
            f"""
            <div style="display:flex;justify-content:space-between;align-items:flex-start;margin-bottom:10px;">
                <div>
                    <div class="panel-title">{title}</div>
                    <div class="panel-subtitle">{subtitle}</div>
                </div>
                <div class="badge-glow">{badge}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        subtitle_html = f'<div class="panel-subtitle">{subtitle}</div>' if subtitle else ""
        st.markdown(
            f"""
            <div style="margin-bottom:10px;">
                <div class="panel-title">{title}</div>
                {subtitle_html}
            </div>
            """,
            unsafe_allow_html=True,
        )


def _project_root() -> Path:
    return Path(__file__).resolve().parent.parent


def _read_json_from_db(filename: str) -> dict[str, Any] | list[Any] | None:
    try:
        file_path = _project_root() / "app" / "db" / filename
        if file_path.exists():
            return json.loads(file_path.read_text(encoding="utf-8"))
    except Exception:
        return None
    return None


def _read_trend_summary(filename: str = "databricks_trend_summary.json") -> dict[str, Any] | None:
    data = _read_json_from_db(filename)
    return data if isinstance(data, dict) else None


def _read_trend_history(filename: str = "databricks_trend_history.json") -> list[dict[str, Any]]:
    data = _read_json_from_db(filename)
    if isinstance(data, list):
        return [item for item in data if isinstance(item, dict)]
    return []


def _format_category_name(raw: str) -> str:
    mapping = {
        "ai_ml": "AI / ML",
        "data_platform": "Data Platform",
        "infra_cloud": "Infra / Cloud",
        "software_engineering": "Software Engineering",
        "customer_facing_technical": "Customer-Facing Technical",
        "other": "Other",
    }
    return mapping.get(raw, raw.replace("_", " ").title())


def render_trend_analysis(summary: dict[str, Any] | None, history: list[dict[str, Any]]) -> None:
    st.markdown('<div style="height:10px;"></div>', unsafe_allow_html=True)
    st.markdown("### Tech Hiring Trend Result")

    if not summary:
        st.warning(
            "No Databricks trend summary found yet. "
            "Please run `python -m app.sources.job_trend_analyzer` first."
        )
        return

    company = str(summary.get("company", "Unknown"))
    captured_at = str(summary.get("captured_at", "--"))
    total_tech_jobs = summary.get("total_tech_jobs", "--")
    top_locations = summary.get("top_locations", [])
    top_keywords = summary.get("top_keywords", [])
    category_breakdown = summary.get("category_breakdown", {})
    history_count = len(history)

    info_col1, info_col2 = st.columns(2, gap="small")
    with info_col1:
        st.markdown(
            f"""
            <div style="
                border:1px solid rgba(255,255,255,0.06);
                border-radius:18px;
                background:rgba(8,12,22,0.72);
                padding:14px 16px;
                margin-bottom:12px;
            ">
                <div style="color:#9da7c2;font-size:12px;margin-bottom:6px;">Company</div>
                <div style="color:#f4f7ff;font-size:18px;font-weight:700;">{company}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    with info_col2:
        st.markdown(
            f"""
            <div style="
                border:1px solid rgba(255,255,255,0.06);
                border-radius:18px;
                background:rgba(8,12,22,0.72);
                padding:14px 16px;
                margin-bottom:12px;
            ">
                <div style="color:#9da7c2;font-size:12px;margin-bottom:6px;">Analysis Scope</div>
                <div style="color:#d8b4fe;font-size:18px;font-weight:700;">Technical Hiring Radar</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        f"""
        <div style="
            border:1px solid rgba(168,85,247,0.16);
            border-radius:20px;
            background:linear-gradient(180deg, rgba(16,22,38,0.86), rgba(8,12,22,0.92));
            padding:16px 18px;
            margin-bottom:14px;
        ">
            <div style="color:#9da7c2;font-size:12px;margin-bottom:8px;">Summary</div>
            <div style="color:#f4f7ff;font-size:14px;line-height:1.8;">
                Databricks technical hiring radar is active. Current parsed technical openings: <b>{total_tech_jobs}</b>.
                Latest snapshot date: <b>{captured_at}</b>. Historical snapshots stored: <b>{history_count}</b>.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    metric_a, metric_b, metric_c = st.columns(3, gap="small")
    with metric_a:
        st.metric("Total Tech Jobs", total_tech_jobs)
    with metric_b:
        st.metric("Top Location Count", top_locations[0]["count"] if top_locations else "--")
    with metric_c:
        st.metric("Keyword Samples", len(top_keywords))

    extra_col1, extra_col2, extra_col3 = st.columns(3, gap="small")
    with extra_col1:
        st.metric("Tracked Source", company)
    with extra_col2:
        st.metric("Category Types", len(category_breakdown))
    with extra_col3:
        st.metric("Captured At", captured_at)

    st.markdown(
        f"""
        <div style="margin-top:6px;margin-bottom:14px;color:#9da7c2;font-size:13px;">
            History Snapshots: <span style="color:#f4f7ff;font-weight:700;">{history_count}</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if top_locations:
        st.markdown("#### Top Locations")
        for item in top_locations[:5]:
            st.markdown(f"- {item.get('name', '--')}: {item.get('count', '--')}")

    if top_keywords:
        st.markdown("#### Top Keywords")
        keyword_text = " · ".join(
            [f"{item.get('name', '--')} ({item.get('count', '--')})" for item in top_keywords[:10]]
        )
        st.markdown(
            f"""
            <div style="
                border:1px solid rgba(255,255,255,0.06);
                border-radius:16px;
                background:rgba(8,12,22,0.68);
                padding:14px 16px;
                margin-bottom:12px;
                color:#f4f7ff;
                line-height:1.8;
            ">
                {keyword_text}
            </div>
            """,
            unsafe_allow_html=True,
        )

    if category_breakdown:
        st.markdown("#### Category Breakdown")
        category_df = pd.DataFrame(
            [
                {
                    "Category": _format_category_name(k),
                    "Count": v,
                }
                for k, v in category_breakdown.items()
            ]
        )
        st.dataframe(category_df, use_container_width=True, hide_index=True)

    if history:
        st.markdown("#### Trend History")
        history_df = pd.DataFrame(
            [
                {
                    "Captured At": item.get("captured_at", "--"),
                    "Company": item.get("company", "--"),
                    "Total Tech Jobs": item.get("total_tech_jobs", "--"),
                    "Top Location": item.get("top_location", "--"),
                    "Top Location Count": item.get("top_location_count", "--"),
                }
                for item in history
            ]
        )
        st.dataframe(history_df, use_container_width=True, hide_index=True)

    with st.expander("View raw trend summary JSON", expanded=False):
        st.json(summary)

    with st.expander("View raw trend history JSON", expanded=False):
        st.json(history)


def main() -> None:
    inject_global_styles()
    payload = safe_get_real_data()
    trend_summary = _read_trend_summary()
    trend_history = _read_trend_history()

    st.markdown('<div class="app-shell">', unsafe_allow_html=True)
    browser_shell_header()

    nav_col, main_col, right_col = st.columns([0.7, 6.2, 3.0], gap="small")

    with nav_col:
        side_nav()

    with main_col:
        top_metrics(payload["metrics"])

        left_sub, right_sub = st.columns([1.0, 1.15], gap="small")

        with left_sub:
            simple_panel_title("Tech Hiring Trend Analysis")
            run_clicked = analysis_summary_panel()

            if run_clicked:
                latest_summary = _read_trend_summary()
                latest_history = _read_trend_history()
                if latest_summary:
                    st.success("Trend summary loaded successfully.")
                    render_trend_analysis(latest_summary, latest_history)
                else:
                    st.warning(
                        "No trend summary file found yet. "
                        "Please run `python -m app.sources.job_trend_analyzer` first."
                    )
            else:
                if trend_summary:
                    render_trend_analysis(trend_summary, trend_history)

        with right_sub:
            simple_panel_title("Earnings Last 30 Days", badge="Live")
            earnings_chart()
            st.markdown(
                """
                <div style="display:flex;justify-content:space-between;color:#c8d3f4;font-size:13px;margin-top:-8px;margin-bottom:16px;">
                    <div>
                        <span style="color:#8ea0ca;">Earned</span><br>
                        <span style="font-size:28px;font-weight:800;color:white;">$220</span>
                    </div>
                    <div style="text-align:right;">
                        <span style="color:#8ea0ca;">Projected</span><br>
                        <span style="font-size:28px;font-weight:800;color:white;">$245</span>
                    </div>
                </div>
                """,
                unsafe_allow_html=True,
            )

        render_manage_projects_panel(payload["table"])

    with right_col:
        render_priority_tasks_panel(payload["task_queue"])
        render_ai_workspace_panel()

        simple_panel_title("Orders by Time", "Execution intensity heatmap")
        heatmap_chart()

        simple_panel_title("Sales Performance", "Projected vs actual")
        line_performance_chart()

    st.markdown("</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()