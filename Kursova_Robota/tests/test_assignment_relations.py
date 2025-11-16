
from datetime import datetime, timedelta
from task_planner.ioc import build_container

def test_relations_member_task():
    c = build_container(":memory:")
    m = c.member_service.add("Ann","Lee",None,8.0)
    t = c.task_service.add("Task", due_at=datetime.utcnow()+timedelta(days=1))
    c.task_service.assign(t.id, m.id, 2.0)
    assert any(x.id == t.id for x in c.task_service.search_by_member(m.id))
    assert any(x.id == m.id for x in c.task_service.search_members_of_task(t.id))
