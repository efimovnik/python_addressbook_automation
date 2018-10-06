

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def open_groups_page(self):
        wd = self.app.wd
        # open groups page
        wd.find_element_by_link_text("groups").click()

    def create(self, group):
        wd = self.app.wd
        self.open_groups_page()
        # init group creation
        wd.find_element_by_name("new").click()
        # fill group form
        self.change_field_name("group_name", group.name)
        self.change_field_name("group_header", group.header)
        self.change_field_name("group_footer", group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        # return to groups page
        self.return_to_groups_page()

    def delete_first_group(self):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # submit delete group
        wd.find_element_by_name("delete").click()
        # return to groups page
        self.return_to_groups_page()

    def edit_first_group(self, group):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # init edit group
        wd.find_element_by_name("edit").click()
        # fill edited group form
        self.fill_group_form(group)
        # submit edit group
        wd.find_element_by_name("update").click()
        # return to groups page
        self.return_to_groups_page()

    def change_field_name(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_group_form(self, group):
        wd = self.app.wd
        self.change_field_name("group_name", group.name)
        self.change_field_name("group_header", group.header)
        self.change_field_name("group_footer", group.footer)

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element_by_name("selected[]").click()

    def modify_first_group(self, new_group_data):
        wd = self.app.wd
        self.open_groups_page()
        self.select_first_group()
        # init edit group
        wd.find_element_by_name("edit").click()
        # fill edited group form
        self.fill_group_form(new_group_data)
        # submit edit group
        wd.find_element_by_name("update").click()
        # return to groups page
        self.return_to_groups_page()

    def count(self):
        wd = self.app.wd
        self.open_groups_page()
        return len(wd.find_elements_by_name("selected[]"))

    def count_group_named(self, group_name):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_groups_page()
        return wd.find_element_by_name("selected[]").text == group_name


    def return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element_by_link_text("group page").click()