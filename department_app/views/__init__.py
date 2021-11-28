# pylint: disable=wrong-import-position
from flask import Blueprint

page = Blueprint('page', __name__)

from . import auth
from . import department_views
from . import employee_views
