from flask import request
from flask_restful import Resource
from . import api
from department_app.service.employee_service import get_all_employees, add_new_employee, update_employee, \
    get_employee_with_params, delete_employee


class EmployeesApi(Resource):
    @staticmethod
    def get():
        """
        Endpoint for getting all employees. If request contains parameters request will match them.

        :return: json response that contains all employee entries.
        """
        dep_id = request.args.get('id')
        first_date = request.args.get('first_date')
        second_date = request.args.get('second_date')
        if dep_id or first_date or second_date:
            employees = get_employee_with_params(dep_id=dep_id, first_date=first_date, second_date=second_date)
        else:
            employees = get_all_employees()
        emp = [employee.to_dict() for employee in employees]
        return emp

    @staticmethod
    def post():
        request_data = request.get_json()
        full_name = request_data['full_name']
        salary = request_data['salary']
        position = request_data['position']
        department = request_data['department']
        date_of_birth = request_data['date_of_birth']
        try:
            add_new_employee(full_name, salary, date_of_birth, position, department)
        except KeyError:
            return 'Wrong data', 400
        return 'Employee has been successfully added', 201

    @staticmethod
    def put():
        request_data = request.get_json()
        try:
            update_employee(emp_id=request_data['id'],
                            name=request_data['full_name'],
                            salary=request_data['salary'],
                            birthday=request_data['date_of_birth'],
                            position=request_data['position'],
                            department=request_data['department'])
        except KeyError:
            return 'Wrong data', 400
        return 'Employee has been successfully changed', 200

    @staticmethod
    def delete():
        request_data = request.get_json()
        try:
            delete_employee(request_data['id'])
        except KeyError:
            return 'Wrong data', 400
        return 'Employee has been successfully deleted', 200


api.add_resource(EmployeesApi, '/employee/')
