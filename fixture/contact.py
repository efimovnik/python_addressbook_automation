from selenium.webdriver.support.ui import Select
from model.contact import Contact, ContactUpd
from random import randrange
import re


class ContactHelper:

    def __init__(self, app):
        self.app = app

# Main test methods
    def open_contacts_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("http://localhost/addressbook/")):
            wd.find_element_by_link_text("home").click()

    def init_add_new_contact(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("add new")) > 0):
            wd.find_element_by_link_text("add new").click()

    def create(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        self.init_add_new_contact()
        self.fill_contact_form(contact)
        self.confirm_contact_creation()
        self.contact_cache = None

    def edit_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contacts_page()
        self.init_edit_contact_by_index(index)
        self.fill_contact_form_without_group(contact)
        # Confirm editing creation of new contact
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def edit_by_id(self, id, contact):
        wd = self.app.wd
        self.open_contacts_page()
        self.init_edit_contact_by_id(id)
        self.fill_contact_form_without_group(contact)
        # Confirm editing creation of new contact
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    def edit(self, contact):
        self.edit_by_index(0, contact)

    def edit_in_details_by_index(self, index, contact):
        wd = self.app.wd
        self.see_details_of_contact_by_index(index)
        self.init_modify_contact()
        self.fill_contact_form_without_group(contact)
        # Confirm editing creation of new contact
        wd.find_element_by_xpath("//input[@value='Update']").click()
        self.contact_cache = None

    def edit_in_details_by_id(self, id, contact):
        wd = self.app.wd
        self.see_details_of_contact_by_id(id)
        self.init_modify_contact()
        self.fill_contact_form_without_group(contact)
        # Confirm editing creation of new contact
        wd.find_element_by_xpath("//input[@value='Update']").click()
        self.contact_cache = None

    def edit_in_details(self, contact):
        self.edit_in_details_by_index(0, contact)

    def delete_contact_in_details(self):
        self.delete_contact_by_index(0)

    def delete_contact_in_details_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.see_details_of_contact_by_index(index)
        self.init_modify_contact()
        self.click_delete_contact(wd)
        self.contact_cache = None

    def delete_contact_in_details_by_id(self, id):
        wd = self.app.wd
        self.open_contacts_page()
        self.see_details_of_contact_by_id(id)
        self.init_modify_contact()
        self.click_delete_contact(wd)
        self.contact_cache = None

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_index(index)
        self.click_delete_contact(wd)
        # submit delete contact
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_contact_by_id(id)
        self.click_delete_contact(wd)
        # submit delete contact
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_in_edit_form_by_index(self, index):
        wd = self.app.wd
        self.open_contacts_page()
        self.init_edit_contact_by_index(index)
        self.click_delete_contact(wd)
        self.contact_cache = None

    def delete_contact_in_edit_form_by_id(self, id):
        wd = self.app.wd
        self.open_contacts_page()
        self.init_edit_contact_by_id(id)
        self.click_delete_contact(wd)
        self.contact_cache = None

    def delete_contact_in_edit_form(self):
        self.delete_contact_in_edit_form_by_index(0)

    def delete_all_contacts(self):
        wd = self.app.wd
        # select all contacts
        wd.find_element_by_id("MassCB").click()
        self.click_delete_contact(wd)
        # submit delete contact
        wd.switch_to_alert().accept()
        self.contact_cache = None

# Assistive test methods

    def fill_contact_form_without_group(self, contact):
        wd = self.app.wd
        self.change_contact_field("firstname", contact.firstname_upd)
        self.change_contact_field("middlename", contact.middlename_upd)
        self.change_contact_field("lastname", contact.lastname_upd)
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

    def fill_contact_form(self, contact):
        self.change_contact_field("firstname", contact.firstname)
        self.change_contact_field("middlename", contact.middlename)
        self.change_contact_field("lastname", contact.lastname)
        self.change_contact_field("nickname", contact.nickname)
        self.change_contact_field("title", contact.title)
        self.change_contact_field("company", contact.company)
        self.change_contact_field("address", contact.address)
        self.change_photo(contact.photo)
        self.change_contact_field("home", contact.home_phone)
        self.change_contact_field("mobile", contact.mobile_phone)
        self.change_contact_field("work", contact.work_phone)
        self.change_contact_field("fax", contact.fax_number)
        self.change_contact_field("email", contact.email)
        self.change_contact_field("email2", contact.email2)
        self.change_contact_field("email3", contact.email3)
        self.change_contact_field("homepage", contact.homepage)
        self.select_date("bday", contact.birth_day)
        self.select_date("bmonth", contact.birth_month)
        self.change_contact_field("byear", contact.birth_year)
        self.select_date("aday", contact.anniversary_day)
        self.select_date("amonth", contact.anniversary_month)
        self.change_contact_field("ayear", contact.anniversary_year)
        self.change_contact_field("address2", contact.address2)
        self.change_contact_field("phone2", contact.phone_number_2)
        self.change_contact_field("notes", contact.notes)
        self.select_belonging_group(contact.group)

    def select_first_contact(self):
        self.select_contact_by_index(0)

    def select_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_name("selected[]")[index].click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def click_delete_contact(self, wd):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Delete']").click()

    def init_modify_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("modifiy").click()

    def init_edit_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        if not len(wd.find_elements_by_name("update")) > 0:
            wd.find_elements_by_css_selector("img[alt=\"Edit\"]")[index].click()

    def init_edit_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        if not len(wd.find_elements_by_name("update")) > 0:
            wd.find_element_by_xpath('//a[@href="edit.php?id=%s"]' % id).click()

    def init_edit_contact(self):
        self.init_edit_contact_by_index(0)

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

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

    def select_belonging_group(self, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name("new_group").click()
            Select(wd.find_element_by_name("new_group")).select_by_visible_text(text)
            wd.find_element_by_name("new_group").click()

    def see_details_of_contact_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        if not len(wd.find_elements_by_name("modifiy")) > 0:
            wd.find_elements_by_css_selector("img[alt=\"Details\"]")[index].click()

    def see_details_of_contact_by_id(self, id):
        wd = self.app.wd
        self.app.open_home_page()
        if not len(wd.find_elements_by_name("modifiy")) > 0:
            wd.find_element_by_xpath('//a[@href="view.php?id=%s"]' % id).click()

    def see_details_of_contact(self):
        self.see_details_of_contact_by_index(0)

    def confirm_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def transfer_contact_to_group_by_index(self, index, group_transfer):
        wd = self.app.wd
        self.select_contact_by_index(index)
        # select group to transfer
        wd.find_element_by_name("to_group").click()
        Select(wd.find_element_by_name("to_group")).select_by_visible_text(group_transfer)
        # submit add to group to transfer
        wd.find_element_by_name("add").click()

    def transfer_contact_to_group(self):
        wd = self.app.wd
        self.transfer_contact_to_group_by_index(0)

    def transfer_contact_to_group_by_group_index(self, index, index_group):
        wd = self.app.wd
        self.select_contact_by_index(index)
        # select group to transfer
        wd.find_element_by_name("to_group").click()
        groups_for_transfer = self.get_groups_to_transfer_list()
        index_group = randrange(len(groups_for_transfer))
        Select(wd.find_elements_by_name("to_group")).select_by_visible_text(index_group_text)
        # submit add to group to transfer
        wd.find_element_by_name("add").click()

    def get_contact_list(self):
        wd = self.app.wd
        self.app.open_home_page()
        contacts = []
        for element in wd.find_elements_by_name("entry"):
            cells = element.find_elements_by_tag_name("td")
            id = element.find_element_by_name("selected[]").get_attribute("id")
            lastname = cells[1].text
            firstname = cells[2].text
            address = cells[3].text
            all_emails = cells[4].text
            all_phones = cells[5].text
            contacts.append(Contact(lastname=lastname, firstname=firstname, id=id,
                                    address=address, all_emails_from_homepage=all_emails,
                                    all_phones_from_homepage=all_phones))
        return contacts

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.init_edit_contact_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        home_phone = wd.find_element_by_name("home").get_attribute("value")
        work_phone = wd.find_element_by_name("work").get_attribute("value")
        mobile_phone = wd.find_element_by_name("mobile").get_attribute("value")
        phone_number_2 = wd.find_element_by_name("phone2").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        return Contact(firstname=firstname, lastname=lastname, id=id,
                       home_phone=home_phone, work_phone=work_phone,
                       mobile_phone=mobile_phone, phone_number_2=phone_number_2,
                       email=email, email2=email2, email3=email3, address=address)

    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.see_details_of_contact_by_index(index)
        text = wd.find_element_by_id("content").text
        home_phone = re.search("H: (.*)", text).group(1)
        work_phone = re.search("W: (.*)", text).group(1)
        mobile_phone = re.search("M: (.*)", text).group(1)
        phone_number_2 = re.search("P: (.*)", text).group(1)
        return Contact(home_phone=home_phone, work_phone=work_phone,
                       mobile_phone=mobile_phone, phone_number_2=phone_number_2)


    contact_cache = None

    def get_contact_upd_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                cells = element.find_elements_by_tag_name("td")
                id = element.find_element_by_name("selected[]").get_attribute("id")
                self.contact_cache.append(ContactUpd(lastname_upd=cells[1].text, firstname_upd=cells[2].text, id=id))
        return list(self.contact_cache)

    def get_groups_to_transfer_list(self):
        wd = self.app.wd
        groups_to_transfer = []
        for element in wd.find_element_by_name("to group"):
            str = element.find_elements_by_tag_name("option")
            groups_to_transfer.append(str.text)
        return groups_to_transfer