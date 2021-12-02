import http

from werkzeug.security import generate_password_hash

from department_app.loader import db
from department_app.tests.conftest import BaseTest
from department_app.models.user_model import User


class TestAuthViews(BaseTest):

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_login(self):
        response = self.app.get('/login/')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_login_post(self):
        user = User(username='test', email='email', psw_hash=generate_password_hash('password'))
        db.session.add(user)
        db.session.commit()
        response = self.app.post('/login/',
                                 data={'username': 'test',
                                       'password': 'password'},
                                 follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_login_post_incorrect(self):
        response = self.app.post('/login/',
                                 data={'username': 'sdfsf',
                                       'password': 'sfsf'},
                                 follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_register(self):
        response = self.app.get('/register/')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_register_post(self):
        response = self.app.post('/register/',
                                 data={'username': 'test',
                                       'email': 'mail',
                                       'password': 'password'},
                                 follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_register_post_incorrect_username(self):
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
        response = self.app.get('/logout', follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
