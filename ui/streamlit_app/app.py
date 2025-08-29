import os

import httpx
import streamlit as st

GATEWAY_URL = os.getenv("GATEWAY_URL", "http://localhost:8080").rstrip("/")

st.set_page_config(page_title="Task Manager", page_icon="✅", layout="wide")
st.title("Task Manager Dashboard")

tab_users, tab_tasks = st.tabs(["Users", "Tasks"])

with tab_users:
    st.subheader("Create User")
    with st.form("create_user"):
        name = st.text_input("Name")
        email = st.text_input("Email")
        submitted = st.form_submit_button("Create")
        if submitted and name and email:
            with httpx.Client() as c:
                r = c.post(f"{GATEWAY_URL}/v1/users", json={"name": name, "email": email})
            if r.status_code == 201:
                st.success("User created!")
            else:
                st.error(f"Error: {r.text}")

    st.subheader("Users")
    with httpx.Client() as c:
        r = c.get(f"{GATEWAY_URL}/v1/users")
    users = r.json()
    st.table(users)

with tab_tasks:
    st.subheader("Create Task")
    with st.form("create_task"):
        title = st.text_input("Title")
        description = st.text_area("Description")
        assignee_id = st.text_input("Assignee ID (optional)")
        status = st.selectbox("Status", ["todo", "in_progress", "done"])
        submitted = st.form_submit_button("Create")
        if submitted and title:
            payload = {
                "title": title,
                "description": description or None,
                "assignee_id": assignee_id or None,
                "status": status,
            }
            with httpx.Client() as c:
                r = c.post(f"{GATEWAY_URL}/v1/tasks", json=payload)
            if r.status_code == 201:
                st.success("Task created!")
            else:
                st.error(f"Error: {r.text}")

    st.subheader("Tasks")
    status_filter = st.selectbox("Filter by status", ["", "todo", "in_progress", "done"])
    params = {}
    if status_filter:
        params["status"] = status_filter
    with httpx.Client() as c:
        r = c.get(f"{GATEWAY_URL}/v1/tasks", params=params)
    tasks = r.json()
    st.table(tasks)
