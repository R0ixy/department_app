import http
import json
from department_app.tests.conftest import BaseTest
from department_app.models.department_model import Department
from department_app.loader import db


class TestDepartmentApi(BaseTest):

    def test_get(self):
        response = self.app.get('/api/department/')
        assert response.status_code == http.HTTPStatus.OK

    def test_post(self):
        data = {
            'name': 'Test Department1',
            'description': 'Test Description1'
        }
        response = self.app.post('/api/department/', data=json.dumps(data),
                                 content_type='application/json')
        assert response.status_code == http.HTTPStatus.CREATED

    def test_put(self):
        department = Department(name='Test Department', description='Test Description')
        # pylint: disable=no-member
        db.session.add(department)
        data = {
            'id': 1,
            'name': 'New Department',
            'description': 'New Description'
        }
        response = self.app.put('/api/department/', data=json.dumps(data),
                                content_type='application/json')
        assert response.status_code == http.HTTPStatus.OK

    def test_delete(self):
        department = Department(name='Test Department', description='Test Description')
        # pylint: disable=no-member
        db.session.add(department)
        data = {
            'id': 1,
        }
        response = self.app.delete('/api/department/', data=json.dumps(data),
                                   content_type='application/json')
        assert response.status_code == http.HTTPStatus.OK
