from model.contact import Contact

def test_del_all_contacts(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(middlename="test_del_contact"))
    app.contact.delete_all_contacts()
