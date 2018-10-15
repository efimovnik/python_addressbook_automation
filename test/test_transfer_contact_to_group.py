from model.contact import Contact
from model.group import Group
from random import randrange


def test_transfer_contact_to_group(app):
    if app.contact.count() == 0:
       app.contact.create(Contact(middlename="test_edit_contact"))
    if app.group.check_group_named("contact_group") == False:
        app.group.create(Group(name="contact_group"))
    app.open_home_page()
    contacts = app.contact.get_contact_upd_list()
    index = randrange(len(contacts))
    app.contact.transfer_contact_to_group_by_index(index, "contact_group")


#def test_transfer_contact_to_group(app):
#    if app.contact.count() == 0:
#       app.contact.create(Contact(middlename="test_edit_contact"))
#    if app.group.check_group_named("contact_group") == False:
#        app.group.create(Group(name="contact_group"))
#    app.open_home_page()
#    contacts = app.contact.get_contact_upd_list()
#    index = randrange(len(contacts))
#    app.contact.transfer_contact_to_group_by_group_index(index, index_group_text)