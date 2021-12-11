"""
Module contains class to test employees service.
"""
# pylint: disable=no-member
from department_app import db
from department_app.tests.conftest import BaseTest
from department_app.models.employee_model import Employee
from department_app.service import employee_service


class TestEmployeeServices(BaseTest):
    """
    Class for employee CRUD operations test cases.
    """

    def test_get_all_employees(self):
        """
        Test get all employees operation
        """
        employee2 = Employee(uuid='2',
                             full_name='Steve Jobs',
                             salary=15000,
                             date_of_birth='1987-06-06',
                             position='engineer',
                             department_uuid='a4152167-a788-4c39-a232-d45a205aa678')
        db.session.add(employee2)
        db.session.commit()
        self.assertEqual(2, len(employee_service.get_all_employees()))

    def test_get_one_employee(self):
        """
        Test get one employee operation
        """
        employee = employee_service.get_one_employee('1')
        self.assertEqual('John Smith', employee.full_name)

    def test_add_new_employee(self):
        """
        Test add employee operation
        """
        employee_service.add_new_employee('Steve Jobs',
                                          15000,
                                          '1987-06-06',
                                          'engineer',
                                          'a4152167-a788-4c39-a232-d45a205aa678')
        self.assertEqual(2, Employee.query.count())

    def test_update_employee(self):
        """
        Test update employee operation
        """
        employee_service.update_employee(1,
                                         'Steve Jobs',
                                         10000,
                                         '1955-04-27',
                                         'engineer2',
                                         'a4152167-a788-4c39-a232-d45a205aa678')
        employee = Employee.query.get(1)
        self.assertEqual('Steve Jobs', employee.full_name)
        self.assertEqual(10000, employee.salary)
        self.assertEqual('1955-04-27', str(employee.date_of_birth))
        self.assertEqual('engineer2', employee.position)
        self.assertEqual('a4152167-a788-4c39-a232-d45a205aa678', employee.department_uuid)

    def test_delete_employee(self):
        """
        Test delete employee operation
        """
        employee_service.delete_employee('1')
        self.assertEqual(0, Employee.query.count())

    def test_get_employee_with_params(self):
        """
        Test get employees with params operation
        """
        self.assertEqual(Employee.query.all(),
                         employee_service.get_employee_with_params(first_date='1987-06-06'))
        self.assertEqual(Employee.query.all(),
                         employee_service.get_employee_with_params(
                             first_date='1982-04-16', second_date='1990-06-27'))
        self.assertEqual(Employee.query.all(), employee_service.get_employee_with_params())

    def test_update_employee_patch(self):
        """
        Test update patch department operation
        """
        employee_service.update_employee_patch(1, name='Steve')
        employee_service.update_employee_patch(1,
                                               salary=10000,
                                               birthday='1955-04-27',
                                               position='engineer2',
                                               department='a4152167-a788-4c39-a232-d45a205aa678')
        employee = Employee.query.get(1)
        self.assertEqual('Steve', employee.full_name)
        self.assertEqual(10000, employee.salary)
