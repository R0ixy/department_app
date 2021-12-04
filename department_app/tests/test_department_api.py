"""
Module contains class to test department api.
"""
import http
import json

from department_app.tests.conftest import BaseTest
from department_app.models.department_model import Department
from department_app import db


class TestDepartmentApi(BaseTest):
    """
    Class for department api test cases.
    """

    @staticmethod
    def fill_db():
        """
        Fill database with test data.
        :return:
        """
        department = Department(name='Test Department', description='Test Description')
        # pylint: disable=no-member
        db.session.add(department)
        db.session.commit()

    def test_get(self):
        """
        Test get request.
        """
        self.fill_db()
        response = self.app.get('/api/departments/')
        assert response.status_code == http.HTTPStatus.OK

    def test_post(self):
        """
        Test post request.
        """
        data = {
            'name': 'Test Department1',
            'description': 'Test Description1'
        }
        response = self.app.post('/api/departments/', data=json.dumps(data),
                                 content_type='application/json')
        assert response.status_code == http.HTTPStatus.CREATED

    def test_wrong_post(self):
        """
        Test post request exception.
        """
        data = {
            'wrong_data': 'wrong data'
        }
        response = self.app.post('/api/departments/', data=json.dumps(data),
                                 content_type='application/json')
        assert response.status_code == http.HTTPStatus.BAD_REQUEST

    def test_put(self):
        """
        Test put request.
        """
        self.fill_db()
        data = {
            'id': 1,
            'name': 'New Department',
            'description': 'New Description'
        }
        response = self.app.put('/api/departments/', data=json.dumps(data),
                                content_type='application/json')
        assert response.status_code == http.HTTPStatus.OK

    def test_wrong_put(self):
        """
        Test put request exception.
        """
        self.fill_db()
        data = {
            'wrong_data': 'wrong data'
        }
        response = self.app.put('/api/departments/', data=json.dumps(data),
                                content_type='application/json')
        assert response.status_code == http.HTTPStatus.BAD_REQUEST

    def test_delete(self):
        """
        Test delete request.
        """
        self.fill_db()
        data = {
            'id': 1,
        }
        response = self.app.delete('/api/departments/', data=json.dumps(data),
                                   content_type='application/json')
        assert response.status_code == http.HTTPStatus.OK

    def test_wrong_delete_data(self):
        """
        Test delete request exception because of wrong data.
        """
        self.fill_db()
        data = {
            'id': 1780,
        }
        response = self.app.delete('/api/departments/', data=json.dumps(data),
                                   content_type='application/json')
        assert response.status_code == http.HTTPStatus.NOT_FOUND

    def test_wrong_delete_args(self):
        """
        Test delete request exception because of wrong args.
        """
        self.fill_db()
        data = {
            'wrong_data': 1,
        }
        response = self.app.delete('/api/departments/', data=json.dumps(data),
                                   content_type='application/json')
        assert response.status_code == http.HTTPStatus.BAD_REQUEST
