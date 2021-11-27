from department_app.app import db
from department_app.tests.base import BaseTest
from department_app.models.department_model import Department
from department_app.service import department_service


class TestDepartmentServices(BaseTest):
    def test_get_all_departments(self):
        department1 = Department(name='department1', description='description1')
        department2 = Department(name='department2', description='description2')

        db.session.add(department1)
        db.session.add(department2)
        db.session.commit()
        self.assertEqual(2, len(department_service.get_all_departments()))
