
def test_del_contact_in_edit(app):
    app.session.login(login="admin", password="secret")
    app.contact.delete_contact_in_edit_form()
    app.session.logout()