"""
Module contains department REST API
"""
from flask import request
from flask_restful import Resource

from department_app.service.department_service import get_all_departments, add_new_department, \
    update_department, delete_department, get_one_department, update_department_patch
from . import api


class DepartmentListApi(Resource):
    """
    Class for Department Api Resource available on '/api/departments' url
    """

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


class DepartmentApiByID(Resource):
    """
    Class for Department Api Resource available on '/api/departments/<id>' url
    """

    @staticmethod
    def get(dep_id):
        """
        Endpoint for getting one department by id.

        :return: json response that contains one department entry.
        """
        try:
            department = get_one_department(dep_id)
        except AttributeError:
            return {'message': 'Not found'}, 404
        return department.to_dict()

    @staticmethod
    def patch(dep_id):
        """
        Endpoint for changing an existing department
        without overwriting unspecified fields with None.

        :return: json response containing the message whether the request was successful or not.
        """
        request_data = request.get_json()
        try:
            if not request_data.get('name') and not request_data.get('description'):
                raise KeyError
            update_department_patch(dep_id,
                                    name=request_data.get('name'),
                                    description=request_data.get('description'))
        except KeyError:
            return {'message': 'Wrong data'}, 400
        return 'Department has been successfully changed', 200

    @staticmethod
    def put(dep_id):
        """
        Endpoint for changing an existing department.

        :return: json response containing the message whether the request was successful or not.
        """
        request_data = request.get_json()
        try:
            update_department(dep_id, request_data['name'], request_data['description'])
        except KeyError:
            return {'message': 'Wrong data'}, 400
        return 'Department has been successfully changed', 200

    @staticmethod
    def delete(dep_id):
        """
        Endpoint for deleting a department.

        :return: json response containing the message whether the request was successful or not.
        """
        delete_department(dep_id)
        return 'Department has been successfully deleted', 200


api.add_resource(DepartmentListApi, '/departments/')
api.add_resource(DepartmentApiByID, '/departments/<dep_id>')
