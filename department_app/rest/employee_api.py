"""
Module contains employees REST API
"""
from datetime import datetime

from flask import request
from flask_restful import Resource
from sqlalchemy.exc import IntegrityError

from department_app.service.employee_service import get_all_employees, update_employee_patch, \
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
        dep_uuid = request.args.get('id')
        first_date = request.args.get('first_date')
        second_date = request.args.get('second_date')
        if dep_uuid or first_date or second_date:
            employees = get_employee_with_params(
                dep_uuid=dep_uuid,
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
            department_uuid = request_data['department_id']
            date_of_birth = request_data['date_of_birth']
        except KeyError:
            return {'error': 'Wrong Key argument'}, 400

        if error := validate(full_name=full_name,
                             position=position,
                             salary=salary,
                             date_of_birth=date_of_birth,
                             department_uuid=department_uuid):
            return error
        try:
            employee = add_new_employee(full_name, salary, date_of_birth, position, department_uuid)
        except IntegrityError:
            return {'error': 'Department with specified ID do not exist'}, 400
        return employee.to_dict(), 201


class EmployeesApiByID(Resource):
    """
    Class for Employees Api Resource available on '/api/employees/<uuid>' url
    """

    @staticmethod
    def get(emp_uuid):
        """
        Endpoint for getting one employee by id.

        :return: json response that contains one employee entry.
        """
        employee = get_one_employee(emp_uuid)
        return employee.to_dict()

    @staticmethod
    def patch(emp_uuid):
        """
        Endpoint for changing an existing employee
        without overwriting unspecified fields with None.

        :return: json response containing the message whether the request was successful or not.
        """
        request_data = request.get_json()

        for key in request_data.keys():
            if key not in ['full_name', 'salary', 'date_of_birth', 'position', 'department_id']:
                return {'error': 'Wrong data'}, 400

        full_name = request_data.get('full_name')
        salary = request_data.get('salary')
        date_of_birth = request_data.get('date_of_birth')
        position = request_data.get('position')
        department_uuid = request_data.get('department_id')

        if error := validate(full_name=full_name,
                             position=position,
                             salary=salary,
                             date_of_birth=date_of_birth,
                             department_uuid=department_uuid):
            return error

        try:
            update_employee_patch(emp_uuid=emp_uuid,
                                  name=full_name,
                                  salary=salary,
                                  birthday=date_of_birth,
                                  position=position,
                                  department=department_uuid)
        except IntegrityError:
            return {'error': 'Department with specified ID do not exist'}, 400
        return get_one_employee(emp_uuid).to_dict(), 200

    @staticmethod
    def put(emp_uuid):
        """
        Endpoint for changing an existing employee.

        :return: json response containing the message whether the request was successful or not.
        """
        request_data = request.get_json()
        try:
            full_name = request_data['full_name']
            salary = request_data['salary']
            date_of_birth = request_data['date_of_birth']
            position = request_data['position']
            department_uuid = request_data['department_id']
        except KeyError:
            return {'error': 'Wrong parameters. Note: all parameters (full_name,'
                             ' salary, date_of_birth,'
                             ' position, department_id)'
                             ' are required for PUT method.'}, 400

        if error := validate(full_name=full_name,
                             position=position,
                             salary=salary,
                             date_of_birth=date_of_birth,
                             department_uuid=department_uuid):
            return error
        try:
            update_employee(emp_uuid=emp_uuid,
                            name=full_name,
                            salary=salary,
                            birthday=date_of_birth,
                            position=position,
                            department=department_uuid)
        except IntegrityError:
            return {'error': 'Department with specified ID do not exist'}, 400
        return get_one_employee(emp_uuid).to_dict(), 200

    @staticmethod
    def delete(emp_uuid):
        """
        Endpoint for deleting an employee.

        :return: json response containing the message whether the request was successful or not.
        """
        delete_employee(emp_uuid)
        return 'Employee has been successfully deleted', 200


api.add_resource(EmployeesListApi, '/employees/')
api.add_resource(EmployeesApiByID, '/employees/<emp_uuid>')


def validate(*, full_name, position, salary, date_of_birth, department_uuid):
    """
    Data validation.

    :param full_name:
    :param position:
    :param salary:
    :param date_of_birth:
    :param department_uuid:
    """
    if full_name and len(full_name) > 64:
        return {'error': 'Full name too long (max length 64 symbols)'}, 400
    if position and len(position) > 64:
        return {'error': 'Position too long (max length 64 symbols)'}, 400
    if salary and not str(salary).isdigit():
        return {'error': 'Wrong data type. Salary must contain only digits'}, 400
    if department_uuid and not len(department_uuid) == 36:
        return {'error': 'Wrong data. Department UUID must contain exactly 36 symbols'}, 400
    if date_of_birth:
        try:
            datetime.strptime(date_of_birth, '%Y-%m-%d')
        except ValueError:
            return {'error': 'Wrong date format. Please use YYYY-MM-DD format'}, 400
    return None
