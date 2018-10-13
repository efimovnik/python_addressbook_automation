from model.contact import ContactUpd, Contact



def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(middlename="test_edit_contact"))
    old_contacts = app.contact.get_contact_upd_list()
    contact = ContactUpd(firstname_upd="Nickolay Upd", middlename_upd="Igorevich Upd", lastname_upd="Efimov Upd", nickname_upd="kolya Upd", title_upd="Title Upd", company_upd="Company Upd", photo_upd="/Users/nikolayefimov/Downloads/pictures pycharm/testpicture2.jpeg", address_upd="Address Upd", home_phone_upd="HomePhone Upd", work_phone_upd="MobilePhone Upd", mobile_phone_upd="WorkPhone Upd", fax_number_upd="FaxNumber Upd", email_upd="updemail1@mail.ru", email2_upd="updemail2@mail.ru", email3_upd="updemail3@mail.ru", homepage_upd="updhomepage.ru", birth_day_upd="19", birth_month_upd="January", birth_year_upd="2005", anniversary_day_upd="20", anniversary_month_upd="February", anniversary_year_upd="2006", address2_upd="address Upd", phone_number_2_upd="HomeAddress Upd", notes_upd="Notes Upd")
    contact.id = old_contacts[0].id
    app.contact.edit(contact)
    new_contacts = app.contact.get_contact_upd_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[0] = contact
    assert sorted(old_contacts, key=ContactUpd.id_or_max) == sorted(new_contacts, key=ContactUpd.id_or_max)