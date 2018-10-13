from model.contact import Contact

def test_del_all_contacts(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(middlename="test_del_contact"))
        app.open_home_page()
    app.contact.delete_all_contacts()
    new_contacts = app.contact.get_contact_list()
    assert new_contacts == []
