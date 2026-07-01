# Backend Architecture

## Current Architecture

```text
Browser
    │
    ▼
FastAPI Router
    │
    ▼
LetterService
    │
    ├────────────► prompts.py
    │
    ▼
AIClient
    │
    ▼
(OpenAI - coming soon)
```

## Responsibilities

### api/

HTTP layer.

Receives requests and returns responses.

### services/

Business logic.

Knows how to analyze Dutch letters.

### ai/

Responsible for communication with AI providers.

### prompts.py

Stores AI prompts.

### client.py

Communicates with AI providers.

### core/

Application configuration.