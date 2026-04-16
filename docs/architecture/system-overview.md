---
title: System Overview
status: draft
last reviewed: 2026-04-16
---

## High-Level Architecture

```mermaid
flowchart LR
    Client --> Frontend
    Frontend -->|HTTP API| Backend
    Backend --> Database

    subgraph Docker Environment
        Frontend
        Backend
        Database
    end
```

---

## Components

### Frontend

- Runs as a separate development server
- Provides user interface
- Communicates with backend via HTTP API
- Uses generated API client based on OpenAPI

Responsibilities:

- presentation
- user interaction
- UI state

---

### Backend

- FastAPI application
- Exposes REST API
- Implements business logic
- Handles persistence

Responsibilities:

- request validation
- application logic
- domain logic
- database access

---

### Database

- Relational database
- Used for persistent storage

Responsibilities:

- store structured project data
- support relationships between entities

---

## Development Runtime Model

In development, components run separately:

- Docker Compose:
    - database and infrastructure
- Backend:
    - local process (`uvicorn`)
- Frontend:
    - local dev server (`vite`)

```mermaid
flowchart LR
    subgraph Host Machine
        Frontend["Frontend Dev Server"]
        Backend["Backend (uvicorn)"]
    end

    subgraph Docker
        Database[(Database)]
    end

    Frontend -->|HTTP| Backend
    Backend --> Database
```

---

## Communication Flow

```mermaid
sequenceDiagram
    actor User
    participant Frontend
    participant Backend
    participant Database

    User->>Frontend: Interact with UI
    Frontend->>Backend: Send HTTP request
    Backend->>Database: Read or write data
    Database-->>Backend: Return result
    Backend-->>Frontend: Return HTTP response
    Frontend-->>User: Update visible UI state
```

---

## API Integration

- Backend exposes OpenAPI schema
- Frontend uses generated client
- API is the single integration boundary

Implications:

- no shared business logic between frontend and backend
- contract must remain stable
- changes require client regeneration

---

## Deployment Considerations (Planned)

Future deployment may include:

- separate containers for frontend and backend
- reverse proxy (routing, TLS)
- external database
- authentication layer
