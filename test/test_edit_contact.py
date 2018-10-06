from model.contact import ContactUpd


def test_edit_contact(app):
    app.contact.edit(ContactUpd(middlename_upd="Igorevich Upd", lastname_upd="Efimov Upd", nickname_upd="kolya Upd", title_upd="Title Upd", company_upd="Company Upd", photo_upd="D:\\testpicture2.jpg", address_upd="Address Upd", home_phone_upd="HomePhone Upd", work_phone_upd="MobilePhone Upd", mobile_phone_upd="WorkPhone Upd", fax_number_upd="FaxNumber Upd", email_upd="updemail1@mail.ru", email2_upd="updemail2@mail.ru", email3_upd="updemail3@mail.ru", homepage_upd="updhomepage.ru", birth_day_upd="19", birth_month_upd="January", birth_year_upd="2005", anniversary_day_upd="20", anniversary_month_upd="February", anniversary_year_upd="2006", address2_upd="address Upd", phone_number_2_upd="HomeAddress Upd", notes_upd="Notes Upd"))
