from flask import Blueprint
from flask_restful import Api

rest = Blueprint('rest', __name__)
api = Api(rest)
from . import department_api
from . import employee_api
