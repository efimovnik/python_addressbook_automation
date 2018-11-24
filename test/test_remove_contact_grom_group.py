from model.contact import Contact
from model.group import Group
import random


def test_remove_contact_from_group(app, db):
    # check preconditions groups and contacts exist
    if db.get_contacts_count() == 0:
       app.contact.create(Contact(middlename="test_edit_contact"))
    if db.get_groups_count() == 0:
        app.group.create(Group(name="contact_group"))
    # check precondition: at least one contact is in any group
    groups = db.get_group_list()
    random_group = random.choice(groups)
    contacts_in_group = []
    for el in groups:
        if len(db.get_contacts_in_group(el.id)) != 0:
            contacts_in_group.append(db.get_contacts_in_group(el.id))
    if len(contacts_in_group) == 0:
        contacts = db.get_contact_list()
        contact = random.choice(contacts)
        app.contact.transfer_contact_to_group_by_id(contact.id, random_group.name)
    # test remove contact from group
    app.open_home_page()
    for group in groups:
        if len(db.get_contacts_in_group(group.id)) != 0:
            contact_remove = random.choice(db.get_contacts_in_group(group.id))
    app.contact.remove_contact_from_group_by_id(contact_remove.id, group.name)
    contacts_not_in_group = db.get_contacts_not_in_group(group.id)
    l = []
    for element in contacts_not_in_group:
        if contact_remove.id == element.id:
            l.append(contact_remove)
    if len(l) == 0:
        raise AssertionError("Contact is still in group '%s'" % group.name)