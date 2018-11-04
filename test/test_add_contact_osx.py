# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group



def test_add_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    if not db.get_group_named("gav1") > 0:
        app.group.create(Group(name="gav1"))
    app.open_home_page()
    old_contacts = db.get_contact_list()
    app.contact.create(contact)
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(), key=Contact.id_or_max)