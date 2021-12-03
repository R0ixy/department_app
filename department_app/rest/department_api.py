from flask import request
from flask_restful import Resource

from department_app.service.department_service import get_all_departments, add_new_department, update_department, \
    delete_department
from . import api


class DepartmentApi(Resource):
    @staticmethod
    def get():
        """
        Endpoint for getting all departments.

        :return: json response that contains all department entries.
        """
        departments = get_all_departments()
        dep = [department.to_dict() for department in departments]
        return dep

    @staticmethod
    def post():
        """
        Endpoint for adding new department.

        :return: json response containing the message whether the request was successful or not.
        """
        request_data = request.get_json()
        try:
            add_new_department(request_data['name'], request_data['description'])
        except KeyError:
            return {'message': 'Wrong Key argument'}, 400
        return 'Department has been successfully added', 201

    @staticmethod
    def put():
        """
        Endpoint for changing an existing department.

        :return: json response containing the message whether the request was successful or not.
        """
        request_data = request.get_json()
        try:
            update_department(request_data['id'], request_data['name'], request_data['description'])
        except KeyError:
            return {'message': 'Wrong Key argument'}, 400
        return 'Department has been successfully changed', 200

    @staticmethod
    def delete():
        """
        Endpoint for deleting a department.

        :return: json response containing the message whether the request was successful or not.
        """
        request_data = request.get_json()
        try:
            delete_department(request_data['id'])
        except KeyError:
            return {'message': 'Wrong Key argument'}, 400
        return 'Department has been successfully deleted', 200


api.add_resource(DepartmentApi, '/departments/')
