from contextlib import asynccontextmanager

import structlog
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.router import api_router
from app.infrastructure.config.logger import setup_logger
from app.infrastructure.config.settings import get_settings

logger = structlog.get_logger(__name__)
settings = get_settings()

app = FastAPI()

# Define the lifespan
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 1. Startup: This runs BEFORE the app starts taking requests
    logger = structlog.get_logger(__name__)
    logger.info("logging_initialized", status="success")

    yield

    # 2. Shutdown: This runs when the app is stopping
    logger.info("logging_shutting_down")

def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        debug=settings.debug,
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins_list(),
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(api_router)
    return app

app = create_app()
