"""
Module contains class to test employee model.
"""
# pylint: disable=no-member
from department_app import db
from department_app.models.employee_model import Employee
from department_app.tests.conftest import BaseTest


class TestEmployee(BaseTest):
    """
    Class for employee model test cases
    """

    def test_employee_model(self):
        """
        Testing if the string representation of
        employee is correct
        """
        employee = Employee(uuid='2',
                            full_name='John Smith',
                            salary=15000,
                            date_of_birth='1987-06-06',
                            position='engineer',
                            department_uuid='a4152167-a788-4c39-a232-d45a205aa678')
        db.session.add(employee)
        db.session.commit()
        self.assertEqual('John Smith', repr(employee))
