default:
  just --list tools

backend-format:
    cd backend && uv run black .

backend-lint:
    cd backend && uv run ruff check .

backend-lint-fix:
    cd backend && uv run ruff check . --fix

backend-typecheck:
    cd backend && uv run mypy app

frontend-format:
    cd frontend && npm run format

frontend-lint:
    cd frontend && npm run lint

frontend-lint-fix:
    cd frontend && npm run lint:fix

frontend-typecheck:
    cd frontend && npm run typecheck

format: backend-format frontend-format

lint: backend-lint frontend-lint

typecheck: backend-typecheck frontend-typecheck

check: lint typecheck
