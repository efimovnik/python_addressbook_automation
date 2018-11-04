from model.contact import ContactUpd, Contact
import random


def test_edit_contact(app, db, check_ui):
    if db.get_contacts_count() == 0:
        app.contact.create(Contact(middlename="test_edit_contact"))
    old_contacts = db.get_contact_list()
    contact_edit = random.choice(old_contacts)
    contact = ContactUpd(firstname_upd="Nickolay Upd", middlename_upd="Igorevich Upd", lastname_upd="Efimov Upd", nickname_upd="kolya Upd", title_upd="Title Upd", company_upd="Company Upd", photo_upd="/Users/nikolayefimov/Downloads/pictures pycharm/testpicture2.jpeg", address_upd="Address Upd", home_phone_upd="HomePhone Upd", work_phone_upd="MobilePhone Upd", mobile_phone_upd="WorkPhone Upd", fax_number_upd="FaxNumber Upd", email_upd="updemail1@mail.ru", email2_upd="updemail2@mail.ru", email3_upd="updemail3@mail.ru", homepage_upd="updhomepage.ru", birth_day_upd="19", birth_month_upd="January", birth_year_upd="2005", anniversary_day_upd="20", anniversary_month_upd="February", anniversary_year_upd="2006", address2_upd="address Upd", phone_number_2_upd="HomeAddress Upd", notes_upd="Notes Upd")
    app.contact.edit_by_id(contact_edit.id, contact)
    new_contacts = db.get_contact_upd_list()
    contact.id = contact_edit.id
    old_contacts.remove(contact_edit)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=ContactUpd.id_or_max) == sorted(new_contacts, key=ContactUpd.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=ContactUpd.id_or_max) == sorted(app.contact.get_group_list(),
                                                                     key=ContactUpd.id_or_max)
