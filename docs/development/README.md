---
title: Development Documentation
last reviewed: 2026-04-16
---

## Purpose

Entry point for all development-related workflows.

Use this section for:

- setting up the local environment
- understanding repository structure
- working on backend and frontend
- running migrations
- generating API clients
- using development tooling

---

## Development Areas

<div class="grid cards" markdown>

- :material-play-circle:{ .lg .middle } __Local Setup__

    ---

    Get the system running locally.

    Covers prerequisites, environment configuration, and startup via Docker/Compose.

    [:octicons-arrow-right-24: Open](./local-setup.md)

- :material-file-tree:{ .lg .middle } __Repository Structure__

    ---

    Overview of the project layout.

    Explains backend, frontend, docs, and supporting files.

    [:octicons-arrow-right-24: Open](./repository-structure.md)

- :material-server:{ .lg .middle } __Backend Development__

    ---

    Working on the FastAPI backend.

    Includes running the app, tests, and conventions.

    [:octicons-arrow-right-24: Open](./backend-development.md)

- :material-monitor:{ .lg .middle } __Frontend Development__

    ---

    Working on the frontend application.

    Covers dev server, API usage, and project structure.

    [:octicons-arrow-right-24: Open](./frontend-development.md)

- :material-database:{ .lg .middle } __Migration Workflow__

    ---

    Database schema changes with Alembic.

    Create, review, and apply migrations.

    [:octicons-arrow-right-24: Open](./migration-workflow.md)

- :material-api:{ .lg .middle } __API Client Generation__

    ---

    Generate and update the frontend API client from OpenAPI.

    Defines when and how to regenerate.

    [:octicons-arrow-right-24: Open](./api-client-generation.md)

- :material-tools:{ .lg .middle } __Developer Tooling__

    ---

    Tooling used in development.

    Includes justfile, linting, formatting, and other utilities.

    [:octicons-arrow-right-24: Open](./developer-tooling.md)

</div>

---

## Development Flow

Typical workflow:

1. Start local environment
2. Make changes (backend/frontend)
3. Run tests
4. Apply or create migrations if needed
5. Regenerate API client if API changed

Details for each step are documented in the linked sections.

---

## Testing

Testing strategy is defined in:

→ [`../architecture/testing-strategy.md`](../architecture/testing-strategy.md)

Levels:

- unit tests (backend, frontend)
- integration tests (partial system)
- system tests (full system via containers)

---

## Notes

- Prefer small, incremental changes
- Keep backend and frontend contract in sync
- Do not manually edit generated API client code
