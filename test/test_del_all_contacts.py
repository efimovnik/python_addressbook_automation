from model.contact import Contact
import time

def test_del_all_contacts(app, db, check_ui):
    if db.get_contacts_count() == 0:
        app.contact.create(Contact(middlename="test_del_contact"))
        app.open_home_page()
    app.contact.delete_all_contacts()
    time.sleep(1) # db did not have time to get information about the remote contact
    new_contacts = db.get_contact_list()
    assert new_contacts == []
    if check_ui:
        assert sorted(new_contacts, key=Contact.id_or_max) == sorted(app.contact.get_contact_list(),
                                                                     key=Contact.id_or_max)
