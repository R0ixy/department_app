from flask import jsonify, request
from . import api
from ..service.department_service import get_all_departments, add_new_department


@api.route('/get_all_departments/', methods=['GET'])
def all_departments():
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

