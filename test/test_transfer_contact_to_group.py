from model.contact import Contact
from model.group import Group


def test_transfer_contact_to_group(app):
    if app.contact.count() == 0:
       app.contact.create(Contact(middlename="test_edit_contact"))
    if app.group.count_group_named("contact_group") == 0:
        app.group.create(Group(name="contact_group"))
    app.open_home_page()
    app.contact.transfer_contact_to_group(group_transfer="contact_group")
