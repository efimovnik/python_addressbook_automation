# -*- coding: utf-8 -*-
from contact import Contact
from application import Application
import pytest


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(login="admin", password="secret")
    app.create_contact(Contact(firstname="Nickolay", middlename="Igorevich", lastname="Efimov", nickname="kolya", title="Title", company="Company", photo="D:\\testpicture.jpg", address="Address", home_phone="HomePhone", work_phone="MobilePhone", mobile_phone="WorkPhone", fax_number="FaxNumber", email="email1@mail.ru", email2="email2@mail.ru", email3="email3@mail.ru", homepage="homepage.ru", birth_day="17", birth_month="November", birth_year="1995", anniversary_day="18", anniversary_month="December", anniversary_year="1996", group="gav1", address2="address", phone_number_2="HomeAddress", notes="Notes"))
    app.logout()

def test_add_empty_contact(app):
    app.login(login="admin", password="secret")
    app.create_contact(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", photo="D:\\testpicture.jpg", address="", home_phone="", work_phone="", mobile_phone="", fax_number="", email="", email2="", email3="", homepage="", birth_day="", birth_month="-", birth_year="", anniversary_day="", anniversary_month="-", anniversary_year="", group="", address2="", phone_number_2="", notes=""))
    app.logout()
