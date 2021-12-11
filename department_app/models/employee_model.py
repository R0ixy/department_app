"""
Module contains the class Employee to work with `employee` table
"""
from department_app import db
from .department_model import Department


# pylint: disable=no-member
class Employee(db.Model):
    """
    Employee model.
    """
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    uuid = db.Column(db.String(length=36), unique=True)
    full_name = db.Column(db.String(length=64), nullable=False)
    salary = db.Column(db.Integer)
    date_of_birth = db.Column(db.Date)
    position = db.Column(db.String(length=64))
    department_uuid = db.Column(db.String(length=36), db.ForeignKey('department.uuid'), unique=True)
    department = db.relationship(Department, backref='employee')

    def to_dict(self):
        """
        Serializer that returns a dictionary from its fields.

        :return: the employee in json format
        """
        return {
            'uuid': self.uuid,
            'full_name': self.full_name,
            'salary': self.salary,
            'date_of_birth': str(self.date_of_birth),
            'position': self.position,
            'department_uuid': self.department_uuid,
            'age': self.age,
            'department': str(self.department)
        }

    def __repr__(self):
        return str(self.full_name)
