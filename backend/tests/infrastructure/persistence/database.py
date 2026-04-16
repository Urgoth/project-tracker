from collections.abc import Generator

from sqlmodel import Session, SQLModel, create_engine

from app.infrastructure.config.settings import get_settings

settings = get_settings()

engine = create_engine(
    settings.database_url,
    echo=settings.debug,
    pool_pre_ping=True,
)


def get_session() -> Generator[Session, None, None]:
    with Session(engine) as session:
        yield session


def init_db() -> None:
    SQLModel.metadata.create_all(engine)


def check_db_connection() -> None:
    with Session(engine) as session:
        session.exec("SELECT 1")
