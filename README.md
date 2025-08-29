# Task Manager Dashboard (Modular, Beginner–Intermediate)

A minimal multi-service example using FastAPI for services, Streamlit for UI, and Docker Compose for orchestration.
The goal is to demonstrate clean modular structure, service boundaries, and good practices without overwhelming complexity.

Services:
- users — authentication (stub) & user directory
- tasks — CRUD for tasks with simple status workflow
- gateway — single entrypoint that proxies requests to the services
- ui — Streamlit dashboard calling the gateway

Quick Start (Local):
1) Create a venv and activate it.
2) pip install -r requirements.txt and the per-service requirements.
3) Run uvicorn for users:8001, tasks:8002, gateway:8080; run Streamlit on 8501.

Quick Start (Docker):
1) Copy .env.example to .env (optional).
2) Run: docker compose up --build
3) UI at http://localhost:8501 ; Gateway at http://localhost:8080/docs

Scripts & Tooling: black, flake8, isort, pytest, Makefile, GitHub Actions.
