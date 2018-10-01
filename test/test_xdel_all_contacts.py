
def test_del_all_contacts(app):
    app.session.login(login="admin", password="secret")
    app.contact.delete_all_contacts()
    app.session.logout()
