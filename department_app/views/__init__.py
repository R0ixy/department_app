"""
Initialize page Blueprint and import all submodules form views module.
"""
# pylint: disable=wrong-import-position, cyclic-import
from flask import Blueprint

page = Blueprint('page', __name__)

from . import auth
from . import department_views
from . import employee_views
