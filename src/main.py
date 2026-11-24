from collections.abc import AsyncIterator
from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.core.config import get_settings
from src.core.exceptions import register_exception_handlers
from src.db.redis import redis_client
from src.db.session import engine
from src.routes import router


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    yield
    engine.dispose()
    redis_client.close()


def create_app() -> FastAPI:
    settings = get_settings()
    app = FastAPI(title=settings.app_name, lifespan=lifespan)

    register_exception_handlers(app)

    app.include_router(router)

    return app


app = create_app()
