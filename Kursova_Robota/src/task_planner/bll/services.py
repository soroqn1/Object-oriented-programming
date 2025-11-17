
from __future__ import annotations
from typing import Optional
from datetime import datetime
from uuid import UUID

from .models import Member, TaskItem, Assignment, TaskStatus, Priority, ProjectState
from .exceptions import DomainValidationException, EntityNotFoundException, OverAllocationException
from ..dal.repository import IRepository

class MemberService:
    def __init__(self, members: IRepository[Member], assignments: IRepository[Assignment]):
        self.members = members
        self.assignments = assignments

    def add(self, first_name: str, last_name: str, email: str | None, capacity: float | None) -> Member:
        if not first_name or not last_name:
            raise DomainValidationException("First and last name are required.")
        if capacity is not None and capacity <= 0:
            raise DomainValidationException("Capacity must be positive.")
        m = Member(first_name=first_name.strip(), last_name=last_name.strip(), email=email, capacity_per_day=capacity)
        return self.members.add(m)

    def list(self) -> list[Member]:
        return self.members.get_all()

    def update_member(self, member_id: UUID, *, first_name: str | None = None, last_name: str | None = None,
                      email: str | None = None, capacity: float | None = None) -> Member:
        m = self.members.get(member_id)
        if not m:
            raise EntityNotFoundException("Member not found")
        if first_name is not None:
            if not first_name.strip(): raise DomainValidationException("first_name empty")
            m.first_name = first_name.strip()
        if last_name is not None:
            if not last_name.strip(): raise DomainValidationException("last_name empty")
            m.last_name = last_name.strip()
        if email is not None:
            m.email = email.strip() or None
        if capacity is not None:
            if capacity <= 0: raise DomainValidationException("Capacity must be positive")
            m.capacity_per_day = capacity
        self.members.update(m)
        return m

    def delete_member(self, member_id: UUID) -> None:
        if not self.members.get(member_id):
            raise EntityNotFoundException("Member not found")
        # also remove assignments for this member
        for a in list(self.assignments.get_all()):
            if a.member_id == member_id:
                self.assignments.delete(a.id)
        self.members.delete(member_id)

    def find_members(self, keyword: str) -> list[Member]:
        kw = keyword.lower().strip()
        return self.members.find(lambda m: kw in m.first_name.lower() or kw in m.last_name.lower() or (m.email and kw in m.email.lower()))


class TaskService:
    def __init__(self, tasks: IRepository[TaskItem], members: IRepository[Member], assignments: IRepository[Assignment]):
        self.tasks = tasks
        self.members = members
        self.assignments = assignments

    def add(self, title: str, priority: str = Priority.Medium, due_at: datetime | None = None, description: str | None = None) -> TaskItem:
        if not (title and title.strip()):
            raise DomainValidationException("Title is required.")
        if priority not in Priority.choices:
            raise DomainValidationException(f"Invalid priority: {priority}")
        if due_at is not None and due_at.date() < datetime.utcnow().date():
            raise DomainValidationException("Due date must be in the future.")
        t = TaskItem(title=title.strip(), priority=priority, due_at=due_at, description=description)
        return self.tasks.add(t)

    def set_status(self, task_id: UUID, status: str) -> None:
        t = self.tasks.get(task_id)
        if not t:
            raise EntityNotFoundException("Task not found")
        if status not in TaskStatus.choices:
            raise DomainValidationException(f"Invalid status: {status}")
        t.status = status
        if status == TaskStatus.Done:
            t.progress = 100
        self.tasks.update(t)

    def set_progress(self, task_id: UUID, progress: int) -> None:
        if not (0 <= progress <= 100):
            raise DomainValidationException("Progress must be 0..100")
        t = self.tasks.get(task_id)
        if not t:
            raise EntityNotFoundException("Task not found")
        t.progress = progress
        if progress == 100:
            t.status = TaskStatus.Done
        self.tasks.update(t)

    def assign(self, task_id: UUID, member_id: UUID, hours: float) -> Assignment:
        if hours <= 0:
            raise DomainValidationException("Hours must be positive.")
        t = self.tasks.get(task_id)
        if not t:
            raise EntityNotFoundException("Task not found")
        m = self.members.get(member_id)
        if not m:
            raise EntityNotFoundException("Member not found")
        load = sum(a.allocated_hours for a in self.assignments.find(lambda a: a.member_id == member_id))
        if m.capacity_per_day is not None and load + hours > m.capacity_per_day:
            raise OverAllocationException("Member over-allocated for the day.")
        a = Assignment(task_id=task_id, member_id=member_id, allocated_hours=hours)
        return self.assignments.add(a)

    def get_by_status(self, status: str) -> list[TaskItem]:
        return self.tasks.find(lambda t: t.status == status)

    def get_overdue(self, now: datetime | None = None) -> list[TaskItem]:
        now = now or datetime.utcnow()
        return self.tasks.find(lambda t: t.due_at is not None and t.due_at < now and t.status != TaskStatus.Done)

class ReportingService:
    def __init__(self, tasks: IRepository[TaskItem], members: IRepository[Member], assignments: IRepository[Assignment]):
        self.tasks = tasks
        self.members = members
        self.assignments = assignments

    def get_project_state(self) -> ProjectState:
        all_tasks = self.tasks.get_all()
        total = len(all_tasks)
        done = sum(1 for t in all_tasks if t.status == TaskStatus.Done)
        active = sum(1 for t in all_tasks if t.status in (TaskStatus.Todo, TaskStatus.InProgress))
        overdue = len([t for t in all_tasks if t.due_at and t.due_at < datetime.utcnow() and t.status != TaskStatus.Done])
        loads: dict[str, float] = {}
        for a in self.assignments.get_all():
            m = self.members.get(a.member_id)
            key = f"{m.first_name} {m.last_name}" if m else "Unknown"
            loads[key] = loads.get(key, 0.0) + a.allocated_hours
        return ProjectState(total=total, done=done, active=active, overdue=overdue, by_member_load=loads)


class _SortKey:
    @staticmethod
    def for_task(key: str):
        key = (key or "").lower()
        if key == "title":
            return lambda t: t.title.lower()
        if key == "priority":
            order = {"Low":0,"Medium":1,"High":2,"Critical":3}
            return lambda t: order.get(t.priority, 99)
        if key == "due":
            return lambda t: (t.due_at or datetime.max)
        if key == "status":
            return lambda t: t.status
        return lambda t: t.title.lower()

class TaskService(TaskService):  # extend
    def update_task(self, task_id: UUID, *, title: str | None = None, description: str | None = None,
                    priority: str | None = None, due_at: datetime | None = None, status: str | None = None) -> TaskItem:
        t = self.tasks.get(task_id)
        if not t:
            raise EntityNotFoundException("Task not found")
        if title is not None:
            if not title.strip(): raise DomainValidationException("Title empty")
            t.title = title.strip()
        if description is not None:
            t.description = description
        if priority is not None:
            if priority not in Priority.choices: raise DomainValidationException("Invalid priority")
            t.priority = priority
        if due_at is not None:
            if due_at.date() < datetime.utcnow().date(): raise DomainValidationException("Due date must be in the future.")
            t.due_at = due_at
        if status is not None:
            if status not in TaskStatus.choices: raise DomainValidationException("Invalid status")
            t.status = status
            if status == TaskStatus.Done:
                t.progress = 100
        self.tasks.update(t)
        return t

    def delete_task(self, task_id: UUID) -> None:
        if not self.tasks.get(task_id):
            raise EntityNotFoundException("Task not found")
        for a in list(self.assignments.get_all()):
            if a.task_id == task_id:
                self.assignments.delete(a.id)
        self.tasks.delete(task_id)

    # Listing with sort and filters
    def list_tasks(self, *, status: str | None = None, only_overdue: bool | None = None, sort_by: str | None = None) -> list[TaskItem]:
        tasks = self.tasks.get_all()
        if status:
            tasks = [t for t in tasks if t.status == status]
        if only_overdue is True:
            now = datetime.utcnow()
            tasks = [t for t in tasks if t.due_at and t.due_at < now and t.status != TaskStatus.Done]
        if sort_by:
            tasks = sorted(tasks, key=_SortKey.for_task(sort_by))
        return tasks

    # Search API
    def search_by_member(self, member_id: UUID) -> list[TaskItem]:
        task_ids = {a.task_id for a in self.assignments.find(lambda x: x.member_id == member_id)}
        return [t for t in self.tasks.get_all() if t.id in task_ids]

    def search_members_of_task(self, task_id: UUID) -> list[Member]:
        member_ids = {a.member_id for a in self.assignments.find(lambda x: x.task_id == task_id)}
        return [m for m in self.members.get_all() if m.id in member_ids]

    def search_tasks_by_status_and_term(self, *, status_done: bool | None = None, term: str | None = None) -> list[TaskItem]:
        now = datetime.utcnow()
        def term_ok(t):
            if term == "expired":
                return t.due_at and t.due_at < now
            if term == "ongoing":
                return (t.due_at and t.due_at >= now) or (t.due_at is None)
            return True
        def status_ok(t):
            if status_done is True:
                return t.status == TaskStatus.Done
            if status_done is False:
                return t.status != TaskStatus.Done
            return True
        return [t for t in self.tasks.get_all() if status_ok(t) and term_ok(t)]
