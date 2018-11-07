from fixture.orm import ORMFixture
from model.group import Group
import random


db = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")


l = db.get_contacts_in_group(Group(id='143'))
contacts = db.get_contact_list()
contact = random.choice(contacts)
for item in l:
    if item == contact:
        print (contact)
        print (item)
        print (len(l))
        ok = []
        ok.append(item)
if len(ok) == 0:
    raise AssertionError("There's no any contact in group id 69")

