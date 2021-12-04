"""
Module contains class to test auth service.
"""
# pylint: disable=no-member
from department_app import db
from department_app.tests.conftest import BaseTest
from department_app.models.user_model import User
from department_app.service import auth_service


class TestAuthService(BaseTest):
    """
    Class for auth CRUD operation test cases.
    """

    @staticmethod
    def fill_db():
        """
        Fill database with test data.
        """
        user = User(username='test_user', email='test_email', psw_hash='test_psw_hash')
        # pylint: disable=no-member
        db.session.add(user)
        db.session.commit()

    def test_username_exists(self):
        """
        Test if username exists.
        """
        self.fill_db()
        self.assertEqual(True, auth_service.username_exists('test_user'))

    def test_not_username_exists(self):
        """
        Test if username don't exist.
        """
        self.fill_db()
        self.assertEqual(False, auth_service.username_exists('sgfhs'))

    def test_email_exists(self):
        """
        Test if email exists.
        """
        self.fill_db()
        self.assertEqual(True, auth_service.email_exists('test_email'))

    def test_not_email_exists(self):
        """
        Test if email don't exist.
        """
        self.fill_db()
        self.assertEqual(False, auth_service.email_exists('fdfs'))

    def test_new_user(self):
        """
        Test add new user operation.
        """
        auth_service.new_user('test_user', 'test_email', 'test_psw_hash')
        self.assertEqual(1, User.query.count())

    def test_get_user(self):
        """
        Test get user operation.
        """
        self.fill_db()
        user = auth_service.get_user('test_user')
        self.assertEqual('test_user', user.username)
