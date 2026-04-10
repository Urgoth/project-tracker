# Backend

## Entrypoint

The application entrypoint is:

- `app/main.py`

Run locally with:

```bash
uv run uvicorn app.main:app --reload
```

## Current Structure

```txt
app/
  api/
    routes/          # HTTP route handlers
  infrastructure/
    config/          # Settings and runtime configuration
    persistence/     # Database engine, sessions, model base conventions
  main.py            # FastAPI bootstrap and app creation
```

## Intended target Structure

```txt
app/
  api/
    routes/          # Route modules grouped by API area
    schemas/         # Request/response DTOs
  application/
    services/        # App-level orchestration services
    use_cases/       # Business use-case entrypoints
  domain/
    models/          # Domain entities/value objects
    rules/           # Pure business rules and policies
  infrastructure/
    persistence/     # Database/repository implementations
    config/          # Settings/configuration
  main.py            # App bootstrap
```

## Configuration

The backend uses environment variables for configuration.

### Setup

Copy the example file:

```bash
cp .env.example .env
```

Adjust values if needed.

### Application runtime settings

Application settings are loaded via `app.infrastructure.config.settings`.

Supported variables:

```env
PT_APP_ENV=DEVELOP
PT_DEBUG=true
PT_API_HOST=localhost
PT_API_PORT=8789

PT_DATABASE_URL=postgresql+psycopg://project_tracker:project_tracker@db:5432/project_tracker
PT_POSTGRES_DB=project_tracker
PT_POSTGRES_USER=project_tracker
PT_POSTGRES_PASSWORD=project_tracker

PT_CORS_ALLOWED_ORIGINS=http://localhost:5173,http://127.0.0.1:5173
```

Logging

Logging is configured separately via `app.infrastructure.config.logger` to avoid circular dependencies.

Supported variables:

```env
PT_LOG_LEVEL=DEBUG
PT_LOG_DIR=/tmp/project-tracker/logs
```

### Notes

- Application runtime settings are loaded via `app.infrastructure.config.settings`
- Logging is configured separately via environment variables in `app.infrastructure.config.logger`
- Invalid application config fails at startup
- CORS is configurable for frontend-backend communication
- Logging writes to console and file

## Persistence

Database integration lives under `app.infrastructure.persistence`.

It provides:

- SQLModel engine setup
- session dependency for FastAPI routes/services
- shared model conventions
- database connectivity checks

Current development target is PostgreSQL via Docker Compose.
