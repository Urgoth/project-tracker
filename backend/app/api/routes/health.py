from datetime import datetime, UTC
from fastapi import APIRouter, Depends, HTTPException
from sqlmodel import Session
from pydantic import BaseModel

from app.infrastructure.persistence import database, get_session

router = APIRouter(prefix="/health", tags=["health"])


class HealthResponse(BaseModel):
    status: str
    service: str
    timestamp: str


@router.get("", response_model=HealthResponse)
def health_check() -> HealthResponse:
    return HealthResponse(
        status="ok",
        service="project-tracker-backend",
        timestamp=datetime.now(UTC).isoformat(),
    )


@router.get("/db")
def database_health(session: Session = Depends(get_session)) -> dict[str, str]:
    if not database.check_db_connection():
        raise HTTPException(status_code=503, detail="Database unavailable")
    else:
        return {"status": "ok"}
