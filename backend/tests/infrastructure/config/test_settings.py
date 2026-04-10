import logging

import pytest
from pydantic import ValidationError

from app.infrastructure.config.settings import Environment, Settings, get_settings


def clear_settings_cache() -> None:
    get_settings.cache_clear()


@pytest.fixture(autouse=True)
def reset_settings_cache():
    clear_settings_cache()
    yield
    clear_settings_cache()


def test_settings_load_with_defaults():
    settings = Settings()

    assert settings.app_name == "project-tracker"
    assert settings.app_env == Environment.DEVELOP
    assert settings.debug is False
    assert settings.api_host == "localhost"
    assert settings.api_port == 8789
    assert settings.database_url == (
        "postgresql+psycopg://project_tracker:project_tracker@db:5432/project_tracker"
    )
    assert settings.cors_origins_list() == [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ]


def test_settings_read_environment_variables(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("PT_APP_ENV", "TEST")
    monkeypatch.setenv("PT_DEBUG", "true")
    monkeypatch.setenv("PT_API_HOST", "127.0.0.1")
    monkeypatch.setenv("PT_API_PORT", "9000")
    monkeypatch.setenv(
        "PT_DATABASE_URL",
        "sqlite:///./project-tracker.db",
    )
    monkeypatch.setenv(
        "PT_CORS_ALLOWED_ORIGINS",
        "http://localhost:4173,http://127.0.0.1:4173",
    )

    settings = Settings()

    assert settings.app_env == Environment.TEST
    assert settings.debug is True
    assert settings.api_host == "127.0.0.1"
    assert settings.api_port == 9000
    assert settings.database_url == "sqlite:///./project-tracker.db"
    assert settings.cors_origins_list() == [
        "http://localhost:4173",
        "http://127.0.0.1:4173",
    ]


@pytest.mark.parametrize("value", [0, 70000])
def test_invalid_api_port_raises_validation_error(value: int, monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("PT_API_PORT", str(value))

    with pytest.raises(ValidationError) as exc_info:
        Settings()

    assert "api_port" in str(exc_info.value)


def test_empty_database_url_raises_validation_error(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("PT_DATABASE_URL", "")

    with pytest.raises(ValidationError) as exc_info:
        Settings()

    assert "database_url" in str(exc_info.value)


def test_empty_cors_origins_raises_validation_error(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("PT_CORS_ALLOWED_ORIGINS", "")

    with pytest.raises(ValidationError) as exc_info:
        Settings()

    assert "cors_allowed_origins" in str(exc_info.value)


def test_invalid_app_env_raises_validation_error(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("PT_APP_ENV", "LOCAL")

    with pytest.raises(ValidationError) as exc_info:
        Settings()

    assert "app_env" in str(exc_info.value)


def test_prod_with_debug_enabled_raises_validation_error(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv("PT_APP_ENV", "PROD")
    monkeypatch.setenv("PT_DEBUG", "true")

    with pytest.raises(ValidationError) as exc_info:
        Settings()

    assert "DEBUG must be false in PROD" in str(exc_info.value)


def test_cors_origins_are_trimmed(monkeypatch: pytest.MonkeyPatch):
    monkeypatch.setenv(
        "CORS_ALLOWED_ORIGINS",
        " http://localhost:5173 , http://127.0.0.1:5173 ",
    )

    settings = Settings()

    assert settings.cors_origins_list() == [
        "http://localhost:5173",
        "http://127.0.0.1:5173",
    ]


def test_get_settings_is_cached():
    first = get_settings()
    second = get_settings()

    assert first is second
