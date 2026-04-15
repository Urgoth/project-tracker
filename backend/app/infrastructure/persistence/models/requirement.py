from __future__ import annotations

from enum import Enum
from typing import Optional
from uuid import UUID

from sqlmodel import Field, Relationship, SQLModel

from .base import TimestampedModel, UUIDPrimaryKeyModel
from .links import RequirementWorkItemLink

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .project import Project
    from .workitem import WorkItem


class RequirementStatus(str, Enum):
    DRAFT = "draft"
    OPEN = "open"
    DONE = "done"


class Requirement(UUIDPrimaryKeyModel, TimestampedModel, SQLModel, table=True):
    project_id: UUID = Field(foreign_key="project.id", index=True, nullable=False)

    title: str = Field(nullable=False, index=True)
    description: Optional[str] = Field(default=None)
    status: RequirementStatus = Field(default=RequirementStatus.OPEN, index=True)

    project: "Project" = Relationship(back_populates="requirements")

    work_items: list["WorkItem"] = Relationship(
        back_populates="requirements",
        link_model=RequirementWorkItemLink,
    )
