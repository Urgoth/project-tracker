from __future__ import annotations

from enum import Enum
from typing import Optional
from uuid import UUID

from sqlmodel import Field, Relationship, SQLModel

from .base import TimestampedModel, UUIDPrimaryKeyModel

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .project import Project


class ResourceLinkCategory(str, Enum):
    REPOSITORY = "repository"
    DOCUMENTATION = "documentation"
    MISC = "misc"


class ResourceLink(UUIDPrimaryKeyModel, TimestampedModel, SQLModel, table=True):
    project_id: UUID = Field(foreign_key="project.id", index=True, nullable=False)

    title: str = Field(nullable=False, index=True)
    description: Optional[str] = Field(default=None)
    url: str = Field(nullable=False)
    category: ResourceLinkCategory = Field(default=ResourceLinkCategory.MISC)

    sort_order: int = Field(default=0, nullable=False)

    project: "Project" = Relationship(back_populates="resource_links")
