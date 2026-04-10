from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy import text
from sqlmodel import Session

from app.infrastructure.persistence import database, get_session

router = APIRouter(prefix="/health", tags=["health"])


@router.get("")
def health_check() -> dict[str, str]:
    return {"status": "ok"}

@router.get("/db")
def database_health(session: Session = Depends(get_session)) -> dict[str, str]:
    if not database.check_db_connection():
        raise HTTPException(status_code=503, detail="Database unavailable")
    else:
        return {"status": "ok"}
