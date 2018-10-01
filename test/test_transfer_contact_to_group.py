
def test_transfer_contact_to_group(app):
    app.session.login(login="admin", password="secret")
    app.contact.transfer_contact_to_group(group_transfer="contact_group")
    app.session.logout()
