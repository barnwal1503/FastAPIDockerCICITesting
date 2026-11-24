from functools import lru_cache
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict
from sqlalchemy import URL

SECRETS_DIR = Path("/run/secrets")


class Settings(BaseSettings):
    # Priority: environment variable > .env file > Docker secret file > default
    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
        secrets_dir=SECRETS_DIR if SECRETS_DIR.is_dir() else None,
    )

    app_name: str = "FastAPI Portfolio"
    environment: str = "development"

    postgres_user: str = "app"
    postgres_password: str
    postgres_db: str = "appdb"
    postgres_host: str = "localhost"
    postgres_port: int = 5432

    db_pool_size: int = 5
    db_max_overflow: int = 10
    db_pool_timeout: int = 30
    db_echo: bool = False

    redis_password: str
    redis_host: str = "localhost"
    redis_port: int = 6379
    redis_db: int = 0

    @property
    def database_url(self) -> str:
        return URL.create(
            "postgresql+psycopg",
            username=self.postgres_user,
            password=self.postgres_password,
            host=self.postgres_host,
            port=self.postgres_port,
            database=self.postgres_db,
        ).render_as_string(hide_password=False)


@lru_cache
def get_settings() -> Settings:
    return Settings()
