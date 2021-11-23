from app import db
from models.department_model import Department


def get_all_departments() -> list:
    """
    Select all data form Departments table.

    :return: list of department entries
    """
    # department_list = db.session.query(Department).all()
    # return [department.to_dict() for department in department_list]
    return db.session.query(Department).all()


def add_new_department(name, description):
    """
    Add new entry in department table.

    :param name: department name
    :param description: department description
    """
    department = Department(name=name, description=description)
    db.session.add(department)
    db.session.commit()


def update_department(department_id, name, description):
    """
    Change existing entry in department table.
    :param department_id: id of department
    :param name: department name
    :param description: department description
    """
    department = Department.query.get_or_404(department_id)
    department.name = name
    department.description = description
    db.session.add(department)
    db.session.commit()

