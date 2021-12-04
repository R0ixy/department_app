"""
Module contains employees REST API
"""
from flask import request
from flask_restful import Resource

from department_app.service.employee_service import get_all_employees, update_employee_patch,\
    update_employee, get_employee_with_params, delete_employee, get_one_employee, add_new_employee
from . import api


class EmployeesListApi(Resource):
    """
    Class for Employees Api Resource available on '/api/employees' url
    """

    @staticmethod
    def get():
        """
        Endpoint for getting employees. If request contains parameters result will match them.

        :return: json response that contains all employee entries.
        """
        dep_id = request.args.get('id')
        first_date = request.args.get('first_date')
        second_date = request.args.get('second_date')
        if dep_id or first_date or second_date:
            employees = get_employee_with_params(
                dep_id=dep_id,
                first_date=first_date,
                second_date=second_date)
        else:
            employees = get_all_employees()
        emp = [employee.to_dict() for employee in employees]
        return emp

    @staticmethod
    def post():
        """
        Endpoint for adding new employee.

        :return: json response containing the message whether the request was successful or not.
        """
        try:
            request_data = request.get_json()
            full_name = request_data['full_name']
            salary = request_data['salary']
            position = request_data['position']
            department = request_data['department_id']
            date_of_birth = request_data['date_of_birth']
            add_new_employee(full_name, salary, date_of_birth, position, department)
        except KeyError:
            return {'message': 'Wrong Key argument'}, 400
        return 'Employee has been successfully added', 201


class EmployeesApiByID(Resource):
    """
    Class for Employees Api Resource available on '/api/employees/<id>' url
    """

    @staticmethod
    def get(emp_id):
        """
        Endpoint for getting one employee by id.

        :return: json response that contains one employee entry.
        """
        employee = get_one_employee(emp_id)
        return employee.to_dict()

    @staticmethod
    def patch(emp_id):
        """
        Endpoint for changing an existing employee
        without overwriting unspecified fields with None.

        :return: json response containing the message whether the request was successful or not.
        """
        request_data = request.get_json()
        try:
            for key in request_data.keys():
                if key not in ['full_name', 'salary', 'date_of_birth', 'position', 'department_id']:
                    raise KeyError
            update_employee_patch(emp_id=emp_id,
                                  name=request_data.get('full_name'),
                                  salary=request_data.get('salary'),
                                  birthday=request_data.get('date_of_birth'),
                                  position=request_data.get('position'),
                                  department=request_data.get('department_id'))
        except KeyError:
            return {'message': 'Wrong data'}, 400
        return 'Employee has been successfully changed', 200

    @staticmethod
    def put(emp_id):
        """
        Endpoint for changing an existing employee.

        :return: json response containing the message whether the request was successful or not.
        """
        request_data = request.get_json()
        try:
            update_employee(emp_id=emp_id,
                            name=request_data['full_name'],
                            salary=request_data['salary'],
                            birthday=request_data['date_of_birth'],
                            position=request_data['position'],
                            department=request_data['department_id'])
        except KeyError:
            return {'message': 'Wrong data'}, 400
        return 'Employee has been successfully changed', 200

    @staticmethod
    def delete(emp_id):
        """
        Endpoint for deleting an employee.

        :return: json response containing the message whether the request was successful or not.
        """
        delete_employee(emp_id)
        return 'Employee has been successfully deleted', 200


api.add_resource(EmployeesListApi, '/employees/')
api.add_resource(EmployeesApiByID, '/employees/<emp_id>')
