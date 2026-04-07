---
title: Project Tracker — Architecture Description
---
## 1. Architecture Overview

`project-tracker` is designed as a **containerized client-server web application** for solo developers and small teams.

The system consists of:

* a **Vue-based frontend** for the user interface
* a **FastAPI backend** exposing a REST API
* a **relational database** for persistent storage
* a future-oriented architecture that supports:

  * extensibility via plugins
  * later multi-user support
  * optional external integrations

The frontend and backend are deployed together in a **single Docker container** for v1 to keep setup and operation simple.

---

## 2. Architectural Goals

The architecture is driven by the following goals:

### 2.1 Simplicity

The first version must be easy to run, easy to develop, and easy to understand.

### 2.2 Clear Separation of Concerns

The UI, API, domain logic, and persistence must be clearly separated so that the system remains maintainable.

### 2.3 Extensibility

The core system must be structured so that plugins can later extend:

* data model
* business logic
* UI behavior

### 2.4 Future Multi-User Readiness

Even though v1 is single-user, the system should not be architected as a purely local or monolithic desktop-style app. A proper client-server split prepares the system for later shared deployments.

### 2.5 Good UX

The architecture must support a responsive UI, clear navigation, and efficient data loading for dashboards and planning views.

---

## 3. System Style

The system follows a **modular layered architecture**:

* **Presentation layer**

  * Vue frontend
  * views, components, routing, state handling

* **API layer**

  * FastAPI routes
  * OpenAPI schema generation
  * request/response validation

* **Application layer**

  * use cases / services
  * orchestration of domain operations

* **Domain layer**

  * core entities and business rules
  * planning hierarchy
  * requirements model
  * link/resource model

* **Persistence layer**

  * relational database
  * repositories / data access layer

This separation ensures that the domain model is not tightly coupled to the frontend, API transport format, or database implementation.

## 4. Deployment Model

### v1 Deployment

The system is deployed as a **single Docker container** containing two application processes:

* a **FastAPI backend process**
* a **Vue frontend process**

The frontend communicates with the backend over HTTP using the backend API endpoint inside the container/network setup.

This approach keeps deployment simple while preserving a clean separation between:

* frontend implementation
* backend implementation
* API contract

### Rationale

The frontend is intentionally **not served from FastAPI**.

This avoids:

* coupling UI delivery to backend internals
* mixing frontend concerns into backend implementation
* muddying the application structure early

This also keeps the client-server architecture explicit from the beginning, which supports future deployment changes.

### Future Deployment Evolution

Later versions may split deployment further into:

* standalone frontend container
* standalone backend container
* external database
* reverse proxy / TLS termination
* optional authentication provider integration

The v1 structure should not block that evolution.

## 5. Frontend Architecture

### Runtime Model

The frontend runs as a **separate Vue application process**.

It accesses the backend via HTTP, for example through a local API address such as:

* `localhost:<api-port>` in development or simple deployments
* an internal service name or reverse-proxy route in later deployments

### Design Consequence

The frontend is a real client of the backend API, not just a UI layer embedded into the backend server.

This has several advantages:

* clean separation of responsibilities
* better frontend independence
* easier future hosting flexibility
* clearer API-driven development

### API Integration

The backend’s OpenAPI schema is used to generate TypeScript API bindings for the frontend.

Benefits:

* reduced duplicate API definitions
* stronger type safety between frontend and backend
* better maintainability when the API evolves

### Frontend Responsibilities

The frontend is responsible for:

* project navigation
* dashboard views
* planning/timeline presentation
* requirements views
* notes editing
* resource link management
* user interaction and state presentation

### Frontend Design Principle

Business rules should not live primarily in the frontend.
The frontend should remain focused on:

* presentation
* interaction
* lightweight UI state

Core business behavior should remain in backend/domain logic.

---

## 6. Backend Architecture

### Technology Choice

The backend is implemented with **FastAPI**.

Reasons:

* strong Python ecosystem
* good developer productivity
* automatic OpenAPI generation
* clean request/response validation
* good foundation for modular service design

### Backend Responsibilities

The backend is responsible for:

* exposing REST endpoints
* validating and processing requests
* executing use cases
* enforcing business rules
* managing persistence
* preparing extension points for plugins

### Boundary Clarification

The FastAPI backend exposes the API only.

It does **not** serve or embed the frontend UI.

Its responsibility is limited to:

* API delivery
* request validation
* application services
* domain logic
* persistence access
* future extension/plugin support

This keeps the backend implementation focused and easier to maintain.

### Internal Backend Structure

A recommended internal structure is:

```text
backend/
  api/
    routes/
    schemas/
  application/
    services/
    use_cases/
  domain/
    models/
    rules/
    events/
  infrastructure/
    persistence/
    plugins/
    integrations/
  main.py
```

This structure keeps technical concerns separate from domain concerns.

---

## 7. Core Domain Model

The system is centered around a small set of core entities.

### 7.1 Project

Represents a managed software project.

Main attributes:

* id
* name
* description
* tags
* notes
* status (optional/simple)
* created/updated timestamps

### 7.2 ResourceLink

Represents an external reference related to a project.

Main attributes:

* id
* project_id
* title
* url
* category
* description (later)

### 7.3 Requirement

Represents a tracked requirement or feature.

Main attributes:

* id
* project_id
* title
* description
* status

Requirements are intentionally separate from planning items, but linkable to them.

### 7.4 WorkItem

The planning system is centered around an abstract **WorkItem** concept.

A work item represents any schedulable planning element in the system.

The MVP defines three work item types:

* Milestone
* Work Package
* Task

Each work item belongs to a project and may optionally belong to another work item via a parent-child relationship.

This allows flexible hierarchical planning without requiring separate dependency handling for each entity type.

Typical examples:

* milestone contains work packages
* work package contains tasks
* tasks may also exist standalone when no work package is needed

### 7.5 WorkItem Attributes

A work item should support:

* id
* project_id
* parent_work_item_id (optional)
* type
* name
* description
* planned start date
* planned end date
* current start date
* current end date
* effort estimate
* responsible person
* status

### 7.6 WorkItem Dependencies

Dependencies are modeled between work items.

Each work item may have:

* 0 or more predecessors
* 0 or more successors

This allows dependencies between:

* milestone and milestone
* milestone and work package
* milestone and task
* work package and work package
* work package and task
* task and task

Dependencies are independent of the containment hierarchy.

### 7.7 Requirement Links

Requirements remain a separate domain concept.

A requirement always belongs to a project and may optionally be linked to one or more work items.

This allows lightweight traceability between:

* project goals
* requirements
* implementation planning

### 7.8 Notes

For v1, notes are a simple markdown blob attached to the project.

---

## 8. Planning Model Considerations

The planning model is one of the most important parts of the system.

### 8.1 Hierarchy

Because planning is hierarchical, the domain must support:

* parent-child relations
* ordering among siblings
* aggregation across hierarchy levels

### 8.2 Status Model

The MVP status model is intentionally lightweight:

* todo
* in progress
* done
* behind schedule

This keeps the planning system useful without turning it into a full ticket tracker.

### 8.3 Timeline / Gantt View

The domain and API must expose enough structured scheduling data to render:

* start/end dates
* hierarchy
* dependencies

### 8.4 Milestone Trend Analysis

The system must preserve enough information to compare:

* originally planned dates
* current dates

This implies the model should distinguish between:

* baseline/planned values
* current/updated values

Even if the trend analysis stays simple in v1, the data model should support it explicitly.

---

## 9. Persistence Architecture

## 9.1 Database Style

A **relational database** is the recommended choice.

Reasoning:

* the domain is structured and relational
* hierarchy and linking are important
* requirements, planning entities, dependencies, and resource links fit naturally into relational modeling
* later multi-user support also fits well with a relational design

## 9.2 Initial Database Recommendation

For v1, the most pragmatic choice is **SQLite**.

Why SQLite fits v1:

* embedded and simple
* works well in a single-container deployment
* low operational overhead
* good fit for single-user or low-concurrency scenarios

## 9.3 Future Database Evolution

When the system moves toward:

* stronger multi-user support
* larger deployments
* more concurrent access

it should be possible to migrate to **PostgreSQL**.

Therefore, the persistence layer should be designed so that:

* business logic does not depend directly on SQLite-specific behavior
* SQLAlchemy or another abstraction layer can support migration later

---

## 10. API Design

The backend exposes a REST API for the frontend.

### API Principles

* resource-oriented endpoints
* clear separation by domain
* validated request/response schemas
* predictable and stable shapes for frontend code generation

### Example endpoint groups

* `/projects`
* `/projects/{id}`
* `/projects/{id}/links`
* `/projects/{id}/requirements`
* `/projects/{id}/planning`
* `/milestones`
* `/work-packages`
* `/tasks`

### API Contract Strategy

The OpenAPI schema is treated as a first-class artifact.
The frontend client should be generated from it.

This improves:

* consistency
* type safety
* development speed

---

## 11. Extensibility Architecture

Extensibility is a core design goal and must influence the architecture from the start.

### 11.1 Plugin Goals

Plugins should eventually be able to extend:

* domain data
* business logic
* UI elements
* integrations with external systems

### 11.2 v1 Approach

v1 should not implement a full plugin runtime yet.
Instead, it should prepare for extensibility by introducing:

* modular domain boundaries
* service interfaces
* repository abstractions
* internal extension points
* event or hook concepts where useful

### 11.3 Important Constraint

The core system should remain useful and understandable without plugins.
Plugins should extend the system, not define its essential behavior.

---

## 12. User and Collaboration Readiness

### v1 Authentication

There is **no authentication in v1**.

The first release is intended for controlled single-user deployment scenarios, where access is managed operationally rather than inside the application.

### Future Authentication Strategy

Authentication is expected to be introduced later at the deployment boundary, for example through:

* TLS / HTTP termination layer
* OAuth2-based authentication

This means the application does not need to implement full authentication in v1.

### Authorization Implications

Even without authentication in v1, the architecture should avoid making authorization impossible later.

Therefore:

* domain and service boundaries should remain compatible with future user context
* ownership and permission concepts should be introducible without major refactoring

### Practical Interpretation

For v1:

* no login screen
* no identity management
* no role model

For v1.x and later:

* authorization should be designed once user identity becomes available through external authentication infrastructure

---

## 13. Recommended Backend Module Boundaries

A useful domain/module split for v1 is:

* `projects`
* `planning`
* `requirements`
* `resources`
* `notes`
* `plugins` (internal groundwork only)

This provides a clean path for later growth.

---

## 14. Recommended MVP Technical Decisions

### Backend

* Python
* FastAPI
* Pydantic
* SQLAlchemy or SQLModel
* Alembic for migrations

### Frontend

* Vue
* TypeScript
* generated API client from OpenAPI
* separate frontend runtime/process

### Deployment

* single Docker container for v1
* two separate processes inside the container:

  * frontend
  * backend

### Authentication

* none in v1
* prepare for external auth later

### Database

* SQLite first
* PostgreSQL-compatible architecture later

---

## 15. Risks and Trade-Offs

### 15.1 Single Container vs Separation

A single container is simpler for v1, but care must be taken not to entangle frontend and backend too tightly.

### 15.2 SQLite Limitations

SQLite is ideal for simplicity, but later multi-user or concurrent deployments may require PostgreSQL.

### 15.3 Plugin Ambition

A plugin system that extends data and logic is powerful, but it can complicate the domain model if introduced too early. The architecture should prepare for it without overbuilding v1.

### 15.4 Planning Complexity

Hierarchical planning, dependencies, Gantt rendering, and milestone trend analysis make planning the most complex part of the MVP.

---

## 16. Architectural Summary

`project-tracker` should be built as a modular containerized web application with:

* **Vue frontend**
* **FastAPI backend**
* **relational persistence**
* **SQLite for v1**
* **clean module boundaries**
* **plugin-ready architecture**
* **future support for multi-user and external integrations**

This architecture balances:

* simple deployment
* clean UX
* maintainability
* future extensibility
