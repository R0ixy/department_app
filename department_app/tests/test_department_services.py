"""
Module contains class to test department service.
"""
# pylint: disable=no-member
from department_app import db
from department_app.tests.conftest import BaseTest
from department_app.models.department_model import Department
from department_app.models.employee_model import Employee
from department_app.service import department_service


class TestDepartmentServices(BaseTest):
    """
    Class for department CRUD operations test cases.
    """

    def test_get_all_departments(self):
        """
        Test get all departments operation
        """
        department2 = Department(uuid='2', name='department2', description='description2')
        db.session.add(department2)
        db.session.commit()
        self.assertEqual(2, len(department_service.get_all_departments()))

    def test_add_department(self):
        """
        Test add department operation
        """
        self.assertEqual(1, Department.query.count())

    def test_update_department(self):
        """
        Test update department operation
        """
        department_service.update_department('a4152167-a788-4c39-a232-d45a205aa678', 'new_department',
                                             'new_description')
        department = Department.query.get(1)
        self.assertEqual('new_department', department.name)
        self.assertEqual('new_description', department.description)

    def test_delete_department(self):
        """
        Test delete department operation
        """
        department_service.delete_department('a4152167-a788-4c39-a232-d45a205aa678')
        self.assertEqual(0, Department.query.count())

    @staticmethod
    def add_entries_to_db():
        """
        Fill database with test data.
        """
        employee1 = Employee(uuid='2',
                             full_name='John Smith',
                             salary=15000,
                             date_of_birth='1987-06-06',
                             position='engineer',
                             department_uuid='a4152167-a788-4c39-a232-d45a205aa678')
        db.session.add(employee1)
        db.session.commit()

    def test_get_average_salary(self):
        """
        Test get average salary operation
        """
        self.add_entries_to_db()
        self.assertEqual(17500, department_service.get_average_salary('a4152167-a788-4c39-a232-d45a205aa678'))

    def test_get_number_of_employees(self):
        """
        Test get number of employees operation
        """
        self.add_entries_to_db()
        self.assertEqual(2, department_service.get_number_of_employees('a4152167-a788-4c39-a232-d45a205aa678'))

    def test_get_one_department(self):
        """
        Test get one department operation
        """
        department1 = department_service.get_one_department('a4152167-a788-4c39-a232-d45a205aa678')
        self.assertEqual('Test Department', department1.name)

    def test_update_department_patch(self):
        """
        Test update patch department operation
        """
        department_service.update_department_patch('a4152167-a788-4c39-a232-d45a205aa678', name='new_department')
        department_service.update_department_patch('a4152167-a788-4c39-a232-d45a205aa678',
                                                   description='new description')
        department = Department.query.get(1)
        self.assertEqual('new_department', department.name)
        self.assertEqual('new description', department.description)
