# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group


def test_add_contact(app, json_contacts_win):
    contact = json_contacts_win
    if not app.group.check_group_named("gav1"):
        app.group.create(Group(name="gav1"))
    app.open_home_page()
    old_contacts = app.contact.get_contact_list()
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)