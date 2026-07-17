from fastapi import FastAPI

from app.ai.exceptions import AIClientError
from app.api.health import router as health_router
from app.api.letters import router as letters_router
from app.core.exception_handlers import ai_client_error_handler
from app.core.settings import settings


app = FastAPI(title=settings.APP_NAME)

app.add_exception_handler(
    AIClientError,
    ai_client_error_handler,
)

app.include_router(health_router)
app.include_router(letters_router)