import http

from department_app.loader import db
from department_app.tests.conftest import BaseTest
from department_app.models.department_model import Department


class TestDepartmentViews(BaseTest):
    @staticmethod
    def fill_db():
        department = Department(name='department1', description='description1')
        db.session.add(department)
        db.session.commit()

    def test_departments(self):
        response = self.app.get('/departments/')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_departments_post(self):
        self.fill_db()
        response = self.app.post('/departments/',
                                 data={'id': 1, 'title': 'test name', 'description': 'test description'},
                                 follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_add_department_get(self):
        response = self.app.get('/departments/add/')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_add_department_post(self):
        response = self.app.post('/departments/add/', data={'title': 'test name', 'description': 'test description'},
                                 follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_delete_department(self):
        self.fill_db()
        response = self.app.post('/departments/delete/1',
                                 follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
