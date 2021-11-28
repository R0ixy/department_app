from ..loader import db
from ..models.department_model import Department
from ..tests.conftest import BaseTest


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