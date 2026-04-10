## Local development

The local development environment uses Docker Compose and starts three services:

- `frontend` — Vue + Vite dev server
- `backend` — FastAPI dev server
- `db` — PostgreSQL database

Frontend and backend run as separate processes/services for development.

### Prerequisites

- Docker
- Docker Compose

### First-time setup

Copy the example environment file:

```sh
cp .env.example .env
```

Start the development environment

```sh
docker compose up --build
```

### Service Urls

- Frontend: [http://localhost:5173](http://localhost:5173)
- Backend API: [http://localhost:8000](http://localhost:8000)
- Backend API docs: [http://localhost:8000/docs](http://localhost:8000/docs)

### Stop the environment

```sh
docker compose down
```

### Hot reload

Source code is mounted into the containers:

- changes under frontend/ trigger Vite hot reload
- changes under backend/ trigger FastAPI reload

### Configuration

- The frontend talks to the backend through `VITE_API_BASE_URL`
- The backend talks to the database through `PT_DATABASE_URL`
- Environment variables can be changed in `.env`
