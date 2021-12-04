"""
Module contains class to test department views.
"""
# pylint: disable=no-member
import http

from department_app.loader import db
from department_app.tests.conftest import BaseTest
from department_app.models.department_model import Department


class TestDepartmentViews(BaseTest):
    """
    Class for department views test cases.
    """

    @staticmethod
    def fill_db():
        """
        Fill database with test data.
        """
        department = Department(name='department1', description='description1')
        db.session.add(department)
        db.session.commit()

    def test_departments(self):
        """
        Test '/departments/' route
        """
        response = self.app.get('/departments/')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_departments_post(self):
        """
        Test '/departments/' route for post request
        """
        self.fill_db()
        response = self.app.post('/departments/',
                                 data={'id': 1,
                                       'title': 'test name',
                                       'description': 'test description'},
                                 follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_add_department_get(self):
        """
        Test '/departments/add/' route
        """
        response = self.app.get('/departments/add/')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_add_department_post(self):
        """
        Test '/departments/add/' route for post request
        """
        response = self.app.post('/departments/add/', data={'title': 'test name',
                                                            'description': 'test description'},
                                 follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_delete_department(self):
        """
        Test '/departments/delete/<id>' route
        """
        self.fill_db()
        response = self.app.post('/departments/delete/1',
                                 follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
