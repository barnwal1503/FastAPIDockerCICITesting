import redis

from src.core.config import get_settings

settings = get_settings()

redis_client = redis.Redis(
    host=settings.redis_host,
    port=settings.redis_port,
    db=settings.redis_db,
    password=settings.redis_password,
    socket_timeout=3,
    socket_connect_timeout=3,
    decode_responses=True,
)
