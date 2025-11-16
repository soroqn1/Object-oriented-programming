
from datetime import datetime, timedelta
from task_planner.ioc import build_container

def test_add_and_get_roundtrip():
    c = build_container(":memory:")
    t = c.task_service.add("Roundtrip", due_at=datetime.utcnow() + timedelta(days=1))
    fetched = c.task_service.tasks.get(t.id)
    assert fetched is not None
    assert str(fetched.id) == str(t.id)
