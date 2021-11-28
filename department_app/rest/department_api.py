from flask import jsonify, request
from . import api
from department_app.service.department_service import get_all_departments, add_new_department, update_department


@api.route('/get_all_departments/', methods=['GET'])
def all_departments():
    """
    Endpoint for getting all departments.

    :return: json response that contains all department entries.
    """
    departments = get_all_departments()
    dep = [department.to_dict() for department in departments]
    return jsonify(dep)


@api.route('/add_department/', methods=['POST'])
def add_department():
    request_data = request.get_json()
    try:
        add_new_department(request_data['name'], request_data['description'])
    except KeyError:
        return jsonify({'message': 'Wrong data'}, 400)
    return jsonify('Department has been successfully added', 201)


@api.route('/update_department/', methods=['PUT'])
def update_department():
    request_data = request.get_json()
    try:
        update_department(request_data['id'], request_data['name'], request_data['description'])
    except KeyError:
        return jsonify({'message': 'Wrong data'}, 400)
    return jsonify('Department has been changed', 201)

