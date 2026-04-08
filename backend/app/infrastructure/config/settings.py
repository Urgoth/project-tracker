from functools import lru_cache
from typing import List

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )

    app_name: str = "project-tracker"
    app_env: str = "development"
    debug: bool = True
    database_url: str = Field(
        default="postgresql+psycopg://project_tracker:project_tracker@db:5432/project_tracker",
        alias="DATABASE_URL",
    )
    cors_allowed_origins: str = Field(
        default="http://localhost:5173",
        alias="CORS_ALLOWED_ORIGINS",
    )

    def cors_origins_list(self) -> List[str]:
        return [origin.strip() for origin in self.cors_allowed_origins.split(",") if origin.strip()]


@lru_cache
def get_settings() -> Settings:
    return Settings()
