
from task_planner.ioc import build_container
from task_planner.bll.exceptions import DomainValidationException, EntityNotFoundException

def test_member_crud_update_delete():
    c = build_container(":memory:")
    m = c.member_service.add("Ann","Lee",None,6.0)
    m2 = c.member_service.update_member(m.id, first_name="Anna", capacity=7.0)
    assert m2.first_name == "Anna" and m2.capacity_per_day == 7.0
    found = c.member_service.find_members("ann")
    assert any(x.id == m2.id for x in found)
    c.member_service.delete_member(m.id)
    assert c.member_service.find_members("ann") == []
    try:
        c.member_service.delete_member(m.id)
    except EntityNotFoundException:
        pass
