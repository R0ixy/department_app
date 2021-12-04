"""
Module contains class to test auth views.
"""
# pylint: disable=no-member
import http

from werkzeug.security import generate_password_hash

from department_app.loader import db
from department_app.tests.conftest import BaseTest
from department_app.models.user_model import User


class TestAuthViews(BaseTest):
    """
    Class for auth views test cases.
    """

    def test_index(self):
        """
        Test '/' route
        """
        response = self.app.get('/')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_login(self):
        """
        Test '/login' route
        """
        response = self.app.get('/login/')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_login_post(self):
        """
        Test '/login' route for post request
        """
        user = User(username='test', email='email', psw_hash=generate_password_hash('password'))
        db.session.add(user)
        db.session.commit()
        response = self.app.post('/login/',
                                 data={'username': 'test',
                                       'password': 'password'},
                                 follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_login_post_incorrect(self):
        """
        Test '/login' route for post request with incorrect data.
        """
        response = self.app.post('/login/',
                                 data={'username': 'sdfsf',
                                       'password': 'sfsf'},
                                 follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_register(self):
        """
        Test '/register' route
        """
        response = self.app.get('/register/')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_register_post(self):
        """
        Test '/register' route for post request
        """
        response = self.app.post('/register/',
                                 data={'username': 'test',
                                       'email': 'mail',
                                       'password': 'password'},
                                 follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_register_post_incorrect_username(self):
        """
        Test '/register' route for post request with incorrect username.
        """
        user = User(username='test', email='email', psw_hash=generate_password_hash('password'))
        db.session.add(user)
        db.session.commit()
        response = self.app.post('/register/',
                                 data={'username': 'test',
                                       'email': 'mail',
                                       'password': 'password'},
                                 follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_register_post_incorrect_email(self):
        """
        Test '/register' route for post request with incorrect email.
        """
        user = User(username='test', email='email', psw_hash=generate_password_hash('password'))
        db.session.add(user)
        db.session.commit()
        response = self.app.post('/register/',
                                 data={'username': 'testuser',
                                       'email': 'email',
                                       'password': 'password'},
                                 follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_logout(self):
        """
        Test '/logout' route.
        """
        response = self.app.get('/logout', follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
