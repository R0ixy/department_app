"""
Module contains class to test employees views.
"""
import http

from department_app.loader import db
from department_app.tests.conftest import BaseTest
from department_app.models.department_model import Department
from department_app.models.employee_model import Employee


class TestEmployeeViews(BaseTest):
    """
    Class for employees views test cases.
    """

    @staticmethod
    def fill_db():
        """
        Fill database with test data.
        """
        department = Department(name='department1', description='description1')
        employee = Employee(full_name='Jhon Smith',
                            salary=2000,
                            date_of_birth='1982-03-14',
                            position='Developer',
                            department_id=1)
        db.session.add(department)
        db.session.add(employee)
        db.session.commit()

    def test_employees(self):
        """
        Test '/employees/' route
        """
        response = self.app.get('/employees/')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_employees_with_params(self):
        """
        Test '/employees/<id>' route
        """
        response = self.app.get('/employees/1')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_employees_post(self):
        """
        Test '/employees/' route for post request
        """
        self.fill_db()
        response = self.app.post('/employees/',
                                 data={'id': 1,
                                       'full_name': 'test name',
                                       'salary': 2000,
                                       'date_of_birth': '1975-05-23',
                                       'position': 'test position',
                                       'department': 1},
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
        department = Department(name='department1', description='description1')
        db.session.add(department)
        db.session.commit()
        response = self.app.post('/employees/add/',
                                 data={'full_name': 'test name',
                                       'salary': 2000,
                                       'date_of_birth': '1975-05-23',
                                       'position': 'test position',
                                       'department': 1},
                                 follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_delete_employee(self):
        """
        Test '/employees/delete/<id>' route
        """
        self.fill_db()
        response = self.app.post('/employees/delete/1', follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
