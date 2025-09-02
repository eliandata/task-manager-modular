# Task Manager Dashboard (Modular, Beginner–Intermediate)

A minimal multi-service example using FastAPI for services, Streamlit for UI, and Docker Compose for orchestration.
The goal is to demonstrate clean modular structure, service boundaries, and good practices without overwhelming complexity.

Services:
- users — authentication (stub) & user directory
- tasks — CRUD for tasks with simple status workflow
- gateway — single entrypoint that proxies requests to the services
- ui — Streamlit dashboard calling the gateway


This guide walks you **step by step** to: **clone the repo**, **create a Python virtual environment**, **install dependencies**, and **run the app locally using Docker & Docker Compose**.

> The virtual environment and Python dependencies help with local development (tests, linters, IDE support).
> **Running the app** itself will be done with **Docker**, so the virtualenv is optional for running, but recommended for development.

---

## 1) Clone the repository

```bash
git clone <YOUR_FORK_OR_REPO_URL>.git
cd task-manager-modular
```

---

## 2) Create a Python virtual environment (recommended for development)

### macOS / Linux
```bash
python -m venv .venv
source .venv/bin/activate
```

### Windows (PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Upgrade packaging tools:
```bash
python -m pip install --upgrade pip
```

---

## 3) Install Python dependencies (for local dev only)

If your repository keeps per‑service requirements, install each (adjust paths if your repo differs):

```bash
pip install -r requirements.txt
pip install -r services/users/requirements.txt
pip install -r services/tasks/requirements.txt
pip install -r gateway/requirements.txt
pip install -r ui/requirements.txt
```

> If your project uses a single consolidated `requirements.txt`, just install that one.

---

## 4) Configure environment variables

Copy the example and edit as needed:

```bash
cp .env.example .env
```

Typical keys (Docker uses service names on the internal network):
```env
# Ports (host → container mappings are handled by docker-compose.yml)
USERS_PORT=8001
TASKS_PORT=8002
GATEWAY_PORT=8080
STREAMLIT_PORT=8501

# Service discovery inside Docker network
USERS_SERVICE_URL=http://users:8001
TASKS_SERVICE_URL=http://tasks:8002
GATEWAY_URL=http://gateway:8080
```

---

## 5) Build and run locally using Docker

Ensure **Docker** and **Docker Compose v2** are installed (`docker compose` command available).

```bash
# Build images and start all services in the background
docker compose up --build -d
```

**What starts:**
- **Users service** (FastAPI) → http://localhost:8001/docs
- **Tasks service** (FastAPI) → http://localhost:8002/docs
- **Gateway** (FastAPI)       → http://localhost:8080/docs
- **UI** (Streamlit)          → http://localhost:8501

Check containers:
```bash
docker compose ps
```

Follow logs (all services):
```bash
docker compose logs -f
```

---

## 6) Verify the stack is running

Open in your browser:
- UI → **http://localhost:8501**
- Gateway (Swagger) → **http://localhost:8080/docs**
- Users (Swagger) → **http://localhost:8001/docs**
- Tasks (Swagger) → **http://localhost:8002/docs**

Quick health checks:
```bash
curl http://localhost:8001/health   # users
curl http://localhost:8002/health   # tasks
curl http://localhost:8080/health   # gateway
```

---

## 7) Stop & clean up

```bash
# Stop containers and remove default network
docker compose down

# (Optional) Remove volumes (⚠️ deletes container data)
docker compose down -v
```

---

## 8) Troubleshooting

- **Ports already in use**: Change ports in `.env` and/or `docker-compose.yml`, or free the port on your machine.
- **UI can’t reach the Gateway**: Ensure the UI uses `GATEWAY_URL=http://gateway:8080` inside Docker; from host, use `http://localhost:8080`.
- **Gateway can’t reach services**: Inside Docker use service names: `http://users:8001` and `http://tasks:8002`.
- **Code changes don’t reflect**: If using bind mounts with auto‑reload, services should refresh. Else, rebuild: `docker compose build --no-cache` then `docker compose up -d`.
- **Permission/Not found**: Verify bind‑mounted paths exist and you have access.
- **Compose v1 vs v2**: Use `docker compose ...` (with a space), not `docker-compose` (deprecated).

---

## 9) Useful commands

```bash
# Rebuild only one service and restart it
docker compose build --no-cache gateway && docker compose up -d gateway

# Exec into a container (shell)
docker compose exec users sh     # or bash depending on the image

# View logs from a single service
docker compose logs -f ui
```

Happy coding! 🚀