---
title: API & Client Contract
status: draft
last reviewed: 2026-04-16
---

???+ note
    - workflow is still evolving
    - tooling and automation may be improved later

## Core Idea

The backend API is the **single integration boundary** between frontend and backend.

- frontend communicates only via HTTP API
- backend exposes a structured contract
- no shared business logic between both

---

## OpenAPI Schema

- backend automatically exposes an OpenAPI schema
- schema defines:
    - endpoints
    - request/response models
    - types

The schema is treated as a **first-class artifact**.

---

## Client Generation

- frontend uses a generated API client (`hey-api`)
- client is generated from the OpenAPI schema

Location:

```text
frontend/src/api/client/generated/
````

Generated artifacts include:

- request functions
- type definitions
- client utilities

---

## Workflow

Typical flow:

1. Modify backend API (routes, schemas)
2. Backend updates OpenAPI schema
3. Regenerate frontend client
4. Use updated client in frontend

---

## Rules

- do not manually edit generated client code
- treat generated files as disposable
- keep schema and client in sync

---

## Implications

- strong typing between frontend and backend
- reduced duplication of API definitions
- safer refactoring of API
