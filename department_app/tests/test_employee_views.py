"""
Module contains class to test employees views.
"""
import http

from department_app import db
from department_app.tests.conftest import BaseTest
from department_app.models.department_model import Department


class TestEmployeeViews(BaseTest):
    """
    Class for employees views test cases.
    """

    def test_employees(self):
        """
        Test '/employees/' route
        """
        response = self.app.get('/employees/')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_employees_with_params(self):
        """
        Test '/employees/<uuid>' route
        """
        response = self.app.get('/employees/a4152167-a788-4c39-a232-d45a205aa678')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_employees_post(self):
        """
        Test '/employees/' route for post request
        """
        response = self.app.post('/employees/',
                                 data={'uuid': '1',
                                       'full_name': 'test name',
                                       'salary': 2000,
                                       'date_of_birth': '1975-05-23',
                                       'position': 'test position',
                                       'department': 'a4152167-a788-4c39-a232-d45a205aa678'},
                                 follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_add_employee(self):
        """
        Test '/employees/add/' route
        """
        response = self.app.get('/employees/add/')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_add_employee_post(self):
        """
        Test '/employees/add/' route for post request
        """
        department = Department(uuid='3', name='department1', description='description1')
        db.session.add(department)
        db.session.commit()
        response = self.app.post('/employees/add/',
                                 data={'full_name': 'test name',
                                       'salary': 2000,
                                       'date_of_birth': '1975-05-23',
                                       'position': 'test position',
                                       'department': 'a4152167-a788-4c39-a232-d45a205aa678'},
                                 follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_delete_employee(self):
        """
        Test '/employees/delete/<uuid>' route
        """
        response = self.app.post('/employees/delete/1', follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
