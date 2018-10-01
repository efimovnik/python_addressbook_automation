from model.contact import ContactUpd


def test_edit_contact_in_details(app):
    app.session.login(login="admin", password="secret")
    app.contact.edit_in_details(ContactUpd(firstname_upd="Nickolay Edit Upd", middlename_upd="Igorevich Edit Upd", lastname_upd="Efimov Edit Upd", nickname_upd="kolya Edit Upd", title_upd="Title Edit Upd", company_upd="Company Edit Upd", photo_upd="D:\\testpicture3.jpg", address_upd="Address Edit Upd", home_phone_upd="HomePhone Edit Upd", work_phone_upd="MobilePhone Edit Upd", mobile_phone_upd="WorkPhone Edit Upd", fax_number_upd="FaxNumber Edit Upd", email_upd="updeditemail1@mail.ru", email2_upd="updeditemail2@mail.ru", email3_upd="updeditemail3@mail.ru", homepage_upd="updedithomepage.ru", birth_day_upd="22", birth_month_upd="April", birth_year_upd="2005", anniversary_day_upd="21", anniversary_month_upd="May", anniversary_year_upd="2007", address2_upd="address Edit Upd", phone_number_2_upd="HomeAddress Edit Upd", notes_upd="Notes Edit Upd"))
    app.session.logout()