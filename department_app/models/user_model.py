"""
Module contains the class User to work with `user` table
"""
# pylint: disable=no-member
from flask_login import UserMixin

from department_app import db


class User(UserMixin, db.Model):
    """
    Employee model.
    """
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(length=16), unique=True, nullable=False)
    email = db.Column(db.String(length=32), unique=True, nullable=False)
    psw_hash = db.Column(db.String(length=256), nullable=False)

    def __repr__(self):
        return str(self.username)
