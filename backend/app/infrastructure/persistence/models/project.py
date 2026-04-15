from __future__ import annotations

from datetime import datetime
from enum import Enum
from typing import Optional
from .links import ProjectCustomerLink

from sqlmodel import Field, Relationship, SQLModel

from .base import (
    TimestampedModel,
    UUIDPrimaryKeyModel,
)

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .resource_link import ResourceLink
    from .requirement import Requirement
    from .workitem import WorkItem


class ProjectStatus(str, Enum):
    PLANNING = "planning"
    ACTIVE = "active"
    ON_HOLD = "on_hold"
    COMPLETED = "completed"
    CANCELLED = "cancelled"


class Project(UUIDPrimaryKeyModel, TimestampedModel, SQLModel, table=True):
    # Note: created_at and updated_at are inherited from TimestampedModel
    # Note: id (UUID) is inherited from UUIDPrimaryKeyModel
    # Core Information
    name: str = Field(index=True, nullable=False)
    description: Optional[str] = Field(default=None)

    # foundation metadata
    tags: Optional[str] = Field(
        default=None,
        description="Optional lightweight tag storage. Can later evolve into normalized tags.",
    )
    notes: Optional[str] = Field(
        default=None, description="Markdown notes blob attached to project."
    )

    # Status and Metadata
    status: ProjectStatus = Field(default=ProjectStatus.PLANNING)
    priority: int = Field(default=3, description="Priority scale 1-5")

    # Timeline
    # We use Optional[datetime] for deadlines to allow 'forever' projects
    deadline: Optional[datetime] = Field(default=None)
    is_archived: bool = Field(default=False, index=True)

    # relations
    customers: list["Customer"] = Relationship(
        back_populates="projects",
        link_model=ProjectCustomerLink,
    )
    resource_links: list["ResourceLink"] = Relationship(back_populates="project")
    requirements: list["Requirement"] = Relationship(back_populates="project")
    work_items: list["WorkItem"] = Relationship(back_populates="project")


class CustomerType(str, Enum):
    INDIVIDUAL = "individual"
    CORPORATE = "corporate"
    GOVERNMENT = "government"
    NON_PROFIT = "non_profit"


class Customer(UUIDPrimaryKeyModel, TimestampedModel, SQLModel, table=True):
    # Core Identity
    name: str = Field(index=True, nullable=False)

    # Classification
    customer_type: CustomerType = Field(
        default=CustomerType.CORPORATE,
        description="Categorization for reporting and billing logic",
    )

    # Internal Metadata
    is_active: bool = Field(default=True, index=True)
    internal_notes: Optional[str] = Field(default=None)

    # Relationships
    # This links the customer to their various projects
    projects: list["Project"] = Relationship(
        back_populates="customers",
        link_model=ProjectCustomerLink,
    )
