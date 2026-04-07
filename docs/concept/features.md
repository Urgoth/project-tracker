---
title: Feature List & Prioritization
---

## Multi-Project Overview

### MVP

* List all projects
* Basic project cards:

  * name
  * short description
  * status (optional/simple)
* Create / delete project
* Navigate to project dashboard

### v1.x

* Search projects
* Filter (status, tags)

### later

* Project grouping
* Favorites / pinning

## Project Dashboard

### MVP

* Central project view
* Display:

  * project name
  * description
  * notes (preview)
  * key links (repo, docs)
  * planning summary:

    * milestones overview
    * timeline snapshot
    * basic progress indication
* Quick navigation to sub-sections

### v1.x

* Customizable dashboard layout

### later

* Widget system (plugin-based)

## Project Metadata

### MVP

* Name
* Description
* Tags (optional)
* Notes (markdown blob)

### v1.x

* Custom fields

### later

* Schema customization via plugins

## Resource Linking

### MVP

* Add/edit/remove links:

  * repository
  * documentation
  * arbitrary URLs
* Categorize links (repo, docs, misc)

### v1.x

* Link grouping
* Link descriptions

### later

* Smart links (metadata, previews via plugins)

## Planning & Scheduling

### Core Model (important design decision)

Hierarchical planning structure:

* Project

  * Sub-project (optional)

    * Milestones

      * Work Packages (aggregation level)

        * Tasks (lowest level)

### MVP

#### Structure

* Create and manage:

  * milestones
  * work packages
  * tasks
* Hierarchical relationships:

  * nesting of sub-projects (optional)
  * milestones → work packages → tasks

#### Attributes (for work packages & tasks)

* name
* description
* start date
* end date
* duration
* effort estimation (hours)
* responsible person
* dependencies (between work packages/tasks)

#### Visualization (included in MVP)

* Timeline view (Gantt-like)
* Milestone trend analysis (simple):

  * planned vs current dates
  * basic deviation indication

### v1.x

* Progress tracking (manual % or status)
* Improved timeline interactions
* Aggregation logic (rollups from tasks → work packages → milestones)

### later

* Advanced scheduling logic
* Auto-adjustments based on dependencies
* Scenario planning
* External integrations (plugins)

## Requirements & Feature Tracking

### Design Decision

Requirements and planning entities are **separate systems**, but **linkable**.

### MVP

* Create requirements/features
* Attributes:

  * title
  * description
  * status (open/done)
* Link requirements to:

  * project
  * work packages (optional)

### v1.x

* Requirement hierarchy (parent/child)
* Tagging

### later

* Full traceability:

  * requirements ↔ work packages ↔ implementation ↔ external issues
* Integration with external systems (plugins)

## Notes & Custom Information

### MVP

* Single markdown note per project
* Used for:

  * free-form documentation
  * project-specific context

### v1.x

* Structured sections within notes

### later

* Multiple documents per project
* Rich content blocks (plugin-based)

## UX & Navigation

### MVP

* Clean, minimal UI
* Fast navigation:

  * homepage → project → sections
* Consistent layout structure
* Focus on:

  * clarity
  * speed

### v1.x

* Keyboard navigation
* Quick actions

### later

* Advanced customization (themes, layouts)

## Extensibility (Plugin System)

### Key Direction

Plugins can extend:

* data model
* business logic
* UI

### MVP

* ❗ Internal architecture prepared for extensibility:

  * modular domain structure
  * clear extension points (conceptual, not exposed yet)

### v1.x

* Basic plugin system:

  * custom fields / data extensions
  * UI extensions

### later

* Full plugin ecosystem:

  * integrations (GitLab, GitHub)
  * custom widgets
  * automation
  * domain extensions

## User & Collaboration Model

### MVP

* Single-user system

### v1.x

* Introduce user entity
* Ownership model

### later

* Full collaboration:

  * roles/permissions
  * shared projects
