
from __future__ import annotations
from pathlib import Path
from typing import TypeVar, Dict, Type

from .dal.repository import IRepository
from .dal.json_repository import JsonRepository
from .bll.models import Member, TaskItem, Assignment
from .bll.services import MemberService, TaskService, ReportingService

T = TypeVar("T")

class Container:
    def __init__(self, data_dir: Path):
        self.data_dir = data_dir
        self._repos: Dict[type, IRepository] = {}
        self.member_service: MemberService | None = None
        self.task_service: TaskService | None = None
        self.reporting_service: ReportingService | None = None

    def repo(self, model: Type[T]) -> IRepository[T]:
        if model not in self._repos:
            self._repos[model] = JsonRepository[T](self.data_dir, model)
        return self._repos[model]

def build_container(data_dir: str = "data") -> Container:
    c = Container(Path(data_dir))
    member_repo = c.repo(Member)
    task_repo = c.repo(TaskItem)
    assignment_repo = c.repo(Assignment)
    c.member_service = MemberService(member_repo, assignment_repo)
    c.task_service = TaskService(task_repo, c.repo(Member), assignment_repo)
    c.reporting_service = ReportingService(task_repo, member_repo, assignment_repo)
    return c
