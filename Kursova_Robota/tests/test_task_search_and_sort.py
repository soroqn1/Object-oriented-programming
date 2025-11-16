
from datetime import datetime, timedelta
from task_planner.ioc import build_container
from task_planner.bll.models import Priority, TaskStatus

def test_list_sort_and_search():
    c = build_container(":memory:")
    t1 = c.task_service.add("B", priority=Priority.High, due_at=datetime.utcnow()+timedelta(days=2))
    t2 = c.task_service.add("A", priority=Priority.Low, due_at=datetime.utcnow()+timedelta(days=1))
    t3 = c.task_service.add("C", priority=Priority.Critical, due_at=datetime.utcnow()-timedelta(days=1))
    c.task_service.set_status(t2.id, TaskStatus.Done)
    # sort by title
    titles = [t.title for t in c.task_service.list_tasks(sort_by="title")]
    assert titles == ["A","B","C"]
    # overdue only
    overdue = c.task_service.list_tasks(only_overdue=True)
    assert any(x.id == t3.id for x in overdue)
    # search done & ongoing
    res = c.task_service.search_tasks_by_status_and_term(status_done=True, term="ongoing")
    assert any(x.id == t2.id for x in res)
