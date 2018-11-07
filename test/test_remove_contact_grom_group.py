from model.contact import Contact
from model.group import Group
import random


def test_remove_contact_from_group(app, db):
    if db.get_contacts_count() == 0:
       app.contact.create(Contact(middlename="test_edit_contact"))
    if db.get_group_named("contact_group") == False:
        app.group.create(Group(name="contact_group"))
    contacts_in_group = db.get_contacts_in_group(Group(id="145"))
    if len(contacts_in_group) == 0:
        contacts = db.get_contact_list()
        contact = random.choice(contacts)
        app.open_home_page()
        app.contact.transfer_contact_to_group_by_id(contact.id, "contact_group")
        contacts_in_group.append(contact)
    contact_in_group = random.choice(contacts_in_group)
    app.contact.remove_contact_from_group_by_id(contact_in_group.id, "contact_group")
    new_contacts_in_group = db.get_contacts_in_group(Group(id="145"))
    for new_contact_in_group in new_contacts_in_group:
        if new_contact_in_group.id == contact_in_group.id:
            raise AssertionError("Contact '%s' is still in 'contact_group'" % contact_in_group.firstname)