from sys import maxsize


class Contact:

    def __init__(self, id=None, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None, address=None, photo=None,
                 home_phone=None, work_phone=None, mobile_phone=None, all_phones_from_homepage=None, fax_number=None, email=None, email2=None, email3=None,
                 all_emails_from_homepage=None, homepage=None, birth_day=None, birth_month=None, birth_year=None, anniversary_day=None, anniversary_month=None,
                 anniversary_year=None, group=None, address2=None, phone_number_2=None, notes=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.photo = photo
        self.home_phone = home_phone
        self.work_phone = work_phone
        self.mobile_phone = mobile_phone
        self.all_phones_from_homepage = all_phones_from_homepage
        self.fax_number = fax_number
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.all_emails_from_homepage = all_emails_from_homepage
        self.homepage = homepage
        self.birth_day = birth_day
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.anniversary_day = anniversary_day
        self.anniversary_month = anniversary_month
        self.anniversary_year = anniversary_year
        self.group = group
        self.address2 = address2
        self.phone_number_2 = phone_number_2
        self.notes = notes
        self.id = id

    def __repr__(self):
            return "%s:%s:%s" % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
            return (self.id is None or other.id is None or self.id == other.id) and self.lastname == other.lastname and self.firstname == other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize

class ContactUpd:

    def __init__(self, firstname_upd=None, middlename_upd=None, lastname_upd=None, nickname_upd=None, title_upd=None, company_upd=None, address_upd=None, photo_upd=None,
                 home_phone_upd=None, work_phone_upd=None, mobile_phone_upd=None, fax_number_upd=None, email_upd=None, email2_upd=None, email3_upd=None,
                 homepage_upd=None, birth_day_upd=None, birth_month_upd=None, birth_year_upd=None, anniversary_day_upd=None, anniversary_month_upd=None,
                 anniversary_year_upd=None, address2_upd=None, phone_number_2_upd=None, notes_upd=None, id=None):
        self.firstname_upd = firstname_upd
        self.middlename_upd = middlename_upd
        self.lastname_upd = lastname_upd
        self.nickname_upd = nickname_upd
        self.title_upd = title_upd
        self.company_upd = company_upd
        self.address_upd = address_upd
        self.photo_upd = photo_upd
        self.home_phone_upd = home_phone_upd
        self.work_phone_upd = work_phone_upd
        self.mobile_phone_upd = mobile_phone_upd
        self.fax_number_upd = fax_number_upd
        self.email_upd = email_upd
        self.email2_upd = email2_upd
        self.email3_upd = email3_upd
        self.homepage_upd = homepage_upd
        self.birth_day_upd = birth_day_upd
        self.birth_month_upd = birth_month_upd
        self.birth_year_upd = birth_year_upd
        self.anniversary_day_upd = anniversary_day_upd
        self.anniversary_month_upd = anniversary_month_upd
        self.anniversary_year_upd = anniversary_year_upd
        self.address2_upd = address2_upd
        self.phone_number_2_upd = phone_number_2_upd
        self.notes_upd = notes_upd
        self.id = id

    def __repr__(self):
            return "%s:%s:%s" % (self.id, self.lastname_upd, self.firstname_upd)

    def __eq__(self, other):
            return (self.id is None or other.id is None or self.id == other.id) and self.lastname_upd == other.lastname_upd \
                   and self.firstname_upd == other.firstname_upd

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize