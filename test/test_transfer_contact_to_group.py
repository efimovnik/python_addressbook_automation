from model.contact import Contact
from model.group import Group
import random


def test_transfer_contact_to_group(app, db):
    # Check preconditions: contacts and groups exist
    if db.get_contacts_count() == 0:
       app.contact.create(Contact(middlename="test_edit_contact"))
    if db.get_groups_count() == 0:
        app.group.create(Group(name="contact_group"))
    # check precondition: at least one contact isn't in any group
    groups = db.get_group_list()
    for el in groups:
        contacts_not_in_group = []
        contacts_not_in_group.append(db.get_contacts_not_in_group(el.id))
    if len(contacts_not_in_group) == 0:
        app.contact.create(Contact(middlename="contact_not_in_group"))
    # test transfer contact to group
    app.open_home_page()
    groups = db.get_group_list()
    for group in groups:
        if len(db.get_contacts_not_in_group(group.id)) != 0:
            contact = random.choice(db.get_contacts_not_in_group(group.id))
    app.contact.transfer_contact_to_group_by_id(contact.id, group.name)
    contacts_in_group = db.get_contacts_in_group(group.id)
    l = []
    for element in contacts_in_group:
        if contact.id == element.id:
            l.append(contact)
    if len(l) == 0:
        raise AssertionError("Contact not in group '%s'" % group.name)



#def test_transfer_contact_to_group(app):
#    if app.contact.count() == 0:
#       app.contact.create(Contact(middlename="test_edit_contact"))
#    if app.group.check_group_named("contact_group") == False:
#        app.group.create(Group(name="contact_group"))
#    app.open_home_page()
#    contacts = app.contact.get_contact_upd_list()
#    index = randrange(len(contacts))
#    app.contact.transfer_contact_to_group_by_group_index(index, index_group_text)