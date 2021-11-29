"""
Module contains the class Employee to work with `employee` table
"""
from .department_model import Department

from ..loader import db


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True, nullable=False)
#     username = db.Column(db.String(length=16), unique=True, nullable=False)
#     email = db.Column(db.String(length=32), unique=True, nullable=False)
#     psw_hash = db.Column(db.String(length=256), nullable=False)
#
#     def __repr__(self):
#         return f'<User {self.username}>'

# pylint: disable=no-member
class Employee(db.Model):
    """
    Employee table.
    """
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    full_name = db.Column(db.String(length=64), nullable=False)
    salary = db.Column(db.Integer)
    date_of_birth = db.Column(db.Date)
    position = db.Column(db.String(length=64))
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)
    department = db.relationship(Department, backref='employee')

    def to_dict(self):
        """
        Serializer that returns a dictionary from its fields
        :return: the employee in json format
        """
        return {
            'id': self.id,
            'full_name': self.full_name,
            'salary': self.salary,
            'date_of_birth': str(self.date_of_birth),
            'position': self.position,
            'department_id': self.department_id,
            'age': self.age
        }

    def __repr__(self):
        return self.full_name
