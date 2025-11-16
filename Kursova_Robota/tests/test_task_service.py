
from datetime import datetime, timedelta
import pytest

from task_planner.ioc import build_container
from task_planner.bll.exceptions import DomainValidationException, OverAllocationException

def test_add_throws_on_empty_title():
    c = build_container(":memory:")
    with pytest.raises(DomainValidationException):
        c.task_service.add("", due_at=datetime.utcnow() + timedelta(days=1))

def test_over_allocation():
    c = build_container(":memory:")
    m = c.member_service.add("Ann", "Lee", None, 4.0)
    t = c.task_service.add("Task", due_at=datetime.utcnow() + timedelta(days=1))
    c.task_service.assign(t.id, m.id, 3.0)
    with pytest.raises(OverAllocationException):
        c.task_service.assign(t.id, m.id, 2.0)

def test_progress_sets_done():
    c = build_container(":memory:")
    t = c.task_service.add("X", due_at=datetime.utcnow() + timedelta(days=1))
    c.task_service.set_progress(t.id, 100)
    got = c.task_service.tasks.get(t.id)
    assert got.status == "Done"
