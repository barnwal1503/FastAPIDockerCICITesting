from fastapi.responses import JSONResponse
from sqlalchemy import text

from src.db.redis import redis_client
from src.db.session import engine


def health() -> JSONResponse:
    checks = {}

    try:
        with engine.connect() as conn:
            conn.execute(text("SELECT 1"))
        checks["postgres"] = "ok"
    except Exception as exc:
        checks["postgres"] = f"error: {exc.__class__.__name__}"

    try:
        redis_client.ping()
        checks["redis"] = "ok"
    except Exception as exc:
        checks["redis"] = f"error: {exc.__class__.__name__}"

    healthy = all(value == "ok" for value in checks.values())
    return JSONResponse(checks, status_code=200 if healthy else 503)
