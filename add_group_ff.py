# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from contact import ContactInitials, ContactPhoto, ContactPhoneNumbers, ContactEmailsHomepage, \
    ContactBirthdaysAnniversary, ContactGroup, ContactNotes
import unittest


class TestAddNewContact(unittest.TestCase):
    def setUp(self):
        self.wd = webdriver.Firefox()
        self.wd.implicitly_wait(30)

    def open_home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, username, password):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(username)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//input[@value='Login']").click()

    def init_add_new_contact(self, wd):
        wd.find_element_by_link_text("add new").click()

    def fill_personal_information(self, wd, contact):
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

    def attach_photo(self, wd, contact):
        wd.find_element_by_name("photo").send_keys(contact.photo)

    def fill_phone_numbers(self, wd, contact):
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

    def fill_emails_and_homepage(self, wd, contact):
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_name("email3").clear()
        wd.find_element_by_name("email3").send_keys(contact.email3)
        wd.find_element_by_name("homepage").clear()
        wd.find_element_by_name("homepage").send_keys(contact.homepage)

    def select_birth_date(self, wd, contact):
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

    def select_belonging_group(self, wd, contact):
        wd.find_element_by_name("new_group").click()
        Select(wd.find_element_by_name("new_group")).select_by_visible_text(contact.group)
        wd.find_element_by_name("new_group").click()

    def fill_secondary_information(self, wd, contact):
        # Fill secondary address
        wd.find_element_by_name("address2").clear()
        wd.find_element_by_name("address2").send_keys(contact.address2)
        # Fill secondary phone number
        wd.find_element_by_name("phone2").clear()
        wd.find_element_by_name("phone2").send_keys(contact.phone_number_2)
        # Fill notes
        wd.find_element_by_name("notes").clear()
        wd.find_element_by_name("notes").send_keys(contact.notes)

    def confirm_group_creation(self, wd):
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def test_add_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.init_add_new_contact(wd)
        self.fill_personal_information(wd,
                                       ContactInitials(firstname="Nickolay", middlename="Igorevich", lastname="Efimov",
                                                       nickname="kolya", title="Title", company="Company",
                                                       address="Address"))
        self.attach_photo(wd, ContactPhoto("D:\\testpicture.jpg"))
        self.fill_phone_numbers(wd, ContactPhoneNumbers(home_phone="HomePhone", work_phone="MobilePhone",
                                                        mobile_phone="WorkPhone", fax_number="FaxNumber"))
        self.fill_emails_and_homepage(wd, ContactEmailsHomepage(email="email1@mail.ru", email2="email2@mail.ru",
                                                                email3="email3@mail.ru", homepage="homepage.ru"))
        self.select_birth_date(wd,
                               ContactBirthdaysAnniversary(birth_day="17", birth_month="November", birth_year="1995",
                                                           anniversary_day="18", anniversary_month="December",
                                                           anniversary_year="1996"))
        self.select_belonging_group(wd, ContactGroup(group="gav1"))
        self.fill_secondary_information(wd,
                                        ContactNotes(address2="address", phone_number_2="HomeAddress", notes="Notes"))
        self.confirm_group_creation(wd)
        self.logout(wd)

    def test_add_empty_contact(self):
        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, username="admin", password="secret")
        self.init_add_new_contact(wd)
        self.fill_personal_information(wd, ContactInitials(firstname="", middlename="", lastname="",
                                                           nickname="", title="", company="", address=""))
       # self.attach_photo(wd, ContactPhoto(""))
        self.fill_phone_numbers(wd, ContactPhoneNumbers(home_phone="", work_phone="",
                                                        mobile_phone="", fax_number=""))
        self.fill_emails_and_homepage(wd, ContactEmailsHomepage(email="", email2="",
                                                                email3="", homepage=""))
        self.select_birth_date(wd, ContactBirthdaysAnniversary(birth_day="", birth_month="-", birth_year="",
                                                               anniversary_day="", anniversary_month="-",
                                                               anniversary_year=""))
        self.select_belonging_group(wd, ContactGroup(group=""))
        self.fill_secondary_information(wd, ContactNotes(address2="", phone_number_2="", notes=""))
        self.confirm_group_creation(wd)
        self.logout(wd)

    def is_element_present(self, how, what):
        try:
            self.wd.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    def is_alert_present(self):
        try:
            self.wd.switch_to_alert()
        except NoAlertPresentException as e:
            return False
        return True

    def tearDown(self):
        self.wd.quit()


if __name__ == "__main__":
    unittest.main()
