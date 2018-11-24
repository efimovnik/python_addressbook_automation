import pymysql.cursors
from model.group import Group
from model.contact import Contact, ContactUpd


class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = pymysql.connect(host=host, database=name, user=user, password=password, autocommit=True)

    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
        finally:
            cursor.close()
        return list

    def get_contact_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname, address, email, email2, "
                           "email3, home, work, mobile, phone2 from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname, address, email, email2, email3, home, work, mobile, phone2) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname,
                                    address=address, email=email, email2=email2, email3=email3,
                                    home_phone=home, work_phone=work, mobile_phone=mobile, phone_number_2=phone2))
        finally:
            cursor.close()
        return list

    def get_contact_upd_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00'")
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(ContactUpd(id=str(id), firstname_upd=firstname, lastname_upd=lastname))
        finally:
            cursor.close()
        return list

    def get_contacts_count(self):
        return len(self.get_contact_list())

    def get_groups_count(self):
        return len(self.get_group_list())

    def get_group_named(self, group_name):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, group_header, group_footer from group_list where group_name = '%s'" % (group_name))
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=str(name), header=header, footer=footer))
        finally:
            cursor.close()
        return len(list)

    def get_contacts_in_group(self, group_id):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select id, firstname, lastname from addressbook where deprecated='0000-00-00 00:00:00' and id in (select id from address_in_groups where group_id = '%s')" % (group_id))
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list

    def get_contacts_not_in_group(self, group_id):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute(
                "select id, firstname, lastname and deprecated from addressbook where deprecated='0000-00-00 00:00:00' and id not in (select id from address_in_groups where group_id = '%s')" % (group_id))
            for row in cursor:
                (id, firstname, lastname) = row
                list.append(Contact(id=str(id), firstname=firstname, lastname=lastname))
        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()
