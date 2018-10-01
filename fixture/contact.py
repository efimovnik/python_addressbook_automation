from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException

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
        # Fill bith month
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.birth_month)
        wd.find_element_by_name("bmonth").click()
        # Fill bith year
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

    def edit(self, contact):
        wd = self.app.wd
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # edit contact by pencil icon
        wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()
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
        wd.find_element_by_name("update").click()


    def confirm_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

