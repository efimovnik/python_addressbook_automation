from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def init_add_new_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        # Initiation of creating new contact
        self.init_add_new_contact()
        # Fill Initials
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        # Fill Nickname
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname)
        # Fill contact Title
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title)
        # Fill company name
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company)
        # Fill adress
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        # Select photo
        wd.find_element_by_name("photo").send_keys(contact.photo)
        # Fill home number
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_phone)
        # Fill mobile number
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_phone)
        # Fill work number
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work_phone)
        # Fill fax number
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax_number)
        # Fill email
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        # Fill email2
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        # Fill email3
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        # Fill homepage
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)
        # Fill bith date
        # Fill bith day
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.birth_day)
        wd.find_element_by_name("bday").click()
        # Fill birth month
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.birth_month)
        wd.find_element_by_name("bmonth").click()
        # Fill birth year
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.birth_year)

        # Select anniversary date
        # Select anniversary day
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.anniversary_day)
        wd.find_element_by_name("aday").click()
        # Fill anniversary month
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.anniversary_month)
        wd.find_element_by_name("amonth").click()
        # Fill anniversary year
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.anniversary_year)
        # Select belonging group
        wd.find_element_by_name("new_group").click()
        Select(wd.find_element_by_name("new_group")).select_by_visible_text(contact.group)
        wd.find_element_by_name("new_group").click()
        # Fill secondary address
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address2)
        # Fill secondary phone number
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone_number_2)
        # Fill notes
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)
        # Confirm creation of new contact
        self.confirm_contact_creation()

    def delete_first_contact(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # delete contact
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # submit delete contact
        wd.switch_to_alert().accept()

    def delete_contact_in_details(self):
        wd = self.app.wd
        # see details of first contact
        wd.find_element_by_xpath("(//img[@alt='Details'])[2]").click()
        # modify contact
        wd.find_element_by_name("modifiy").click()
        # delete contact
        wd.find_element_by_xpath("//input[@value='Delete']").click()

    def delete_contact_in_edit_form(self):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # initiate edit contact by pencil icon
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        # delete contact
        wd.find_element_by_xpath("//input[@value='Delete']").click()

    def delete_all_contacts(self):
        wd = self.app.wd
        # select all contacts
        wd.find_element_by_id("MassCB").click()
        # delete contact
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # submit delete contact
        wd.switch_to_alert().accept()

    def edit(self, contact):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # initiate edit contact by pencil icon
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
        # Fill editing Initials
        self.change_contact_field("firstname", contact.firstname_upd)
        self.change_contact_field("middlename", contact.middlename_upd)
        self.change_contact_field("lastname", contact.middlename_upd)
        self.change_contact_field("nickname", contact.nickname_upd)
        self.change_contact_field("title", contact.title_upd)
        self.change_contact_field("company", contact.company_upd)
        self.change_contact_field("address", contact.address_upd)
        self.change_photo(contact.photo_upd)
        self.change_contact_field("home", contact.home_phone_upd)
        self.change_contact_field("mobile", contact.mobile_phone_upd)
        self.change_contact_field("work", contact.work_phone_upd)
        self.change_contact_field("fax", contact.fax_number_upd)
        self.change_contact_field("email", contact.email_upd)
        self.change_contact_field("email2", contact.email2_upd)
        self.change_contact_field("email3", contact.email3_upd)
        self.change_contact_field("homepage", contact.homepage_upd)
        self.select_date("bday", contact.birth_day_upd)
        self.select_date("bmonth", contact.birth_month_upd)
        self.change_contact_field("byear", contact.birth_year_upd)
        self.select_date("aday", contact.anniversary_day_upd)
        self.select_date("amonth", contact.anniversary_month_upd)
        self.change_contact_field("ayear", contact.anniversary_year_upd)
        self.change_contact_field("address2", contact.address2_upd)
        self.change_contact_field("phone2", contact.phone_number_2_upd)
        self.change_contact_field("notes", contact.notes_upd)
        # Confirm editing creation of new contact
        wd.find_element_by_name("update").click()

    def select_date(self, field_date_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_date_name).click()
            Select(wd.find_element_by_name(field_date_name)).select_by_visible_text(text)
            wd.find_element_by_name(field_date_name).click()

    def change_contact_field(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_photo(self, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name("photo").send_keys(text)

    def transfer_contact_to_group(self, group_transfer):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # select group to transfer
        wd.find_element_by_name("to_group").click()
        Select(wd.find_element_by_name("to_group")).select_by_visible_text(group_transfer)
        # submit add to group to transfer
        wd.find_element_by_name("add").click()

    def edit_in_details(self, contact):
        wd = self.app.wd
        # see details of first contact
        wd.find_element_by_xpath("(//img[@alt='Details'])[2]").click()
        # modify contact
        wd.find_element_by_name("modifiy").click()
        # Fill editing Initials
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname_upd)
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(contact.middlename_upd)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname_upd)
        # Fill editing Nickname
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(contact.nickname_upd)
        # Fill contact Title
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(contact.title_upd)
        # Fill editing company name
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(contact.company_upd)
        # Fill editing adress
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address_upd)
        # Select editing photo
        wd.find_element_by_name("photo").send_keys(contact.photo_upd)
        # Fill editing home number
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.home_phone_upd)
        # Fill editing mobile number
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile_phone_upd)
        # Fill editing work number
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.work_phone_upd)
        # Fill editing fax number
        wd.find_element_by_name("fax").clear()
        wd.find_element_by_name("fax").send_keys(contact.fax_number_upd)
        # Fill editing email
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email_upd)
        # Fill editing email2
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2_upd)
        # Fill editing email3
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3_upd)
        # Fill editing homepage
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage_upd)
        # Fill editing bith date
        # Fill editing bith day
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.birth_day_upd)
        wd.find_element_by_name("bday").click()
        # Fill editing bith month
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.birth_month_upd)
        wd.find_element_by_name("bmonth").click()
        # Fill editing bith year
        wd.find_element_by_name("byear").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.birth_year_upd)

        # Select editing anniversary date
        # Select editing anniversary day
        wd.find_element_by_name("aday").click()
        Select(wd.find_element_by_name("aday")).select_by_visible_text(contact.anniversary_day_upd)
        wd.find_element_by_name("aday").click()
        # Fill editing anniversary month
        wd.find_element_by_name("amonth").click()
        Select(wd.find_element_by_name("amonth")).select_by_visible_text(contact.anniversary_month_upd)
        wd.find_element_by_name("amonth").click()
        # Fill editing anniversary year
        wd.find_element_by_name("ayear").click()
        wd.find_element_by_name("ayear").clear()
        wd.find_element_by_name("ayear").send_keys(contact.anniversary_year_upd)
        # Fill editing secondary address
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address2_upd)
        # Fill editing secondary phone number
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone_number_2_upd)
        # Fill editing notes
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes_upd)
        # Confirm editing creation of new contact
        wd.find_element_by_xpath("//input[@value='Update']").click()

    def confirm_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
