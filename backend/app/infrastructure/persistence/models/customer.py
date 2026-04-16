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
    from .project import Project


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
