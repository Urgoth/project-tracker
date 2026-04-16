---
title: Architecture Documentation
last reviewed: 2026-04-16
---

???+ note
    - This section describes the __intended architecture__, not only the current implementation
    - Some parts are still evolving and marked as `draft` or `planned`

## Purpose

Describe the structure and design of the system.

This section provides:

- high-level system understanding
- separation of responsibilities
- core technical decisions
- guidance for future evolution

---

## Architecture Areas

<div class="grid cards" markdown>

- :material-sitemap:{ .lg .middle } __System Overview__

    ---

    High-level architecture of the system.

    Covers frontend, backend, and infrastructure interaction.

    [:octicons-arrow-right-24: Open](./system-overview.md)

- :material-server:{ .lg .middle } __Backend__

    ---

    Structure and responsibilities of the backend.

    Covers API layer, application logic, and persistence.

    [:octicons-arrow-right-24: Open](./backend-overview.md)

- :material-monitor:{ .lg .middle } __Frontend__

    ---

    Structure and responsibilities of the frontend.

    Covers UI architecture and API integration.

    [:octicons-arrow-right-24: Open](./frontend-overview.md)

- :material-database:{ .lg .middle } __Data Model__

    ---

    Overview of core entities and relationships.

    Describes the domain structure and evolution.

    [:octicons-arrow-right-24: Open](./data-model.md)

- :material-api:{ .lg .middle } __API & Client Contract__

    ---

    Interaction between backend API and frontend client.

    Covers OpenAPI usage and client generation.

    [:octicons-arrow-right-24: Open](./api-and-client-contract.md)

- :material-test-tube:{ .lg .middle } __Testing Strategy__

    ---

    Testing approach across the system.

    Defines unit, integration, and system tests.

    [:octicons-arrow-right-24: Open](./testing-strategy.md)

</div>

---

## Design Principles

The system follows a small set of core principles:

### Separation of Concerns

- frontend handles presentation and interaction
- backend handles business logic and persistence
- API defines the contract between both

---

### Simplicity First

- minimal complexity in v1
- avoid premature abstractions
- prefer explicit over implicit behavior

---

### API-Driven Development

- backend exposes a clear API contract
- frontend integrates via generated client
- OpenAPI schema is a first-class artifact

---

### Extensibility

- system is structured to allow future extensions
- domain, services, and API are modular
- plugin system is a future goal

---

### Future Readiness

- architecture supports later multi-user scenarios
- deployment can evolve from local to distributed
- database choice can evolve if needed

---

## Decision Handling

Architectural decisions are documented inline in relevant documents.

Typical format:

```md
### Decision: <short title>

Context:
- ...

Decision:
- ...

Rationale:
- ...
```

This keeps decisions close to the implementation they affect.
