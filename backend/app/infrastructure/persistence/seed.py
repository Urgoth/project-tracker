from sqlmodel import Session, text

from app.infrastructure.persistence.database import engine
from app.infrastructure.persistence.models import (
    Customer,
    CustomerType,
    Project,
    ProjectStatus,
)
import structlog

logger = structlog.get_logger(__name__)


def seed_test_data() -> None:
    with Session(engine) as session:
        # prevent duplicate seeding
        existing = session.exec(text("SELECT 1 FROM customer LIMIT 1")).first()
        if existing:
            return

        # customers
        c1 = Customer(name="Acme Corp", customer_type=CustomerType.CORPORATE)
        c2 = Customer(name="City Council", customer_type=CustomerType.GOVERNMENT)

        session.add_all([c1, c2])
        session.flush()  # ensures IDs available

        # projects
        p1 = Project(
            name="Internal Tool",
            description="Build internal dashboard",
            status=ProjectStatus.ACTIVE,
            priority=2,
            customer_id=c1.id,
        )

        p2 = Project(
            name="Website Redesign",
            description="Modernize public website",
            status=ProjectStatus.PLANNING,
            priority=3,
            customer_id=c1.id,
        )

        p3 = Project(
            name="Permit System",
            description="Digitize permit workflow",
            status=ProjectStatus.ACTIVE,
            priority=1,
            customer_id=c2.id,
        )

        session.add_all([p1, p2, p3])
        session.commit()
