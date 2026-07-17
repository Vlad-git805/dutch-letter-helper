from fastapi import Request, status
from fastapi.responses import JSONResponse

from app.ai.exceptions import AIClientError


async def ai_client_error_handler(
    request: Request,
    exc: AIClientError,
) -> JSONResponse:
    return JSONResponse(
        status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
        content={
            "detail": "AI service is temporarily unavailable. Please try again later."
        },
    )