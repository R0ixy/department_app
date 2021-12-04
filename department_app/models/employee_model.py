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
            'age': self.age,
            'department': str(self.department)
        }

    def __repr__(self):
        return self.full_name
