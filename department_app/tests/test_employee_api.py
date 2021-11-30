import http
import json

from department_app.tests.conftest import BaseTest
from department_app.models.employee_model import Employee
from department_app.models.department_model import Department
from department_app.loader import db


class TestEmployeeApi(BaseTest):
    @staticmethod
    def create_dep():
        department = Department(name='Test Department', description='Test Description')
        # pylint: disable=no-member
        db.session.add(department)
        db.session.commit()

    def fill_db(self):
        self.create_dep()
        employee = Employee(full_name='James Johnson',
                            salary=2000,
                            date_of_birth='1982-03-14',
                            position='Developer',
                            department_id=1)
        # pylint: disable=no-member
        db.session.add(employee)
        db.session.commit()

    def test_get(self):
        self.fill_db()
        response = self.app.get('/api/employee/')
        assert response.status_code == http.HTTPStatus.OK

    def test_get_with_param_id(self):
        self.fill_db()
        response = self.app.get('/api/employee/?id=1&')
        assert response.status_code == http.HTTPStatus.OK

    def test_get_with_param_first_date(self):
        self.fill_db()
        response = self.app.get('/api/employee/?first_date=1982-03-14')
        assert response.status_code == http.HTTPStatus.OK

    def test_get_with_param_id_and_first_date(self):
        self.fill_db()
        response = self.app.get('/api/employee/?id=1&first_date=1982-03-14')
        assert response.status_code == http.HTTPStatus.OK

    def test_get_with_all_params(self):
        self.fill_db()
        response = self.app.get('/api/employee/?id=1&first_date=1982-03-14&second_date=1991-02-21')
        assert response.status_code == http.HTTPStatus.OK

    def test_post(self):
        self.create_dep()
        data = {
            'full_name': 'Jhon Smith',
            'salary': 1500,
            'date_of_birth': '1991-02-21',
            'position': 'Engineer',
            'department_id': 1
        }
        response = self.app.post('/api/employee/', data=json.dumps(data),
                                 content_type='application/json')
        assert response.status_code == http.HTTPStatus.CREATED

    def test_wrong_post(self):
        self.create_dep()
        data = {
            'wrong_data': 'wrong data'
        }
        response = self.app.post('/api/employee/', data=json.dumps(data),
                                 content_type='application/json')
        assert response.status_code == http.HTTPStatus.BAD_REQUEST

    def test_put(self):
        self.fill_db()
        data = {
            'id': 1,
            'full_name': 'Jhon Smith',
            'salary': 1500,
            'date_of_birth': '1991-02-21',
            'position': 'Engineer',
            'department_id': 1
        }
        response = self.app.put('/api/employee/', data=json.dumps(data),
                                content_type='application/json')
        assert response.status_code == http.HTTPStatus.OK

    def test_wrong_put(self):
        self.create_dep()
        data = {
            'wrong_data': 'wrong data'
        }
        response = self.app.put('/api/employee/', data=json.dumps(data),
                                content_type='application/json')
        assert response.status_code == http.HTTPStatus.BAD_REQUEST

    def test_delete(self):
        self.fill_db()
        data = {
            'id': 1,
        }
        response = self.app.delete('/api/employee/', data=json.dumps(data),
                                   content_type='application/json')
        assert response.status_code == http.HTTPStatus.OK

    def test_wrong_delete_data(self):
        self.create_dep()
        data = {
            'id': 3423
        }
        response = self.app.delete('/api/employee/', data=json.dumps(data),
                                   content_type='application/json')
        assert response.status_code == http.HTTPStatus.NOT_FOUND

    def test_wrong_delete_args(self):
        self.create_dep()
        data = {
            'wrong_arg': 3423
        }
        response = self.app.delete('/api/employee/', data=json.dumps(data),
                                   content_type='application/json')
        assert response.status_code == http.HTTPStatus.BAD_REQUEST
