"""
Module contains class to test department api.
"""
import http
import json

from department_app.tests.conftest import BaseTest


class TestDepartmentApi(BaseTest):
    """
    Class for department api test cases.
    """

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
        data = {
            'name': 'New Department',
            'description': 'New Description'
        }
        response = self.app.put('/api/departments/a4152167-a788-4c39-a232-d45a205aa678', data=json.dumps(data),
                                content_type='application/json')
        assert response.status_code == http.HTTPStatus.OK

    def test_wrong_put(self):
        """
        Test put request exception.
        """
        data = {
            'wrong_data': 'wrong data'
        }
        response = self.app.put('/api/departments/a4152167-a788-4c39-a232-d45a205aa678', data=json.dumps(data),
                                content_type='application/json')
        assert response.status_code == http.HTTPStatus.BAD_REQUEST

    def test_delete(self):
        """
        Test delete request.
        """
        response = self.app.delete('/api/departments/a4152167-a788-4c39-a232-d45a205aa678',
                                   content_type='application/json')
        assert response.status_code == http.HTTPStatus.OK

    def test_wrong_delete(self):
        """
        Test delete request exception.
        """
        response = self.app.delete('/api/departments/1780',
                                   content_type='application/json')
        assert response.status_code == http.HTTPStatus.NOT_FOUND

    def test_get_one(self):
        """
        Test get by uuid request.
        """
        response = self.app.get('/api/departments/a4152167-a788-4c39-a232-d45a205aa678')
        assert response.status_code == http.HTTPStatus.OK

    def test_get_wrong_one(self):
        """
        Test get by uuid request exception.
        """
        response = self.app.get('/api/departments/241')
        assert response.status_code == http.HTTPStatus.NOT_FOUND

    def test_patch(self):
        """
        Test patch request.
        """
        data = {
            'name': 'New Department',
        }
        response = self.app.patch('/api/departments/a4152167-a788-4c39-a232-d45a205aa678', data=json.dumps(data),
                                  content_type='application/json')
        assert response.status_code == http.HTTPStatus.OK

    def test_wrong_patch(self):
        """
        Test patch request exception.
        """
        data = {
            'name': 'New Department',
        }
        response = self.app.patch('/api/departments/241', data=json.dumps(data),
                                  content_type='application/json')
        assert response.status_code == http.HTTPStatus.NOT_FOUND

    def test_wrong_args_patch(self):
        """
        Test patch request exception.
        """
        data = {
            'wrong_data': 'wrong_data',
        }
        response = self.app.patch('/api/departments/a4152167-a788-4c39-a232-d45a205aa678', data=json.dumps(data),
                                  content_type='application/json')
        assert response.status_code == http.HTTPStatus.BAD_REQUEST

    def test_name_validation(self):
        """
        Test name validation.
        """
        data = {
            'name': 'wronghfsjfhsjfhhhhhhhhhhhhhhhhhhhhhhhhsfjkshgsjkdghsdjkghsjkghsjkghsgjshgjkshgjkshgsjghsjdata',
            'description': 'normal_description',
        }
        response1 = self.app.post('/api/departments/', data=json.dumps(data),
                                  content_type='application/json')
        response2 = self.app.patch('/api/departments/a4152167-a788-4c39-a232-d45a205aa678', data=json.dumps(data),
                                   content_type='application/json')
        response3 = self.app.put('/api/departments/a4152167-a788-4c39-a232-d45a205aa678', data=json.dumps(data),
                                 content_type='application/json')
        assert response1.status_code == http.HTTPStatus.BAD_REQUEST
        assert response2.status_code == http.HTTPStatus.BAD_REQUEST
        assert response3.status_code == http.HTTPStatus.BAD_REQUEST
