from selenium.webdriver.support.ui import Select


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

    def edit(self, contact):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_first_contact()
        self.init_edit_contact()
        self.fill_contact_form_without_group(contact)
        # Confirm editing creation of new contact
        wd.find_element_by_name("update").click()

    def edit_in_details(self, contact):
        wd = self.app.wd
        self.see_details_of_contact()
        self.init_modify_contact()
        self.fill_contact_form_without_group(contact)
        # Confirm editing creation of new contact
        wd.find_element_by_xpath("//input[@value='Update']").click()

    def delete_contact_in_details(self):
        wd = self.app.wd
        self.open_contacts_page()
        self.see_details_of_contact()
        self.init_modify_contact()
        self.click_delete_contact(wd)

    def delete_first_contact(self):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_first_contact()
        self.click_delete_contact(wd)
        # submit delete contact
        wd.switch_to_alert().accept()

    def delete_contact_in_edit_form(self):
        wd = self.app.wd
        self.open_contacts_page()
        self.select_first_contact()
        self.init_edit_contact()
        self.click_delete_contact(wd)

    def delete_all_contacts(self):
        wd = self.app.wd
        # select all contacts
        wd.find_element_by_id("MassCB").click()
        self.click_delete_contact(wd)
        # submit delete contact
        wd.switch_to_alert().accept()

# Assistive test methods

    def fill_contact_form_without_group(self, contact):
        wd = self.app.wd
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

    def fill_contact_form(self, contact):
        self.change_contact_field("firstname", contact.firstname)
        self.change_contact_field("middlename", contact.middlename)
        self.change_contact_field("lastname", contact.middlename)
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

    def transfer_contact_to_group(self, group_transfer):
        wd = self.app.wd
        self.select_first_contact()
        # select group to transfer
        wd.find_element_by_name("to_group").click()
        Select(wd.find_element_by_name("to_group")).select_by_visible_text(group_transfer)
        # submit add to group to transfer
        wd.find_element_by_name("add").click()

    def select_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def click_delete_contact(self, wd):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Delete']").click()

    def init_modify_contact(self):
        wd = self.app.wd
        wd.find_element_by_name("modifiy").click()

    def init_edit_contact(self):
        wd = self.app.wd
        if not len(wd.find_elements_by_name("update")) > 0:
            wd.find_element_by_css_selector("img[alt=\"Edit\"]").click()

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

    def see_details_of_contact(self):
        wd = self.app.wd
        if not len(wd.find_elements_by_name("modifiy")) > 0:
            wd.find_element_by_css_selector("img[alt=\"Details\"]").click()

    def confirm_contact_creation(self):
        wd = self.app.wd
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
