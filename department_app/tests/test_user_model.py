from department_app.loader import db
from department_app.models.user_model import User
from department_app.tests.conftest import BaseTest


class TestUser(BaseTest):
    def test_user_model(self):
        user = User(username='test_user', email='test_email', psw_hash='test_psw_hash')
        # pylint: disable=no-member
        db.session.add(user)
        db.session.commit()
        self.assertEqual('test_user', repr(user))
