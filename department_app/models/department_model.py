"""
Module contains the class Department to work with `department` table
"""
from uuid import uuid4

from department_app import db


# pylint: disable=no-member
class Department(db.Model):
    """
    Department model.
    """
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    uuid = db.Column(db.String(length=36), unique=True, nullable=False, default=uuid4)
    name = db.Column(db.String(length=32))
    description = db.Column(db.Text)

    def to_dict(self):
        """
        Serializer that returns a dictionary from its fields
        :return: the department in json format
        """
        try:
            average_salary = self.average_salary
            number_of_employees = self.number_of_employees
        except AttributeError:
            return {'uuid': self.uuid,
                    'name': self.name,
                    'description': self.description,
                    }
        return {
            'uuid': self.uuid,
            'name': self.name,
            'description': self.description,
            'average_salary': average_salary,
            'number_of_employees': number_of_employees
        }

    def __repr__(self):
        return str(self.name)
