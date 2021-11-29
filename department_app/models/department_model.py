"""
Module contains the class Department to work with `department` table
"""
# pylint: disable=cyclic-import
from ..loader import db


# pylint: disable=no-member
class Department(db.Model):
    """
    Department table.
    """
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(length=32))
    description = db.Column(db.Text)

    def to_dict(self):
        """
        Serializer that returns a dictionary from its fields
        :return: the department in json format
        """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'average_salary': self.average_salary,
            'number_of_employees': self.number_of_employees
        }

    def __repr__(self):
        return self.name
