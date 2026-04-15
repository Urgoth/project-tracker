from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlmodel import Session, select
from sqlalchemy.orm import selectinload
from typing import List, Optional

from app.infrastructure.persistence import get_session
from app.infrastructure.persistence.models import Project, ProjectStatus

router = APIRouter(prefix="/projects", tags=["health"])


@router.get("/projects", response_model=List[Project], operation_id="listProjects")
def list_projects(
    offset: int = 0,
    limit: int = Query(default=100, le=100),
    status: Optional[ProjectStatus] = None,
    session: Session = Depends(get_session),
):
    """
    Retrieves a list of projects with optional filtering and pagination.
    """
    statement = select(Project).offset(offset).limit(limit)

    if status:
        statement = statement.where(Project.status == status)

    projects = session.exec(statement).all()
    return projects


@router.get("/projects/{project_id}", response_model=Project, operation_id="getProject")
def get_project(project_id: UUID, session: Session = Depends(get_session)):
    """
    Retrieves a project by UUID, including its associated customers and work items.
    """
    # Create the selection statement
    statement = (
        select(Project)
        .where(Project.id == project_id)
        .options(
            selectinload(Project.customers),  # type: ignore
            selectinload(Project.work_items),  # type: ignore
        )
    )

    # Execute the query
    results = session.exec(statement)
    project = results.first()

    if not project:
        raise HTTPException(status_code=404, detail="Project not found")

    return project


@router.post("/projects", response_model=Project, operation_id="createProject")
def create_project(project: Project, session: Session = Depends(get_session)):
    """
    Creates a new project.
    """
    session.add(project)
    session.commit()
    session.refresh(project)
    return project
