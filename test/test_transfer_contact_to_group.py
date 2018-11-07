from model.contact import Contact
from model.group import Group
import random


def test_transfer_contact_to_group(app, db):
    if db.get_contacts_count() == 0:
       app.contact.create(Contact(middlename="test_edit_contact"))
    if db.get_group_named("contact_group") == False:
        app.group.create(Group(name="contact_group"))
    app.open_home_page()
    contacts = db.get_contact_list()
    contact = random.choice(contacts)
    app.contact.transfer_contact_to_group_by_id(contact.id, "contact_group")
    contacts_in_group = db.get_contacts_in_group(Group(id="145"))
    l = []
    for contact_in_group in contacts_in_group:
        if contact_in_group.id == contact.id:
            l.append(contact_in_group.id)
    if len(l) == 0:
        raise AssertionError("There's no chosen contact in group 'contact_group'")




#def test_transfer_contact_to_group(app):
#    if app.contact.count() == 0:
#       app.contact.create(Contact(middlename="test_edit_contact"))
#    if app.group.check_group_named("contact_group") == False:
#        app.group.create(Group(name="contact_group"))
#    app.open_home_page()
#    contacts = app.contact.get_contact_upd_list()
#    index = randrange(len(contacts))
#    app.contact.transfer_contact_to_group_by_group_index(index, index_group_text)