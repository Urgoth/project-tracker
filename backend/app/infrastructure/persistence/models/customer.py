from typing import List, Optional
from enum import Enum
from pydantic import BaseModel
from sqlmodel import Field, Relationship
from ..base import TimestampedModel, UUIDPrimaryKeyModel
from .project import Project

class CustomerType(str, Enum):
    INDIVIDUAL = "individual"
    CORPORATE = "corporate"
    GOVERNMENT = "government"
    NON_PROFIT = "non_profit"

class Customer(UUIDPrimaryKeyModel, TimestampedModel, BaseModel, table=True):
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
