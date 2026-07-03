# ADR 001 - Use FastAPI

## Status

Accepted

## Context

The project requires a modern Python web framework for building a REST API.

The framework should:

- be easy to learn;
- provide automatic request validation;
- generate API documentation;
- have good performance;
- be suitable for AI applications.

## Decision

Use FastAPI as the backend framework.

## Why

FastAPI provides:

- automatic request validation with Pydantic;
- automatic OpenAPI (Swagger) documentation;
- excellent performance;
- strong type hint support;
- modern Python architecture.

## Consequences

### Positive

- Fast development.
- Built-in API documentation.
- Easy integration with AI services.
- Large community.

### Negative

- Requires understanding of type hints and dependency injection.
- Slightly steeper learning curve than Flask.