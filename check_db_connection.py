from fixture.orm import ORMFixture
from model.group import Group


dbm = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    l = dbm.get_group_named(Group(name="gav1"))
    for item in l:
        print (item)
    print (len(l))
finally:
    pass # db.destroy()


