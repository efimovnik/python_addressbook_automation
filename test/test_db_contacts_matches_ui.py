from model.contact import Contact
import re


def test_contact_list(app, db):
    def clean(contact):
        return Contact(id=contact.id, firstname=contact.firstname, lastname=contact.lastname,
                        address=contact.address, email=contact.email, email2=contact.email2, email3=contact.email3,
                        home_phone=contact.home_phone, work_phone=contact.work_phone, mobile_phone=contact.mobile_phone,
                        phone_number_2=contact.phone_number_2)
    ui_list = sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
    db_list = sorted(map(clean, db.get_contact_list()), key=Contact.id_or_max)
    ui_phones_emails = []
    db_phones_emails = []
    for contact_db in db_list:
        all_phones_from_homepage = merge_phones_like_on_home_page(contact_db)
        all_emails_from_homepage = merge_emails_like_on_home_page(contact_db)
        ui_phones_emails.append(all_phones_from_homepage and all_emails_from_homepage)
    for contact_ui in ui_list:
        db_phones_emails.append(contact_ui.all_phones_from_homepage and contact_ui.all_emails_from_homepage)
    assert sorted(ui_phones_emails) == sorted(db_phones_emails)
    assert ui_list == db_list



def clear(s):
    return re.sub('[ () - ! ]', '', s)


def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.home_phone, contact.mobile_phone, contact.work_phone, contact.phone_number_2]))))


def merge_emails_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                            map(lambda x: clear(x),
                                filter(lambda x: x is not None,
                                       [contact.email, contact.email2, contact.email3]))))
