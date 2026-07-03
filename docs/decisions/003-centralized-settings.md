# ADR 003

## Decision

Use pydantic-settings for application configuration.

## Why

Avoid using os.getenv() throughout the project.

Create one centralized configuration object.

## Consequences

Cleaner architecture.

Easier maintenance.

Safer configuration management.