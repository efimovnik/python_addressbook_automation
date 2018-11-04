from model.contact import ContactUpd, Contact
import random


def test_edit_some_contact_in_details_osx(app, db, check_ui):
    if db.get_contacts_count() == 0:
        app.contact.create(Contact(middlename="test_edit_contact"))
    old_contacts = db.get_contact_upd_list()
    contact_edit = random.choice(old_contacts)
    contact = ContactUpd(firstname_upd="Nickolay Edit Upd", middlename_upd="Igorevich Edit Upd",
                         lastname_upd="Efimov Edit Upd", nickname_upd="kolya Edit Upd", title_upd="Title Edit Upd",
                         company_upd="Company Edit Upd",
                         photo_upd="D:\\testpicture3.jpg",
                         address_upd="Address Edit Upd", home_phone_upd="HomePhone Edit Upd",
                         work_phone_upd="MobilePhone Edit Upd", mobile_phone_upd="WorkPhone Edit Upd",
                         fax_number_upd="FaxNumber Edit Upd", email_upd="updeditemail1@mail.ru",
                         email2_upd="updeditemail2@mail.ru", email3_upd="updeditemail3@mail.ru",
                         homepage_upd="updedithomepage.ru", birth_day_upd="22", birth_month_upd="April",
                         birth_year_upd="2005", anniversary_day_upd="21", anniversary_month_upd="May",
                         anniversary_year_upd="2007", address2_upd="address Edit Upd",
                         phone_number_2_upd="HomeAddress Edit Upd", notes_upd="Notes Edit Upd")
    app.contact.edit_in_details_by_id(contact_edit.id, contact)
    new_contacts = db.get_contact_upd_list()
    contact.id = contact_edit.id
    old_contacts.remove(contact_edit)
    old_contacts.append(contact)
    assert sorted(old_contacts, key=ContactUpd.id_or_max) == sorted(new_contacts, key=ContactUpd.id_or_max)
    if check_ui:
        assert sorted(new_contacts, key=ContactUpd.id_or_max) == sorted(app.contact.get_group_list(),
                                                                        key=ContactUpd.id_or_max)