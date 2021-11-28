from department_app.loader import db
from department_app.models.employee_model import Employee
from department_app.models.department_model import Department
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
        department = Department(name='test_department', description='test')
        employee = Employee(full_name='John Smith', salary=15000, date_of_birth='1987-06-06', position='engineer',
                            department_id=1)
        db.session.add(department)
        db.session.add(employee)
        db.session.commit()
        self.assertEqual('<Employee John Smith>', repr(employee))
