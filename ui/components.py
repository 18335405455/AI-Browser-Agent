from __future__ import annotations

from typing import Any
from textwrap import dedent

import pandas as pd
import plotly.graph_objects as go
import streamlit as st


def browser_shell_header() -> None:
    st.markdown(
        dedent("""
        <div class="top-browser">
            <div class="browser-row">
                <div class="traffic">
                    <span class="dot red"></span>
                    <span class="dot yellow"></span>
                    <span class="dot green"></span>
                </div>
                <div class="browser-bar">AI Browser Agent Workflow Platform / dashboard</div>
                <div class="browser-actions">
                    <div class="mini-btn"></div>
                    <div class="mini-btn"></div>
                    <div class="mini-btn"></div>
                </div>
            </div>
        </div>
        """),
        unsafe_allow_html=True,
    )


def side_nav() -> None:
    st.markdown(
        dedent("""
        <div class="side-nav">
            <div>
                <div class="brand">Z</div>
                <div class="nav-stack">
                    <div class="nav-item active">◈</div>
                    <div class="nav-item">◎</div>
                    <div class="nav-item">◌</div>
                    <div class="nav-item">◍</div>
                    <div class="nav-item">◐</div>
                    <div class="nav-item">◒</div>
                    <div class="nav-item">◓</div>
                </div>
            </div>
            <div class="nav-stack">
                <div class="nav-item">◉</div>
                <div class="nav-item">☻</div>
            </div>
        </div>
        """),
        unsafe_allow_html=True,
    )


def metric_card(title: str, value: str, subtext: str, featured: bool = False) -> None:
    cls = "metric-card featured" if featured else "metric-card"
    st.markdown(
        dedent(f"""
        <div class="{cls}">
            <div class="metric-label">{title}</div>
            <div class="metric-value">{value}</div>
            <div class="metric-foot">
                <span>{subtext}</span>
                <span class="status-dots"><span></span><span></span><span></span><span></span></span>
            </div>
        </div>
        """),
        unsafe_allow_html=True,
    )


def panel_open(title: str, subtitle: str = "", badge: str = "") -> None:
    subtitle_html = f'<div class="panel-subtitle">{subtitle}</div>' if subtitle else ""
    badge_html = f'<div class="badge-glow">{badge}</div>' if badge else ""
    st.markdown(
        dedent(f"""
        <div class="panel">
            <div class="panel-title-row">
                <div>
                    <div class="panel-title">{title}</div>
                    {subtitle_html}
                </div>
                {badge_html}
            </div>
        </div>
        """),
        unsafe_allow_html=True,
    )


def panel_close() -> None:
    return


def analysis_summary_panel() -> bool:
    legend_col1, legend_col2 = st.columns([1, 1], gap="small")

    with legend_col1:
        st.markdown(
            """
            <div style="display:flex; align-items:center; gap:8px; color:#dbe2ff; font-size:13px; margin-bottom:8px;">
                <span style="width:10px;height:10px;border-radius:50%;background:#84cc16;display:inline-block;"></span>
                Actual
            </div>
            """,
            unsafe_allow_html=True,
        )

    with legend_col2:
        st.markdown(
            """
            <div style="display:flex; align-items:center; gap:8px; color:#dbe2ff; font-size:13px; margin-bottom:8px;">
                <span style="width:10px;height:10px;border-radius:50%;background:#e879f9;display:inline-block;"></span>
                AI Projected
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        <div style="color:#a9b4d0;font-size:13px;line-height:1.85; margin-top:10px;">
            Browser execution telemetry, extraction confidence, and analysis throughput
            are aggregated here. Faster response and stable retry handling usually
            produce cleaner task lifecycles and better report consistency.
        </div>
        """,
        unsafe_allow_html=True,
    )

    return st.button("Run Analysis", use_container_width=True, key="run_analysis_btn_main")


def render_priority_tasks_panel(tasks: list[dict[str, Any]]) -> None:
    st.markdown(
        dedent("""
        <div class="panel">
            <div class="panel-title-row">
                <div>
                    <div class="panel-title">Priority Tasks</div>
                    <div class="panel-subtitle">Active reminder queue</div>
                </div>
                <div class="badge-glow">See All</div>
            </div>
        </div>
        """),
        unsafe_allow_html=True,
    )

    for i, task in enumerate(tasks[:3]):
        c1, c2 = st.columns([3.6, 1.4], gap="small")

        with c1:
            name = task.get("name", "Unnamed task")
            date = task.get("date", "--")
            desc = task.get("desc", "Task detail not available.")
            st.markdown(
                f"""
                <div style="font-weight:700;font-size:14px;color:#f5f7ff;margin-bottom:8px;">
                    <span style="display:inline-block;width:10px;height:10px;border-radius:50%;background:#a855f7;box-shadow:0 0 12px rgba(168,85,247,.45);margin-right:10px;"></span>{name}
                </div>
                <div style="color:#aeb7d3;font-size:12px;margin-bottom:6px;">{date}</div>
                <div style="color:#aeb7d3;font-size:13px;line-height:1.6;">{desc}</div>
                """,
                unsafe_allow_html=True,
            )

        with c2:
            st.markdown(
                f"""
                <div style="text-align:right;font-weight:700;font-size:14px;color:#f5f7ff;padding-top:4px;">
                    {task.get("progress", "0/0")}
                </div>
                """,
                unsafe_allow_html=True,
            )

        if i < len(tasks[:3]) - 1:
            st.markdown(
                '<div style="height:1px;background:rgba(255,255,255,0.06);margin:14px 0 16px 0;"></div>',
                unsafe_allow_html=True,
            )


def render_ai_workspace_panel() -> None:
    st.markdown(
        dedent("""
        <div class="panel ai-hero">
            <div style="text-align:center; color:#c4b5fd; font-size:13px;">Hi, Operator</div>
            <div class="ai-title">How can I help you?</div>
            <div class="ai-caption">Agent orchestration / extraction / automation / insight routing</div>
        </div>
        """),
        unsafe_allow_html=True,
    )

    pill_cols = st.columns(3, gap="small")
    pills = ["LoopAI", "GPT Chat", "Deep Seek"]
    for col, label in zip(pill_cols, pills):
        with col:
            st.markdown(
                f"""
                <div style="
                    text-align:center;
                    padding:8px 10px;
                    border-radius:999px;
                    background:rgba(255,255,255,0.05);
                    border:1px solid rgba(255,255,255,0.07);
                    color:#ebe8ff;
                    font-size:12px;
                    margin-bottom:12px;
                ">
                    {label}
                </div>
                """,
                unsafe_allow_html=True,
            )

    labels = [
        "Text Assistance",
        "Process Automation",
        "Optimization",
        "Smart Response",
    ]

    row1 = st.columns(2, gap="small")
    row2 = st.columns(2, gap="small")

    for col, label in zip(row1, labels[:2]):
        with col:
            st.markdown(
                f"""
                <div style="
                    min-height:110px;
                    border-radius:20px;
                    background:linear-gradient(180deg, rgba(255,255,255,0.06), rgba(255,255,255,0.03));
                    border:1px solid rgba(255,255,255,0.07);
                    padding:16px;
                    display:flex;
                    align-items:end;
                    color:#f5f3ff;
                    font-weight:700;
                    margin-bottom:12px;
                ">
                    {label}
                </div>
                """,
                unsafe_allow_html=True,
            )

    for col, label in zip(row2, labels[2:]):
        with col:
            st.markdown(
                f"""
                <div style="
                    min-height:110px;
                    border-radius:20px;
                    background:linear-gradient(180deg, rgba(255,255,255,0.06), rgba(255,255,255,0.03));
                    border:1px solid rgba(255,255,255,0.07);
                    padding:16px;
                    display:flex;
                    align-items:end;
                    color:#f5f3ff;
                    font-weight:700;
                    margin-bottom:12px;
                ">
                    {label}
                </div>
                """,
                unsafe_allow_html=True,
            )

    st.markdown(
        """
        <div style="
            margin-top:4px;
            height:52px;
            border-radius:999px;
            background:rgba(8,12,22,0.88);
            border:1px solid rgba(168,85,247,0.25);
            display:flex;
            align-items:center;
            justify-content:space-between;
            padding:0 10px 0 16px;
            color:#9da7c2;
        ">
            <span>Ask something...</span>
            <div style="
                width:38px;
                height:38px;
                border-radius:50%;
                background:linear-gradient(135deg, #7c3aed, #a855f7);
                box-shadow:0 0 18px rgba(168,85,247,0.35);
            "></div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_manage_projects_panel(df: pd.DataFrame) -> None:
    st.markdown(
        dedent("""
        <div class="panel">
            <div class="panel-title-row">
                <div>
                    <div class="panel-title">Manage Projects</div>
                    <div class="panel-subtitle">Task lifecycle / execution history / workflow table</div>
                </div>
            </div>
        </div>
        """),
        unsafe_allow_html=True,
    )

    tab_cols = st.columns(5, gap="small")
    tabs = ["Priority", "Active", "Completed", "Canceled", "Recommended"]
    for i, (col, tab) in enumerate(zip(tab_cols, tabs)):
        with col:
            active = i == 0
            cls = "tab-chip active" if active else "tab-chip"
            st.markdown(
                f'<div class="{cls}" style="text-align:center;">{tab}</div>',
                unsafe_allow_html=True,
            )

    st.markdown('<div style="height:14px;"></div>', unsafe_allow_html=True)

    header_cols = st.columns([2.6, 1.2, 1.3, 1.0, 1.2], gap="small")
    headers = ["Name", "Source", "Updated", "Value", "Status"]
    for col, h in zip(header_cols, headers):
        with col:
            st.markdown(
                f'<div style="color:#9da7c2;font-size:12px;font-weight:600;padding-bottom:10px;">{h}</div>',
                unsafe_allow_html=True,
            )

    st.markdown(
        '<div style="height:1px;background:rgba(255,255,255,0.06);margin:0 0 6px 0;"></div>',
        unsafe_allow_html=True,
    )

    if df.empty:
        st.info("No tasks yet.")
        return

    for _, row in df.iterrows():
        cols = st.columns([2.6, 1.2, 1.3, 1.0, 1.2], gap="small")
        status = str(row.get("status", "pending")).lower()

        chip_style = {
            "running": "background:rgba(34,197,94,0.12);color:#86efac;",
            "pending": "background:rgba(245,158,11,0.12);color:#fcd34d;",
            "failed": "background:rgba(251,113,133,0.12);color:#fda4af;",
            "completed": "background:rgba(139,92,246,0.14);color:#d8b4fe;",
            "success": "background:rgba(139,92,246,0.14);color:#d8b4fe;",
        }.get(status, "background:rgba(245,158,11,0.12);color:#fcd34d;")

        with cols[0]:
            st.markdown(
                f"""
                <div style="font-weight:700;color:#edf1ff;font-size:14px;margin-bottom:3px;">
                    {row.get('task_name', 'Unnamed Task')}
                </div>
                <div style="color:#9da7c2;font-size:12px;">
                    {row.get('task_type', 'workflow')}
                </div>
                """,
                unsafe_allow_html=True,
            )

        with cols[1]:
            st.markdown(
                f'<div style="color:#edf1ff;font-size:13px;padding-top:6px;">{row.get("source", "browser")}</div>',
                unsafe_allow_html=True,
            )

        with cols[2]:
            st.markdown(
                f'<div style="color:#edf1ff;font-size:13px;padding-top:6px;">{row.get("updated_at", "--")}</div>',
                unsafe_allow_html=True,
            )

        with cols[3]:
            st.markdown(
                f'<div style="color:#edf1ff;font-size:13px;padding-top:6px;">{row.get("price", "--")}</div>',
                unsafe_allow_html=True,
            )

        with cols[4]:
            st.markdown(
                f"""
                <div style="padding-top:2px;">
                    <span style="
                        display:inline-block;
                        padding:5px 10px;
                        border-radius:999px;
                        font-size:11px;
                        font-weight:700;
                        border:1px solid rgba(255,255,255,0.06);
                        {chip_style}
                    ">
                        {status.title()}
                    </span>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown(
            '<div style="height:1px;background:rgba(255,255,255,0.05);margin:12px 0;"></div>',
            unsafe_allow_html=True,
        )

    st.markdown(
        '<div class="footer-note">Task data will use real backend payload when api_client is available.</div>',
        unsafe_allow_html=True,
    )


def earnings_chart() -> None:
    xs = ["W1", "W2", "W3", "W4", "W5", "W6"]
    ys = [110, 140, 128, 182, 168, 245]

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=xs,
            y=ys,
            mode="lines+markers",
            line=dict(color="#8b5cf6", width=4, shape="spline"),
            marker=dict(size=10, color="#a855f7", line=dict(color="#d8b4fe", width=1)),
            fill="tozeroy",
            fillcolor="rgba(139,92,246,0.12)",
            hovertemplate="Revenue: $%{y}<extra></extra>",
        )
    )

    fig.update_layout(
        height=230,
        margin=dict(l=0, r=0, t=10, b=0),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#c7d2fe"),
        xaxis=dict(showgrid=False, zeroline=False, tickfont=dict(color="#7f8ab0")),
        yaxis=dict(showgrid=True, gridcolor="rgba(255,255,255,0.06)", zeroline=False, tickfont=dict(color="#7f8ab0")),
    )
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})


def heatmap_chart() -> None:
    z = [
        [0, 1, 2, 1, 0, 0],
        [1, 2, 3, 2, 1, 0],
        [2, 3, 5, 3, 2, 1],
        [1, 2, 3, 2, 1, 0],
        [0, 1, 2, 1, 0, 0],
    ]

    fig = go.Figure(
        data=go.Heatmap(
            z=z,
            x=["Sun", "Mon", "Tue", "Wed", "Thu", "Fri"],
            y=["10am", "12pm", "2pm", "4pm", "6pm"],
            colorscale=[
                [0.0, "rgba(27,31,49,1)"],
                [0.25, "rgba(91,33,182,0.65)"],
                [0.55, "rgba(124,58,237,0.85)"],
                [1.0, "rgba(192,132,252,1)"],
            ],
            showscale=False,
            hovertemplate="Intensity: %{z}<extra></extra>",
        )
    )

    fig.update_layout(
        height=240,
        margin=dict(l=0, r=0, t=10, b=0),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#c7d2fe"),
        xaxis=dict(showgrid=False, tickfont=dict(color="#8893b5")),
        yaxis=dict(showgrid=False, tickfont=dict(color="#8893b5")),
    )
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})


def line_performance_chart() -> None:
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
    actual = [12, 18, 16, 25, 28, 33]
    projected = [10, 14, 19, 21, 30, 36]

    fig = go.Figure()
    fig.add_trace(
        go.Scatter(
            x=months,
            y=actual,
            mode="lines",
            name="Actual",
            line=dict(width=3, color="#fb7185", shape="spline"),
        )
    )
    fig.add_trace(
        go.Scatter(
            x=months,
            y=projected,
            mode="lines",
            name="Projected",
            line=dict(width=3, color="#8b5cf6", shape="spline"),
            fill="tozeroy",
            fillcolor="rgba(139,92,246,0.10)",
        )
    )

    fig.update_layout(
        height=240,
        margin=dict(l=0, r=0, t=10, b=0),
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color="#c7d2fe"),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, x=0),
        xaxis=dict(showgrid=False, tickfont=dict(color="#8893b5")),
        yaxis=dict(showgrid=True, gridcolor="rgba(255,255,255,0.06)", tickfont=dict(color="#8893b5")),
    )
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})


def build_demo_tasks() -> list[dict[str, Any]]:
    return [
        {
            "name": "Follow-ups",
            "date": "Apr 1",
            "progress": "3/4 Completed",
            "desc": "Retry handling and task consistency checks.",
        },
        {
            "name": "Contract Review",
            "date": "Apr 2",
            "progress": "1/2 Completed",
            "desc": "Review extracted browser actions and structure.",
        },
        {
            "name": "Invoices",
            "date": "Apr 3",
            "progress": "1/5 Completed",
            "desc": "Notify downstream report modules and refresh history.",
        },
    ]


def build_demo_table() -> pd.DataFrame:
    return pd.DataFrame(
        [
            {
                "task_name": "Garden Grove Designs",
                "task_type": "Mobile App",
                "source": "Playwright",
                "updated_at": "Apr 02",
                "price": "$25",
                "status": "running",
            },
            {
                "task_name": "Flora & Fauna Studio",
                "task_type": "Online Shop",
                "source": "Crawler",
                "updated_at": "Apr 03",
                "price": "$50",
                "status": "pending",
            },
            {
                "task_name": "Vibrant Noses Studio",
                "task_type": "Digital Commerce",
                "source": "LLM",
                "updated_at": "Apr 04",
                "price": "$75",
                "status": "completed",
            },
        ]
    )