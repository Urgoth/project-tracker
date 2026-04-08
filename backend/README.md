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
