from model.contact import Contact


def test_del_contact_in_details(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(middlename="test_edit_contact"))
    old_contacts = app.contact.get_contact_list()
    app.contact.delete_contact_in_details()
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    old_contacts[0:1] = []
    assert old_contacts == new_contacts