from fastapi import FastAPI

from app.api.health import router as health_router
from app.api.letters import router as letters_router

app = FastAPI(
    title="Dutch Letter Helper API",
    version="0.1.0"
)

app.include_router(health_router)
app.include_router(letters_router)