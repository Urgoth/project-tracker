---
title: Roadmap
---

## Roadmap Strategy

The project will be developed using **vertical slices**.

This means each milestone delivers a coherent, usable feature across:

- data model
- backend logic
- API
- frontend UI

This approach is preferred because it:

- keeps progress visible
- reduces integration risk
- validates architecture early
- supports iterative UX refinement

## Milestone 0 — Foundation

### Goal

Create the technical and structural foundation for development.

### Scope

- Repository setup refinement
- Basic project structure for:
    - FastAPI backend
    - Vue frontend
- Docker-based local development setup
- Database setup with migrations
- OpenAPI-based frontend client generation
- Basic architecture documentation
- Mermaid diagram integration in docs

### Deliverables

- runnable container/dev environment
- backend/frontend skeleton
- database migration pipeline
- initial documentation structure

### Definition of Done

- frontend and backend run as separate processes
- frontend can call backend successfully
- database migrations work
- documentation structure is committed

---

## Milestone 1 — Project Core Slice

### Goal

Implement the minimum usable project management core.

### Scope

- Create project
- Edit project metadata
- Delete project
- List projects on homepage
- Navigate to project dashboard
- Basic project dashboard shell
- Markdown notes blob per project

### Deliverables

- homepage with project overview
- project detail/dashboard page
- project CRUD API
- notes editing and display

### Definition of Done

- user can create and open projects
- user can edit metadata and notes
- dashboard displays stored project data

---

## Milestone 2 — Resource Links Slice

### Goal

Make the project dashboard practically useful by linking external resources.

### Scope

- Add/edit/remove resource links

- Resource categories:
    - repo
    - docs
    - misc
- Display links on dashboard

### Deliverables

- resource link data model
- resource link API
- frontend management UI
- dashboard integration

### Definition of Done

- user can attach important links to a project
- dashboard becomes useful as a central project hub

---

## Milestone 3 — Planning Core Slice

### Goal

Introduce structured planning entities and relationships.

### Scope

- Milestones
- Work packages
- Tasks
- Optional parent project hierarchy
- Optional standalone tasks
- Optional task assignment to work package and/or milestone
- Minimal status tracking:
    - todo
    - in progress
    - done
    - behind schedule

### Deliverables

- planning data model
- CRUD API for milestones, work packages, tasks
- frontend views for planning entities
- project dashboard planning summary

### Definition of Done

- user can model project planning structure
- planning items are visible and editable
- dashboard shows planning summary

---

## Milestone 4 — Timeline & Dependencies Slice

### Goal

Make planning visual and connected.

### Scope

- Gantt-like timeline view
- Planning dependencies between:
    - milestones
    - work packages
    - tasks
- milestone trend analysis (simple)

### Deliverables

- dependency model
- timeline UI
- trend visualization
- API support for aggregated planning view

### Definition of Done

- user can define dependencies
- user can inspect planning on a timeline
- user can see milestone deviation from baseline

---

## Milestone 5 — Requirements Slice

### Goal

Add lightweight requirements tracking and connect it to planning.

### Scope

- create/edit/delete requirements
- link requirements to projects
- optionally link requirements to work packages/tasks
- requirement status:
    - open
    - done

### Deliverables

- requirements data model
- requirements API
- requirements UI
- cross-linking with planning items

### Definition of Done

- user can track requirements separately from planning
- requirements can be associated with implementation work

---

## Milestone 6 — UX Consolidation Slice

### Goal

Improve clarity, speed, and usability of the MVP.

### Scope

- dashboard refinement
- better navigation
- improved project overview
- planning view usability improvements
- consistency pass across UI

### Deliverables

- polished MVP UX
- reduced friction in core workflows
- improved information density without clutter

### Definition of Done

- core workflows feel coherent
- navigation is efficient
- UI reflects the product vision clearly

---

## Milestone 7 — Extensibility Foundation

### Goal

Prepare the system for future plugin support without shipping a full plugin ecosystem yet.

### Scope

- formalize extension points in backend
- identify data model extension strategy
- identify UI extension strategy
- internal plugin architecture groundwork

### Deliverables

- documented extension points
- first internal extensibility interfaces
- architectural validation for plugin direction

### Definition of Done

- extension strategy is implemented at the architectural level
- future plugin work does not require major redesign

---

## Post-MVP / v1.x

### Likely next features

- search and filtering
- custom fields
- manual progress percentages
- aggregation/rollup logic
- ownership model
- authorization concepts
- improved planning interactions

---

## Later / Long-Term

### Future capabilities

- plugin runtime
- external integrations
- OAuth2-based authenticated deployments
- multi-user collaboration
- PostgreSQL deployment option
- advanced scheduling logic
- full traceability between requirements and implementation artifacts

---

## Recommended implementation order inside each slice

For each milestone, use this order:

1. domain model
2. database migration
3. backend service/use case
4. API endpoint
5. generated frontend client
6. frontend view/components
7. dashboard integration
8. documentation update

This keeps slices disciplined and reduces drift between backend and frontend.

---

## Risks to monitor

### Planning complexity

Planning is the most complex part of the MVP and should be introduced incrementally.

### Timeline UI complexity

Gantt-like visualization can become expensive early if overbuilt.

### Dependency flexibility

Cross-type dependencies are powerful but require careful validation rules.

### Plugin ambition

The plugin vision is valuable, but implementation must not destabilize the MVP.
