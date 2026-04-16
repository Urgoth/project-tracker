from datetime import date
from enum import Enum
from typing import Optional
from uuid import UUID

from sqlmodel import Field, Relationship, SQLModel

from .base import TimestampedModel, UUIDPrimaryKeyModel
from .links import RequirementWorkItemLink

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .project import Project
    from .requirement import Requirement


class WorkItemType(str, Enum):
    MILESTONE = "milestone"
    WORK_PACKAGE = "work_package"
    TASK = "task"


class WorkItemStatus(str, Enum):
    DRAFT = "draft"
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    IN_REVIEW = "in_review"
    DONE = "done"
    BEHIND_SCHEDULE = "behind_schedule"


class WorkItem(UUIDPrimaryKeyModel, TimestampedModel, SQLModel, table=True):
    project_id: UUID = Field(foreign_key="project.id", index=True, nullable=False)
    parent_work_item_id: Optional[UUID] = Field(
        default=None, foreign_key="workitem.id", index=True
    )

    type: WorkItemType = Field(nullable=False, index=True)
    name: str = Field(nullable=False, index=True)
    description: Optional[str] = Field(default=None)

    planned_start_date: Optional[date] = Field(default=None, index=True)
    planned_end_date: Optional[date] = Field(default=None, index=True)
    current_start_date: Optional[date] = Field(default=None, index=True)
    current_end_date: Optional[date] = Field(default=None, index=True)

    effort_estimate_hours: Optional[float] = Field(default=None)
    responsible_person: Optional[str] = Field(default=None)

    status: WorkItemStatus = Field(default=WorkItemStatus.TODO, index=True)
    sort_order: int = Field(default=0, nullable=False)

    project: "Project" = Relationship(back_populates="work_items")

    parent: Optional["WorkItem"] = Relationship(
        back_populates="children",
        sa_relationship_kwargs={"remote_side": "WorkItem.id"},
    )
    children: list["WorkItem"] = Relationship(back_populates="parent")

    requirements: list["Requirement"] = Relationship(
        back_populates="work_items",
        link_model=RequirementWorkItemLink,
    )
