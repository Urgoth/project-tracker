---
title: Testing Strategy
status: draft
last reviewed: 2026-04-16
---

???+ note
    - test tooling may differ between backend and frontend
    - exact test layout is not fixed yet
    - CI execution strategy will be documented later

## Purpose

Describe how the system should be tested at different levels.

The strategy is intentionally simple and will evolve with the project.

---

## Test Levels

The project distinguishes between three test levels:

- unit tests
- integration tests
- system tests

---

## Unit Tests

Unit tests verify isolated parts of the system.

Typical scope:

- backend domain logic
- backend services
- frontend components
- frontend utility functions

Goals:

- fast feedback
- focused failure causes
- low setup overhead

---

## Integration Tests

Integration tests verify collaboration between selected parts of the system.

Typical scope:

- API endpoint + application logic + persistence
- frontend API integration
- migration workflow against a real database
- selected cross-module behavior

Goals:

- verify boundaries
- catch wiring/configuration issues
- test realistic behavior without running the full system

---

## System Tests

System tests verify the behavior of the full system as a whole.

Typical scope:

- build images
- start environment with Compose
- execute end-to-end checks against running services

Goals:

- verify deployment-relevant behavior
- validate frontend-backend integration
- catch environment and configuration issues

---

## Practical Guidance

Use:

- **unit tests** for isolated logic
- **integration tests** for interactions between a few parts
- **system tests** for full-stack verification

Prefer more unit and integration tests than system tests.
System tests are valuable, but usually slower and more expensive to maintain.

---

## Current Direction

The intended test split is:

- backend unit tests
- frontend unit tests
- backend/frontend integration tests where useful
- full system tests via built containers and Compose

Implementation details are still evolving.
