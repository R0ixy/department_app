"""
Module contains class to test user model.
"""
# pylint: disable=no-member
from department_app import db
from department_app.models.user_model import User
from department_app.tests.conftest import BaseTest


class TestUser(BaseTest):
    """
    Class for user model test cases
    """

    def test_user_model(self):
        """
        Testing if the string representation of
        user is correct
        """
        user = User(username='test_user', email='test_email', psw_hash='test_psw_hash')
        db.session.add(user)
        db.session.commit()
        self.assertEqual('test_user', repr(user))
