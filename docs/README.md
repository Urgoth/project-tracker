---
title: Project Tracker Documentation
last reviewed: 2026-04-16
---

!!! warning
    This documentation is being actively rebuilt and refined.

## Purpose

This documentation provides a structured overview of the **project-tracker** system for developers and technical contributors.

## Documentation Structure

<div class="grid cards" markdown>

- :lucide-landmark:{ .lg .middle } **Architecture**

    ---

    System design, structure, and technical decisions.

    Covers system overview, backend/frontend architecture, data model, API contract, and testing strategy.

    [:octicons-arrow-right-24: Open](./architecture/README.md)

- :material-tools:{ .lg .middle } **Development**

    ---

    Everything needed to work on the codebase.

    Includes local setup, repository structure, workflows, migrations, API client generation, and tooling.

    [:octicons-arrow-right-24: Open](./development/README.md)

- :material-api:{ .lg .middle } **API**

    ---

    Backend API structure and OpenAPI usage.

    Describes API conventions and how the frontend integrates via the generated client.

    [:octicons-arrow-right-24: Open](./api/README.md)

- :material-clipboard-text:{ .lg .middle } **Project**

    ---

    Internal planning and project management.

    Roadmap, milestones, and planning-related documentation.

    [:octicons-arrow-right-24: Open](./project/README.md)

- :material-account:{ .lg .middle } **User Guide (Planned)**

    ---

    End-user documentation is not yet implemented.

    Will include product overview, getting started, and usage guides.

    [:octicons-arrow-right-24: Open](./user-guide/README.md)

</div>

---

## Conventions

### Document Status

Each document contains metadata:

- `authoritative` — accurate and actively maintained
- `draft` — partially complete or evolving
- `planned` — placeholder for future content

---

### Scope of Documentation

This documentation reflects:

- the **current implementation**
- the **intended architecture direction**
- planned workflows where relevant

Some areas are intentionally incomplete and marked as `planned`.

---

### Diagrams and Assets

Diagrams are stored under:

```text
docs/assets/diagrams/
````

Guidelines:

- Prefer **Mermaid** for diagrams (native integration)
- Store source files alongside rendered output if needed
- Organize by category:

    - architecture
    - workflows
    - data-model
    - testing

---

## Related Information

- Root project README: [`../README.md`](../README.md)
- Source code:

    - backend: `../backend/`
    - frontend: `../frontend/`
