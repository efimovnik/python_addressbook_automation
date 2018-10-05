from model.group import Group


def test_edit_first_group(app):
    app.group.edit_first_group(Group(name="name_edited", header="header_edited", footer="footer_edited"))

