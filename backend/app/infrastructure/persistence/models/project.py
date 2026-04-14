from typing import Optional
from enum import Enum
from uuid import UUID

from pydantic import BaseModel
from app.infrastructure.persistence.models.customer import Customer
from sqlmodel import Field, Relationship
from ..base import TimestampedModel, UUIDPrimaryKeyModel # Assuming base.py is in the same dir
from datetime import datetime

class ProjectStatus(str, Enum):
    PLANNING = "planning"
    ACTIVE = "active"
    ON_HOLD = "on_hold"
    COMPLETED = "completed"
    CANCELLED = "cancelled"

class Project(UUIDPrimaryKeyModel, TimestampedModel, BaseModel, table=True):
    # Note: created_at and updated_at are inherited from TimestampedModel
    # Note: id (UUID) is inherited from UUIDPrimaryKeyModel
    # Core Information
    name: str = Field(index=True, nullable=False)
    description: Optional[str] = Field(default=None)
    
    # Status and Business Logic
    status: ProjectStatus = Field(default=ProjectStatus.PLANNING)
    priority: int = Field(default=3, description="Priority scale 1-5")
    
    # Timeline
    # We use Optional[datetime] for deadlines to allow 'forever' projects
    deadline: Optional[datetime] = Field(default=None)
    is_archived: bool = Field(default=False, index=True)

    # Foreign Key to Customer
    customer_id: Optional[UUID] = Field(
        default=None, 
        foreign_key="customer.id", 
        index=True
    )
    
    # Relationship back to Customer
    customer: Optional[Customer] = Relationship(back_populates="projects")

