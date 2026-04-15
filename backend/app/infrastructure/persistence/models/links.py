from __future__ import annotations

from uuid import UUID

from sqlmodel import Field, SQLModel


class RequirementWorkItemLink(SQLModel, table=True):
    requirement_id: UUID = Field(
        foreign_key="requirement.id", primary_key=True, nullable=False
    )
    work_item_id: UUID = Field(
        foreign_key="workitem.id", primary_key=True, nullable=False
    )


class ProjectCustomerLink(SQLModel, table=True):
    project_id: UUID = Field(foreign_key="project.id", primary_key=True, nullable=False)
    customer_id: UUID = Field(
        foreign_key="customer.id", primary_key=True, nullable=False
    )
