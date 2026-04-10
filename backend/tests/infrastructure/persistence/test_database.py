from fastapi import HTTPException
import pytest
from sqlmodel import Session
from fastapi.testclient import TestClient

from app.main import app
from app.infrastructure.config.settings import Settings
from app.infrastructure.persistence.database import get_session

def test_settings_load_postgres_database_url(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv(
        "PT_DATABASE_URL",
        "postgresql+psycopg://user:pass@db:5432/project_tracker",
    )

    settings = Settings()

    assert settings.database_url == "postgresql+psycopg://user:pass@db:5432/project_tracker"

def test_get_session_yields_session() -> None:
    generator = get_session()
    session = next(generator)

    try:
        assert isinstance(session, Session)
    finally:
        session.close()
        generator.close()

def test_health_db_endpoint_exists() -> None:
    client = TestClient(app)
    response = client.get("/health/db")

    assert response.status_code in {200, 503}

def test_health_db_returns_ok(monkeypatch) -> None:
    from app.infrastructure.persistence import database

    def fake_check_db_connection() -> bool:
        return True

    monkeypatch.setattr(database, "check_db_connection", fake_check_db_connection)

    client = TestClient(app)
    response = client.get("/health/db")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}

def test_health_db_returns_503_on_failure(monkeypatch) -> None:
    from app.infrastructure.persistence import database

    def fake_check_db_connection() -> None:
        raise HTTPException(status_code=503, detail="Database unavailable")

    monkeypatch.setattr(database, "check_db_connection", fake_check_db_connection)

    client = TestClient(app)
    response = client.get("/health/db")

    assert response.status_code == 503
