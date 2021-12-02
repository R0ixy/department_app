import http

from department_app.loader import db
from department_app.tests.conftest import BaseTest


class TestAuthViews(BaseTest):

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_login(self):
        response = self.app.get('/login/')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_register_post(self):
        response = self.app.post('/register/',
                                 data={'username': 'test',
                                       'email': 'mail',
                                       'password': 'password'},
                                 follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_login_post(self):
        response = self.app.post('/login/',
                                 data={'username': 'test',
                                       'password': 'password'},
                                 follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_register(self):
        response = self.app.get('/register/')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_logout(self):
        response = self.app.get('/logout', follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
