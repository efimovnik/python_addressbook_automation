# -*- coding: utf-8 -*-

from model.group import Group

def test_add_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="gav2", header="gav3", footer="gav4"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)


def test_add_contact_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="contact_group", header="contact_group", footer="contact_group"))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
