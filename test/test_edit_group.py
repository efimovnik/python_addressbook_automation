from model.group import Group
import random
import time


def test_modify_some_group_name(app, db, check_ui):
    if db.get_groups_count() == 0:
        app.group.create(Group(name="test_edit_group"))
    old_groups = db.get_group_list()
    group_edit = random.choice(old_groups)
    group = Group(name="New group")
    app.group.modify_group_by_id(group_edit.id, group)
    time.sleep(1)
    new_groups = db.get_group_list()
    assert len(old_groups) == len(new_groups)
    group.id = group_edit.id
    old_groups.remove(group_edit)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:
        assert sorted(new_groups, key=Group.id_or_max) == sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_modify_first_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test_edit_group"))
    old_groups = app.group.get_group_list()
    app.group.modify_first_group(Group(header="header_edited"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
