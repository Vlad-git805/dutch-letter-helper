# ADR 002 - Use Service Layer

## Status

Accepted

## Context

Business logic should not be placed directly inside FastAPI routers.

As the application grows, the same business logic may be used by:

- REST API;
- CLI tools;
- background jobs;
- scheduled tasks;
- future integrations.

## Decision

Move all business logic into the Service Layer.

Routers are responsible only for handling HTTP requests and responses.

## Why

This separates responsibilities.

- Router handles HTTP.
- Service contains business logic.
- AI Client communicates with AI.
- Schemas define data structures.

## Consequences

### Positive

- Cleaner architecture.
- Easier testing.
- Better scalability.
- Easier maintenance.
- Lower coupling.

### Negative

- More files.
- Slightly more initial complexity.