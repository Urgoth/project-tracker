---
title: Architecture Diagrams
---

## 1. System Context Diagram

### Purpose

Shows how `project-tracker` interacts with users and external systems.

```mermaid
flowchart LR
    U[User / Developer / Team Member]

    PT[Project Tracker]

    GR[Git Repositories]
    DOC[Documentation Systems]
    URL[Other External Resources]

    OAUTH[OAuth2 Provider<br/>future]
    PLUG[Integration Plugins<br/>future]

    U --> PT
    PT -->|links only| GR
    PT -->|links only| DOC
    PT -->|links only| URL

    PT -. future .-> OAUTH
    PT -. future .-> PLUG
```

---

## 2. Container Diagram

### Purpose

Shows internal runtime structure and communication.

### Key Decisions Reflected

* Separate frontend and backend processes
* Single container deployment in v1
* SQLite embedded for v1

```mermaid
flowchart LR
    USER[User]

    subgraph BROWSER[Browser]
        FEAPP[Vue App]
    end

    subgraph CONTAINER[Docker Container]
        FE[Frontend Process<br/>Vue]
        BE[Backend Process<br/>FastAPI]
        DB[(SQLite DB)]
    end

    USER --> FEAPP
    FEAPP --> FE
    FE -->|HTTP/REST API| BE
    BE -->|SQL| DB
```

---

## 3. Domain Model Diagram

### Purpose

Defines the core data model and relationships in a more abstract way.

### Key Design Decisions Reflected

* project hierarchy via `parent_project_id`
* abstract `WorkItem` model
* `Milestone`, `WorkPackage`, and `Task` are work item types
* dependencies are modeled uniformly between work items
* requirements are separate from planning, but may link to both projects and work items

```mermaid
classDiagram
    class Project {
        +id
        +name
        +description
        +parent_project_id
        +notes
        +tags
    }

    class WorkItem {
        +id
        +project_id
        +parent_work_item_id
        +type
        +name
        +description
        +planned_start
        +planned_end
        +current_start
        +current_end
        +effort_hours
        +responsible
        +status
    }

    class Requirement {
        +id
        +project_id
        +title
        +description
        +status
    }

    class ResourceLink {
        +id
        +project_id
        +title
        +url
        +category
    }

    class WorkItemDependency {
        +id
        +predecessor_work_item_id
        +successor_work_item_id
        +dependency_type
    }

    class RequirementWorkItemLink {
        +id
        +requirement_id
        +work_item_id
    }

    Project "1" --> "0..*" Project : parent/child
    Project "1" --> "0..*" WorkItem
    Project "1" --> "0..*" Requirement
    Project "1" --> "0..*" ResourceLink

    WorkItem "1" --> "0..*" WorkItem : parent/child
    WorkItem "1" --> "0..*" WorkItemDependency : predecessor
    WorkItem "1" --> "0..*" WorkItemDependency : successor

    Requirement "1" --> "0..*" RequirementWorkItemLink
    WorkItem "1" --> "0..*" RequirementWorkItemLink
```

---

# Recommended interpretation

## `WorkItem.type`

Use an enum-like field:

* `milestone`
* `work_package`
* `task`

That keeps the data model flexible while still allowing specialized logic in backend services and frontend views.

## `parent_work_item_id`

Use this for containment/hierarchy between work items.

This allows:

* milestone → work package
* work package → task
* milestone → task, if needed
* future extensions, if your model evolves

You may still enforce business rules later so not every combination is allowed.

## `WorkItemDependency`

This cleanly expresses:

* any work item may have 0..* predecessors
* any work item may have 0..* successors

That matches your real-world dependency requirement much better than separate dependency handling by entity type.

## `RequirementWorkItemLink`

This keeps requirements separate from planning while allowing traceability.

So a requirement can be linked to:

* its project directly
* optionally one or more work items

---

## 4. Sequence Diagram — Open Project Dashboard

### Purpose

Shows how data flows when a user opens a project dashboard.

```mermaid
sequenceDiagram
    actor U as User
    participant FE as Vue Frontend
    participant BE as FastAPI Backend
    participant DB as SQLite DB

    U->>FE: Open Project Dashboard
    FE->>BE: GET /projects/{id}/dashboard

    BE->>DB: Fetch project metadata
    BE->>DB: Fetch resource links
    BE->>DB: Fetch milestones/work packages/tasks summary
    BE->>DB: Fetch requirements summary

    DB-->>BE: Return data
    BE->>BE: Aggregate dashboard response
    BE-->>FE: JSON dashboard payload

    FE->>FE: Render dashboard
    FE-->>U: Show project dashboard
```
