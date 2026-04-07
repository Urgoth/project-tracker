---
title: Scope Definition
---

## In Scope (v1)

* Multi-project homepage/dashboard
* Individual project dashboards
* Project metadata:

  * name
  * description
  * notes
* Manual linking of external resources:

  * Git repositories
  * documentation
* Lightweight planning:

  * milestones
  * work packages
  * start/end dates
  * duration
  * effort estimation (hours)
  * dependencies
  * responsible person
* Requirements and feature tracking (basic)
* Storage of structured internal data
* Clean, fast, and minimal UX

## Out of Scope (v1)

The following are explicitly excluded:

* External tool integrations (e.g. GitLab/GitHub APIs)
* Full task management systems (e.g. Jira-like functionality)
* Issue tracking replacement
* CI/CD management
* Deep analytics or reporting
* Complex enterprise workflows

## Non-Goals

This tool does **not aim to replace**:

* Ticketing systems (e.g. Jira, GitLab Issues)
* Full project management suites
* Version control platforms

Instead, it acts as:

> A lightweight, structured overview and planning companion.

## Integration Strategy

**v1:**

* Manual linking only (URLs, references)

**Future:**

* API-based integrations (e.g. GitLab/GitHub)
* Likely implemented as **plugins/extensions**

## Data Philosophy

* The system stores **its own structured project data**
* External systems are:

  * **referenced, not replicated**
  * used as sources of detailed information

This ensures:

* independence from external systems
* flexibility in linking any resource

## UX Principles

Priority order:

1. **Clarity**

   * Minimal, understandable interfaces
   * No unnecessary visual noise

2. **Speed**

   * Fast navigation and access to information
   * Efficient workflows

3. **Aesthetics**

   * Clean, modern UI
   * Developer-friendly design

## Key Design Constraint

> The system must remain simple at its core, while allowing extensibility for
advanced use cases.
