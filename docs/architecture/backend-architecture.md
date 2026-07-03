# Backend Architecture

## Current Architecture

                Browser
                    │
                    ▼
              FastAPI Router
                    │
                    ▼
             LetterService
                    │
                    ▼
               AI Client
                    │
                    ▼
             OpenAI SDK
                    │
                    ▼
              OpenAI API

## Responsibilities

### Api/

Responsible for HTTP requests.

### Services/

Business logic.

### Ai/

Communication with OpenAI.

### Schemas/

Request and Response models.

### Core/

Application configuration.

### Utils/

Helper functions.

### Request Flow

Client

↓

FastAPI Router

↓

LetterService

↓

AIClient

↓

OpenAI API

↓

AIClient

↓

LetterService

↓

Router

↓

JSON Response

### Dependency Direction

Router

↓

Service

↓

AI Client

↓

OpenAI SDK

### Project Structure

backend/
├── app/
│   ├── api/
│   ├── ai/
│   ├── core/
│   ├── models/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   └── main.py
├── .env.example
└── requirements.txt