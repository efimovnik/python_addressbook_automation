# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group
import pytest
import random
import string
import calendar


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " "*10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


def random_day():
    return str(random.randrange(1, 32, 1))


def random_month():
    return calendar.month_name[random.randrange(1, 13, 1)]


testdata = [Contact(firstname="", middlename="", lastname="", nickname="", title="", company="", photo="/Users/nikolayefimov/Downloads/pictures pycharm/testpicture.jpg", address="", home_phone="", work_phone="", mobile_phone="", fax_number="", email="", email2="", email3="", homepage="", birth_day="", birth_month="-", birth_year="", anniversary_day="", anniversary_month="-", anniversary_year="", group="[none]", address2="", phone_number_2="", notes="")] + \
           [Contact(firstname=random_string("Nickolay", 10), middlename=random_string("Igorevich", 10),
                     lastname=random_string("Efimov", 5), nickname=random_string("kolya", 10), title=random_string("Title", 10),
                     company=random_string("Company", 10), photo="/Users/nikolayefimov/Downloads/pictures pycharm/testpicture.jpg",
                     address=random_string("Address", 5), home_phone=random_string("HomePhone", 10),
                     work_phone=random_string("MobilePhone", 10), mobile_phone=random_string("WorkPhone", 5),
                     fax_number=random_string("FaxNumber", 10), email=random_string("email1@mail.ru", 5),
                     email2=random_string("email2@mail.ru", 5), email3=random_string("email3@mail.ru", 5),
                     homepage=random_string("homepage.ru", 5), birth_day=random_day(),
                     birth_month=random_month(), birth_year=random_string("1", 5), anniversary_day=random_day(),
                     anniversary_month=random_month(), anniversary_year=random_string("1996", 5), group="gav1",
                     address2=random_string("address", 5), phone_number_2=random_string("HomeAddress", 10),
                     notes=random_string("Notes", 5))
            for i in range(5)
]


@pytest.mark.parametrize("contact", testdata, ids=[repr(x) for x in testdata])
def test_add_contact(app, contact):
    if not app.group.check_group_named("gav1"):
        app.group.create(Group(name="gav1"))
    app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)