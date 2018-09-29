# -*- coding: utf-8 -*-

from group import Group
from application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_group(app):
    app.login(login="admin", password="secret")
    app.create_group(Group(name="gav2", header="gav3", footer="gav4"))
    app.logout()


def test_add_empty_group(app):
    app.login(login="admin", password="secret")
    app.create_group(Group(name="", header="", footer=""))
    app.logout()
