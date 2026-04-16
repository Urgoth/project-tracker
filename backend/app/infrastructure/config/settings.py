from functools import lru_cache
from typing import List
import structlog

from pydantic import Field, field_validator, model_validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from enum import Enum


class Environment(str, Enum):
    DEVELOP = "DEVELOP"
    TEST = "TEST"
    PROD = "PROD"


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
        env_prefix="PT_",
    )

    app_name: str = "project-tracker"
    app_env: Environment = Environment.DEVELOP
    debug: bool = False

    api_host: str = "localhost"
    api_port: int = 8789

    postgres_db: str = "project_tracker"
    postgres_user: str = "project_tracker"
    postgres_password: str = "project_tracker"
    database_url: str = Field(
        default="postgresql+psycopg://project_tracker:project_tracker@db:5432/project_tracker",
    )
    cors_allowed_origins: str = Field(
        default="http://localhost:5173,http://127.0.0.1:5173",
    )

    @field_validator("api_host")
    @classmethod
    def validate_api_host(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("API host must not be empty")
        return value

    @field_validator("api_port")
    @classmethod
    def validate_api_port(cls, value: int) -> int:
        if not 1 <= value <= 65535:
            raise ValueError("API port must be between 1 and 65535")
        return value

    @field_validator("database_url")
    @classmethod
    def validate_database_url(cls, value: str) -> str:
        value = value.strip()
        if not value:
            raise ValueError("Database URL must not be empty")
        return value

    @field_validator("cors_allowed_origins")
    @classmethod
    def validate_cors_allowed_origins(cls, value: str) -> str:
        origins = [origin.strip() for origin in value.split(",") if origin.strip()]
        if not origins:
            raise ValueError("CORS_ALLOWED_ORIGINS must contain at least one origin")
        return ",".join(origins)

    @model_validator(mode="after")
    def validate_production_safety(self) -> "Settings":
        if self.app_env == Environment.PROD and self.debug:
            raise ValueError("DEBUG must be false in PROD")
        return self

    def cors_origins_list(self) -> list[str]:
        return [
            origin.strip()
            for origin in self.cors_allowed_origins.split(",")
            if origin.strip()
        ]


@lru_cache
def get_settings() -> Settings:
    settings = Settings()
    if settings.debug:
        logger = structlog.get_logger()
        logger.debug("loaded settings", settings=settings.model_dump())
    return settings
