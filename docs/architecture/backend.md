---
title: Backend Overview
status: draft
last reviewed: 2026-04-16
---

???+ note
    - structure is still evolving
    - avoid over-engineering early
    - introduce layering gradually as complexity grows

## Responsibilities

The backend is responsible for:

- exposing a REST API
- validating and processing requests
- executing application logic
- managing persistence

It is the **single source of truth** for business logic.

---

## Technology

- FastAPI
- Pydantic (validation)
- SQLModel / SQLAlchemy (persistence)
- Alembic (migrations)

## Layers (Conceptual)

The backend follows a layered approach:

- **API layer**
    - routes
    - request/response schemas
- **Application layer**
    - use cases
    - orchestration logic
- **Domain layer**
    - core entities
    - business rules
- **Infrastructure layer**
    - database access
    - external integrations

This separation is a guideline and not strictly enforced yet.

---

## API

- REST-based
- OpenAPI schema is automatically generated
- serves as contract for frontend integration

---

## Persistence

- relational database
- schema managed via Alembic migrations
