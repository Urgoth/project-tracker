---
title: Frontend Overview
status: draft
last reviewed: 2026-04-16
---

???+ note
    - structure is intentionally simple
    - will evolve with features and UI complexity
    - avoid introducing heavy state management early

## Responsibilities

The frontend is responsible for:

- rendering the user interface
- handling user interaction
- managing UI state
- communicating with the backend API

It is **not responsible for core business logic**.

---

## Technology

- Vite
- TypeScript
- Vue

---

## API Integration

- backend exposes OpenAPI schema
- frontend uses generated client ([hey-api](https://heyapi.dev/))
- API is the only integration boundary

Implications:

- no direct coupling to backend internals
- client must be regenerated when API changes
- generated code should not be manually modified

---

## State & Logic

Guidelines:

- keep business logic in backend
- frontend handles:

    - UI state
    - presentation logic
    - user interaction flows

---

## Development Model

- runs as separate dev server (`npm run dev`)
- communicates with backend over HTTP
- supports fast iteration via hot reload
