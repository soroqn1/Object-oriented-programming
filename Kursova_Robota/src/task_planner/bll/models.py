
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
from uuid import uuid4, UUID
from datetime import datetime

class Priority:
    Low = "Low"
    Medium = "Medium"
    High = "High"
    Critical = "Critical"
    choices = {Low, Medium, High, Critical}

class TaskStatus:
    Todo = "Todo"
    InProgress = "InProgress"
    Done = "Done"
    Canceled = "Canceled"
    Overdue = "Overdue"
    choices = {Todo, InProgress, Done, Canceled, Overdue}

@dataclass
class Member:
    first_name: str
    last_name: str
    email: Optional[str] = None
    capacity_per_day: Optional[float] = None
    id: UUID = field(default_factory=uuid4)

@dataclass
class TaskItem:
    title: str
    description: Optional[str] = None
    priority: str = Priority.Medium
    status: str = TaskStatus.Todo
    progress: int = 0
    start_at: Optional[datetime] = None
    due_at: Optional[datetime] = None
    id: UUID = field(default_factory=uuid4)

@dataclass
class Assignment:
    task_id: UUID
    member_id: UUID
    allocated_hours: float
    id: UUID = field(default_factory=uuid4)

@dataclass
class ProjectState:
    total: int
    done: int
    active: int
    overdue: int
    by_member_load: dict
