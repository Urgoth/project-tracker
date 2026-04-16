---
title: Local Development Setup
last reviewed: 2026-04-16
---

## Purpose

Run the full development environment locally.

This includes:

- infrastructure services via Docker Compose
- backend application (FastAPI)
- frontend application (Vite)

---

## Prerequisites

Required tools:

- Docker + Docker Compose
- Python + `uv`
- Node.js + npm

---

## Environment Configuration

On first setup:

```sh
cp .env.example .env
````

The `.env` file is used by Docker Compose and backend configuration.

---

## Step 1 — Start Development Environment

Start infrastructure services (e.g. database):

```sh
docker compose -f docker/compose.dev-env.yml --env-file .env up
```

This runs supporting services required by the backend.

---

## Step 2 — Run Backend

```sh
cd backend
uv run uvicorn app.main:app
```

Backend will be available at:

```
http://localhost:<backend-port>
```

(Port defined via configuration)

---

## Step 3 — Run Frontend

```sh
cd frontend
npm install
npm run dev
```

Frontend dev server will be available at:

```
http://localhost:<frontend-port>
```

---

## Development Workflow

Typical startup:

1. Start dev environment (Docker)
2. Start backend
3. Start frontend

All three must be running for full system functionality.

---

## Notes

- Backend and frontend run as separate processes in development
- API communication happens over HTTP
- Environment variables are shared via `.env`

---

## Planned Improvements

The setup will be streamlined in the future using `just` commands, for example:

```sh
just dev
```

This will:

- start Docker services
- run backend
- run frontend
