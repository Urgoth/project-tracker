from typing import List, Optional
from enum import Enum
from uuid import UUID

from sqlmodel import Field, Relationship, SQLModel, table
from .base import TimestampedModel, UUIDPrimaryKeyModel # Assuming base.py is in the same dir
from datetime import datetime

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
    customer: Optional["Customer"] = Relationship(back_populates="projects")

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
        description="Categorization for reporting and billing logic"
    )
    
    # Internal Metadata
    is_active: bool = Field(default=True, index=True)
    internal_notes: Optional[str] = Field(default=None)

    # Relationships
    # This links the customer to their various projects
    projects: List["Project"] = Relationship(back_populates="customer")
