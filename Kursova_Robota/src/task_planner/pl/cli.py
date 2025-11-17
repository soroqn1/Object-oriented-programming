
from __future__ import annotations
import typer
from typing import Optional
from datetime import datetime
from uuid import UUID
from rich import print as rprint

from ..ioc import build_container
from ..bll.models import TaskStatus, Priority
from ..bll.exceptions import DomainValidationException, EntityNotFoundException, OverAllocationException

app = typer.Typer(help="Task Planner (Python) — DAL/BLL/PL coursework")

class _Err:
    @staticmethod
    def wrap(fn):
        def _w(*args, **kwargs):
            try:
                return fn(*args, **kwargs)
            except (DomainValidationException, EntityNotFoundException, OverAllocationException, ValueError) as e:
                typer.secho(f"Error: {e}", fg=typer.colors.RED)
                raise typer.Exit(1)
        return _w

@app.callback()
def _init(ctx: typer.Context, data_dir: str = typer.Option("data", help="Directory for JSON storage")):
    ctx.obj = build_container(data_dir)

# ---- Members ----
member_app = typer.Typer(help="Manage members")
app.add_typer(member_app, name="member")

@member_app.command("add")
@_Err.wrap
def member_add(ctx: typer.Context,
               first_name: str,
               last_name: str,
               email: Optional[str] = None,
               capacity: Optional[float] = typer.Option(None, help="Capacity per day (hours)")):
    c = ctx.obj
    m = c.member_service.add(first_name, last_name, email, capacity)  
    rprint({"id": str(m.id), "name": f"{m.first_name} {m.last_name}", "capacity": m.capacity_per_day})

@member_app.command("list")
def member_list(ctx: typer.Context):
    c = ctx.obj
    for m in c.member_service.list():  
        rprint({"id": str(m.id), "name": f"{m.first_name} {m.last_name}", "email": m.email, "capacity": m.capacity_per_day})

@member_app.command("update")
@_Err.wrap
def member_update(ctx: typer.Context, member_id: str,
                  first_name: Optional[str] = None, last_name: Optional[str] = None,
                  email: Optional[str] = None, capacity: Optional[float] = None):
    c = ctx.obj
    m = c.member_service.update_member(UUID(member_id), first_name=first_name, last_name=last_name, email=email, capacity=capacity)  
    rprint({"id": str(m.id), "name": f"{m.first_name} {m.last_name}", "email": m.email, "capacity": m.capacity_per_day})

@member_app.command("delete")
@_Err.wrap
def member_delete(ctx: typer.Context, member_id: str):
    c = ctx.obj
    c.member_service.delete_member(UUID(member_id))  
    rprint({"deleted": member_id})

@member_app.command("find")
def member_find(ctx: typer.Context, keyword: str):
    c = ctx.obj
    res = c.member_service.find_members(keyword)  
    for m in res: rprint({"id": str(m.id), "name": f"{m.first_name} {m.last_name}", "email": m.email})

# ---- Tasks ----
task_app = typer.Typer(help="Manage tasks")
app.add_typer(task_app, name="task")

@task_app.command("add")
@_Err.wrap
def task_add(ctx: typer.Context,
             title: str,
             prio: str = typer.Option(Priority.Medium, "--prio", case_sensitive=False),
             due: Optional[str] = typer.Option(None, "--due", help="YYYY-MM-DD"),
             desc: Optional[str] = typer.Option(None, "--desc")):
    c = ctx.obj
    due_dt = datetime.strptime(due, "%Y-%m-%d") if due else None
    t = c.task_service.add(title, prio, due_dt, desc)  
    rprint({"id": str(t.id), "title": t.title, "priority": t.priority, "due": t.due_at.isoformat() if t.due_at else None})

@task_app.command("list")
def task_list(ctx: typer.Context, status: Optional[str] = typer.Option(None, "--status")):
    c = ctx.obj
    tasks = c.task_service.get_by_status(status) if status else c.task_service.tasks.get_all()  
    for t in tasks:
        rprint({"id": str(t.id), "title": t.title, "status": t.status, "progress": t.progress, "due": t.due_at.isoformat() if t.due_at else None})

@task_app.command("view")
def task_view(ctx: typer.Context, task_id: str):
    c = ctx.obj
    t = c.task_service.tasks.get(UUID(task_id))  
    if not t: raise typer.Exit(1)
    rprint(t.__dict__)

@task_app.command("update")
@_Err.wrap
def task_update(ctx: typer.Context, task_id: str,
                title: Optional[str] = None, desc: Optional[str] = None,
                prio: Optional[str] = None, due: Optional[str] = None, status: Optional[str] = None):
    c = ctx.obj
    due_dt = datetime.strptime(due, "%Y-%m-%d") if due else None
    t = c.task_service.update_task(UUID(task_id), title=title, description=desc, priority=prio, due_at=due_dt, status=status)  
    rprint({"id": str(t.id), "title": t.title, "priority": t.priority, "status": t.status})

@task_app.command("delete")
@_Err.wrap
def task_delete(ctx: typer.Context, task_id: str):
    c = ctx.obj
    c.task_service.delete_task(UUID(task_id))  
    rprint({"deleted": task_id})

@task_app.command("list2")
def task_list2(ctx: typer.Context,
               status: Optional[str] = typer.Option(None, "--status"),
               overdue: bool = typer.Option(False, "--overdue/--no-overdue"),
               sort_by: Optional[str] = typer.Option(None, "--sort-by", help="title|priority|due|status")):
    c = ctx.obj
    tasks = c.task_service.list_tasks(status=status, only_overdue=(True if overdue else None), sort_by=sort_by)  
    for t in tasks:
        rprint({"id": str(t.id), "title": t.title, "status": t.status, "priority": t.priority, "due": t.due_at.isoformat() if t.due_at else None})

@task_app.command("search-by-member")
def search_by_member(ctx: typer.Context, member_id: str):
    c = ctx.obj
    tasks = c.task_service.search_by_member(UUID(member_id))  
    for t in tasks: rprint({"id": str(t.id), "title": t.title})

@task_app.command("search-members-of-task")
def search_members_of_task(ctx: typer.Context, task_id: str):
    c = ctx.obj
    members = c.task_service.search_members_of_task(UUID(task_id))  
    for m in members: rprint({"id": str(m.id), "name": f"{m.first_name} {m.last_name}"})

@task_app.command("search-tasks")
def search_tasks(ctx: typer.Context,
                 done: Optional[bool] = typer.Option(None, "--done/--not-done", help="Filter by completion"),
                 term: Optional[str] = typer.Option(None, "--term", help="expired|ongoing")):
    c = ctx.obj
    res = c.task_service.search_tasks_by_status_and_term(status_done=done, term=term)  
    for t in res:
        rprint({"id": str(t.id), "title": t.title, "status": t.status, "due": t.due_at.isoformat() if t.due_at else None})

@task_app.command("assign")
@_Err.wrap
def task_assign(ctx: typer.Context, task_id: str, member_id: str, hours: float):
    c = ctx.obj
    a = c.task_service.assign(UUID(task_id), UUID(member_id), hours)  
    rprint({"assignment_id": str(a.id), "task_id": str(a.task_id), "member_id": str(a.member_id), "hours": a.allocated_hours})

@task_app.command("set-status")
@_Err.wrap
def task_set_status(ctx: typer.Context, task_id: str, status: str):
    c = ctx.obj
    c.task_service.set_status(UUID(task_id), status)  
    rprint({"ok": True})

@task_app.command("set-progress")
@_Err.wrap
def task_set_progress(ctx: typer.Context, task_id: str, progress: int):
    c = ctx.obj
    c.task_service.set_progress(UUID(task_id), progress)  
    rprint({"ok": True})

# ---- Reports ----
@app.command("report")
def report_state(ctx: typer.Context):
    c = ctx.obj
    state = c.reporting_service.get_project_state()  
    rprint({
        "total": state.total,
        "done": state.done,
        "active": state.active,
        "overdue": state.overdue,
        "by_member_load": state.by_member_load
    })

def main():
    app()

if __name__ == "__main__":
    main()
