from department_app.app import db
from department_app.tests.conftest import BaseTest
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

    def test_add_department(self):
        department_service.add_new_department('department1', 'description')
        self.assertEqual(1, Department.query.count())

    def test_update_department(self):
        department_service.add_new_department('department1', 'description')
        department_service.update_department(1, 'new_department', 'new_description')
        department = Department.query.get(1)
        self.assertEqual('new_department', department.name)
        self.assertEqual('new_description', department.description)

    def test_delete_department(self):
        department_service.add_new_department('department1', 'description1')
        department_service.delete_department(1)
        self.assertEqual(0, Department.query.count())
