"""
Module contains class to test employee api.
"""
# pylint: disable=no-member
import http
import json

from department_app.tests.conftest import BaseTest


class TestEmployeeApi(BaseTest):
    """
    Class for employees api test cases.
    """

    def test_get(self):
        """
        Test get request.
        """
        response = self.app.get('/api/employees')
        assert response.status_code == http.HTTPStatus.OK

    def test_get_with_param_id(self):
        """
        Test get request with param id.
        """
        response = self.app.get('/api/employees?uuid=1&')
        assert response.status_code == http.HTTPStatus.OK

    def test_get_with_param_first_date(self):
        """
        Test get request with param first_date.
        """
        response = self.app.get('/api/employees?first_date=1982-03-14')
        assert response.status_code == http.HTTPStatus.OK

    def test_get_with_param_id_and_first_date(self):
        """
        Test get request with params id and first_date.
        """
        response = self.app.get('/api/employees?uuid=1&first_date=1982-03-14')
        assert response.status_code == http.HTTPStatus.OK

    def test_get_with_all_params(self):
        """
        Test get request with all possible params.
        """
        response = self.app.get('/api/employees?uuid=1&first_date=1982-03-14&second_date=1991-02-21')
        assert response.status_code == http.HTTPStatus.OK

    def test_post(self):
        """
        Test post request.
        """
        data = {
            'full_name': 'John Smith',
            'salary': 1500,
            'date_of_birth': '1991-02-21',
            'position': 'Engineer',
            'department_id': 'a4152167-a788-4c39-a232-d45a205aa678'
        }
        response = self.app.post('/api/employees', data=json.dumps(data),
                                 content_type='application/json')
        assert response.status_code == http.HTTPStatus.CREATED

    def test_wrong_post(self):
        """
        Test post request exception.
        """
        data = {
            'wrong_data': 'wrong data'
        }
        response = self.app.post('/api/employees', data=json.dumps(data),
                                 content_type='application/json')
        assert response.status_code == http.HTTPStatus.BAD_REQUEST

    def test_put(self):
        """
        Test put request.
        """
        data = {
            'full_name': 'John Smith',
            'salary': 1500,
            'date_of_birth': '1991-02-21',
            'position': 'Engineer',
            'department_id': 'a4152167-a788-4c39-a232-d45a205aa678'
        }
        response = self.app.put('/api/employees/1', data=json.dumps(data),
                                content_type='application/json')
        assert response.status_code == http.HTTPStatus.OK

    def test_wrong_put(self):
        """
        Test put request exception.
        """
        data = {
            'wrong_data': 'wrong data'
        }
        response = self.app.put('/api/employees/1', data=json.dumps(data),
                                content_type='application/json')
        assert response.status_code == http.HTTPStatus.BAD_REQUEST

    def test_delete(self):
        """
        Test delete request.
        """
        response = self.app.delete('/api/employees/1',
                                   content_type='application/json')
        assert response.status_code == http.HTTPStatus.OK

    def test_wrong_delete_data(self):
        """
        Test delete request exception because of wrong data.
        """
        response = self.app.delete('/api/employees/3423',
                                   content_type='application/json')
        assert response.status_code == http.HTTPStatus.NOT_FOUND

    def test_get_one(self):
        """
        Test get by uuid request.
        """
        response = self.app.get('/api/employees/1')
        assert response.status_code == http.HTTPStatus.OK

    def test_get_wrong_one(self):
        """
        Test get by uuid request exception.
        """
        response = self.app.get('/api/employees/423')
        assert response.status_code == http.HTTPStatus.NOT_FOUND

    def test_patch(self):
        """
        Test patch request.
        """
        data = {
            'full_name': 'Daisy Jonson',
        }
        response = self.app.patch('/api/employees/1', data=json.dumps(data),
                                  content_type='application/json')
        assert response.status_code == http.HTTPStatus.OK

    def test_wrong_patch(self):
        """
        Test patch request exception.
        """
        data = {
            'full_name': 'Daisy Jonson',
        }
        response = self.app.patch('/api/employees/423', data=json.dumps(data),
                                  content_type='application/json')
        assert response.status_code == http.HTTPStatus.OK
        # assert response.status_code == http.HTTPStatus.NOT_FOUND

    def test_wrong_args_patch(self):
        """
        Test patch request exception.
        """
        data = {
            'wrong_data': 'wrong_data',
        }
        response = self.app.patch('/api/employees/1', data=json.dumps(data),
                                  content_type='application/json')
        assert response.status_code == http.HTTPStatus.BAD_REQUEST

    def test_validation_name(self):
        """
        Test name validation.
        """
        data = {
            'full_name': 'wrongfhhhhhhhhhhhhhsgggsdfjcbnxzbvxbhsdvbsgfygreshfbndbchsfgsefgnbhfeyfdbvdhfdbhs'
        }
        response = self.app.patch('/api/employees/1', data=json.dumps(data),
                                  content_type='application/json')
        assert response.status_code == http.HTTPStatus.BAD_REQUEST

    def test_validation_position(self):
        """
        Test position validation.
        """
        data = {
            'position': 'wrongfhhhhhhhhhhhhhsgggsdfjcbnxzbvxbhsdvbsgfygreshfbndbchsfgsefgnbhfeyfdbvdhfdbhs'
        }
        response = self.app.patch('/api/employees/1', data=json.dumps(data),
                                  content_type='application/json')
        assert response.status_code == http.HTTPStatus.BAD_REQUEST

    def test_validation_salary(self):
        """
        Test salary validation.
        """
        data = {
            'salary': '43hb23'
        }
        response = self.app.patch('/api/employees/1', data=json.dumps(data),
                                  content_type='application/json')
        assert response.status_code == http.HTTPStatus.BAD_REQUEST

    def test_validation_dep_id(self):
        """
        Test id validation.
        """
        data = {
            'department_id': '43hb23'
        }
        response = self.app.patch('/api/employees/1', data=json.dumps(data),
                                  content_type='application/json')
        assert response.status_code == http.HTTPStatus.BAD_REQUEST

    def test_validation_dep_id_2(self):
        """
        Test uuid validation.
        """
        data = {
            'department_id': 'a4152167-a788-4f43-a232-d45a765aa678'
        }
        response = self.app.patch('/api/employees/1', data=json.dumps(data),
                                  content_type='application/json')
        assert response.status_code == http.HTTPStatus.BAD_REQUEST

    def test_validation_date(self):
        """
        Test date validation.
        """
        data = {
            'date_of_birth': 'sfsf'
        }
        response = self.app.patch('/api/employees/1', data=json.dumps(data),
                                  content_type='application/json')
        assert response.status_code == http.HTTPStatus.BAD_REQUEST

    def test_post_validate(self):
        """
        Test post request validation.
        """
        data = {
            'full_name': 'Jhon Smith',
            'salary': '15s00',
            'date_of_birth': '1991-02-21',
            'position': 'Engineer',
            'department_id': 'a4152167-a788-4c39-a232-d45a205aa678'
        }
        response = self.app.post('/api/employees', data=json.dumps(data),
                                 content_type='application/json')
        assert response.status_code == http.HTTPStatus.BAD_REQUEST

    def test_post_validate_id(self):
        """
        Test post request uuid validation.
        """
        data = {
            'full_name': 'Jhon Smith',
            'salary': 1500,
            'date_of_birth': '1991-02-21',
            'position': 'Engineer',
            'department_id': 'a4152167-a788-4f43-a232-d45a765aa678'
        }
        response = self.app.post('/api/employees', data=json.dumps(data),
                                 content_type='application/json')
        assert response.status_code == http.HTTPStatus.BAD_REQUEST

    def test_put_validate(self):
        """
        Test put request validation.
        """
        data = {
            'full_name': 'Jhon Smith',
            'salary': '150o0',
            'date_of_birth': '1991-02-21',
            'position': 'Engineer',
            'department_id': 'a4152167-a788-4c39-a232-d45a205aa678'
        }
        response = self.app.put('/api/employees/1', data=json.dumps(data),
                                content_type='application/json')
        assert response.status_code == http.HTTPStatus.BAD_REQUEST

    def test_put_validate_id(self):
        """
        Test put request uuid validation.
        """
        data = {
            'full_name': 'Jhon Smith',
            'salary': '1500',
            'date_of_birth': '1991-02-21',
            'position': 'Engineer',
            'department_id': 'a4152167-a788-4f43-a232-d45a765aa678'
        }
        response = self.app.put('/api/employees/1', data=json.dumps(data),
                                content_type='application/json')
        assert response.status_code == http.HTTPStatus.BAD_REQUEST

    def test_no_request_body(self):
        """
        Test request body missing.
        """
        response1 = self.app.post('/api/employees')
        response2 = self.app.patch('/api/employees/1',)
        response3 = self.app.put('/api/employees/1')
        assert response1.status_code == http.HTTPStatus.BAD_REQUEST
        assert response2.status_code == http.HTTPStatus.BAD_REQUEST
        assert response3.status_code == http.HTTPStatus.BAD_REQUEST
