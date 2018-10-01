# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.session.login(login="admin", password="secret")
    app.contact.create(Contact(firstname="Nickolay", middlename="Igorevich", lastname="Efimov", nickname="kolya", title="Title", company="Company", photo="D:\\testpicture.jpg", address="Address", home_phone="HomePhone", work_phone="MobilePhone", mobile_phone="WorkPhone", fax_number="FaxNumber", email="email1@mail.ru", email2="email2@mail.ru", email3="email3@mail.ru", homepage="homepage.ru", birth_day="17", birth_month="November", birth_year="1995", anniversary_day="18", anniversary_month="December", anniversary_year="1996", group="gav1", address2="address", phone_number_2="HomeAddress", notes="Notes"))
    app.session.logout()

def test_add_empty_contact(app):
    app.session.login(login="admin", password="secret")
    app.contact.create(Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", photo="D:\\testpicture.jpg", address="", home_phone="", work_phone="", mobile_phone="", fax_number="", email="", email2="", email3="", homepage="", birth_day="", birth_month="-", birth_year="", anniversary_day="", anniversary_month="-", anniversary_year="", group="", address2="", phone_number_2="", notes=""))
    app.session.logout()

def test_add_third_contact(app):
    app.session.login(login="admin", password="secret")
    app.contact.create(Contact(firstname="1", middlename="2", lastname="3", nickname="4", title="5", company="", photo="D:\\testpicture.jpg", address="6", home_phone="7", work_phone="8", mobile_phone="9", fax_number="10", email="11", email2="12", email3="13", homepage="14", birth_day="", birth_month="-", birth_year="", anniversary_day="", anniversary_month="-", anniversary_year="", group="", address2="15", phone_number_2="16", notes="17"))
    app.session.logout()
