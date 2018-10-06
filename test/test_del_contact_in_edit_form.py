from model.contact import Contact


def test_del_contact_in_edit(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(middlename="test_edit_contact"))
    app.contact.delete_contact_in_edit_form()