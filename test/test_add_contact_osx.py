# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group


def test_add_contact(app):
    if app.group.check_group_named("gav1") == False:
        app.group.create(Group(name="gav1"))
    app.open_home_page()
    app.contact.create(Contact(firstname="Nickolay", middlename="Igorevich", lastname="Efimov", nickname="kolya", title="Title", company="Company", photo="/Users/nikolayefimov/Downloads/pictures pycharm/testpicture.jpg", address="Address", home_phone="HomePhone", work_phone="MobilePhone", mobile_phone="WorkPhone", fax_number="FaxNumber", email="email1@mail.ru", email2="email2@mail.ru", email3="email3@mail.ru", homepage="homepage.ru", birth_day="17", birth_month="November", birth_year="1995", anniversary_day="18", anniversary_month="December", anniversary_year="1996", group="gav1", address2="address", phone_number_2="HomeAddress", notes="Notes"))


def test_add_empty_contact(app):
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", photo="/Users/nikolayefimov/Downloads/pictures pycharm/testpicture.jpg", address="", home_phone="", work_phone="", mobile_phone="", fax_number="", email="", email2="", email3="", homepage="", birth_day="", birth_month="-", birth_year="", anniversary_day="", anniversary_month="-", anniversary_year="", group="[none]", address2="", phone_number_2="", notes=""))


def test_add_third_contact(app):
    app.contact.create(Contact(firstname="1", middlename="2", lastname="3", nickname="4", title="5", company="", photo="/Users/nikolayefimov/Downloads/pictures pycharm/testpicture.jpg", address="6", home_phone="7", work_phone="8", mobile_phone="9", fax_number="10", email="11", email2="12", email3="13", homepage="14", birth_day="", birth_month="-", birth_year="", anniversary_day="", anniversary_month="-", anniversary_year="", group="[none]", address2="15", phone_number_2="16", notes="17"))
