from department_app.loader import db
from department_app.tests.conftest import BaseTest
from department_app.models.employee_model import Employee
from department_app.models.department_model import Department
from department_app.service import employee_service


class TestEmployeeServices(BaseTest):
    @staticmethod
    def create_department():
        department = Department(name='department', description='description')
        db.session.add(department)

    @staticmethod
    def fill_db():
        employee1 = Employee(full_name='John Smith', salary=15000, date_of_birth='1987-06-06', position='engineer',
                             department_id=1)
        db.session.add(employee1)

    def test_get_all_employees(self):
        self.create_department()
        self.fill_db()
        employee2 = Employee(full_name='Steve Jobs', salary=15000, date_of_birth='1987-06-06', position='engineer',
                             department_id=1)
        db.session.add(employee2)
        db.session.commit()
        self.assertEqual(2, len(employee_service.get_all_employees()))

    def test_add_new_employee(self):
        self.create_department()
        employee_service.add_new_employee('Steve Jobs', 15000, '1987-06-06', 'engineer', 1)
        self.assertEqual(1, Employee.query.count())

    def test_update_employee(self):
        self.create_department()
        self.fill_db()
        employee_service.update_employee(1, 'Steve Jobs', 10000, '1955-04-27', 'engineer2', 1)
        employee = Employee.query.get(1)
        self.assertEqual('Steve Jobs', employee.full_name)
        self.assertEqual(10000, employee.salary)
        self.assertEqual('1955-04-27', str(employee.date_of_birth))
        self.assertEqual('engineer2', employee.position)
        self.assertEqual(1, employee.department_id)

    def test_delete_employee(self):
        self.create_department()
        self.fill_db()
        employee_service.delete_employee(1)
        self.assertEqual(0, Employee.query.count())

    def test_get_employee_with_date_of_birth(self):
        self.create_department()
        self.fill_db()
        self.assertEqual(Employee.query.all(), employee_service.get_employee_with_date_of_birth('1987-06-06'))
        self.assertEqual(Employee.query.all(),
                         employee_service.get_employee_with_date_of_birth('1982-04-16', '1990-06-27'))

