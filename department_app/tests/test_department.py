from department_app.app import db
from department_app.models.department_model import Department
from department_app.tests.conftest import BaseTest


class TestDepartment(BaseTest):
    """
    Class for department model test cases
    """
    def test_department_model(self):
        """
        Testing if the string representation of
        department is correct
        """
        department = Department(name='test_department', description='test')
        # pylint: disable=no-member
        db.session.add(department)
        db.session.commit()
        self.assertEqual('<Department test_department>', repr(department))