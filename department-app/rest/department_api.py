from flask import jsonify
from . import api
from service.department_service import get_all_departments


@api.route('/get_all_departments/', methods=['GET'])
def all_departments():
    departments = get_all_departments()
    dep = [department.to_dict() for department in departments]
    return jsonify(dep)
