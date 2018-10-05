# -*- coding: utf-8 -*-

from model.group import Group

def test_add_group(app):
    app.group.create(Group(name="gav2", header="gav3", footer="gav4"))


def test_add_empty_group(app):
    app.group.create(Group(name="", header="", footer=""))


def test_add_contact_group(app):
    app.group.create(Group(name="contact_group", header="contact_group", footer="contact_group"))

