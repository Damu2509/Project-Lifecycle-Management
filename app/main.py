from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api_router import router
from app.core.logger import get_logger
from app.shared.constants import APP_DESCRIPTION, APP_TITLE, APP_VERSION

logger = get_logger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting %s v%s", APP_TITLE, APP_VERSION)
    yield
    logger.info("Shutting down %s", APP_TITLE)


app = FastAPI(
    title=APP_TITLE,
    description=APP_DESCRIPTION,
    version=APP_VERSION,
    lifespan=lifespan,
)

app.include_router(router)
