"""
CRUD operations for department model.
"""
# pylint: disable=no-member
from sqlalchemy.sql import func

from department_app import db
from department_app.models.department_model import Department
from department_app.models.employee_model import Employee


def get_all_departments() -> list:
    """
    Select all data form Departments table.

    :return: list of department entries
    """
    departments = db.session.query(Department).all()
    for department in departments:
        salary = get_average_salary(department.uuid)
        department.average_salary = float(salary) if salary else 0
        department.number_of_employees = get_number_of_employees(department.uuid)
    return departments


def add_new_department(name, description) -> Department:
    """
    Add new entry in department table.

    :param name: department name
    :param description: department description
    :return: last department query
    """
    department = Department(name=name, description=description)
    db.session.add(department)
    db.session.commit()
    return db.session.query(Department).order_by(Department.id.desc()).first()


def update_department(department_uuid, name, description):
    """
    Change existing entry in department table.

    :param department_uuid: uuid of department
    :param name: department name
    :param description: department description
    """
    department = Department.query.filter_by(uuid=department_uuid).first_or_404(
        description='Not found. Entry with specified ID is missing.')
    department.name = name
    department.description = description
    db.session.add(department)
    db.session.commit()


def delete_department(department_uuid):
    """
    Delete department form table.

    :param department_uuid: uuid of department to delete
    """
    department = Department.query.filter_by(uuid=department_uuid).first_or_404(
        description='Not found. Entry with specified ID is missing.')
    db.session.delete(department)
    db.session.commit()


def get_average_salary(department_uuid) -> float:
    """
    Get average_salary department by id.

    :param department_uuid: id of department to get average salary
    :return: average_salary
    """
    return db.session.query(func.avg(Employee.salary)).filter_by(
        department_uuid=department_uuid).scalar()


def get_number_of_employees(department_uuid):
    """
    Get number of employees in department by its id.

    :param department_uuid: id of department
    :return: number of employees in department
    """
    return db.session.query(Employee).filter_by(department_uuid=department_uuid).count()


def get_one_department(dep_uuid):
    """
    Select data by id form Departments table.

    :param dep_uuid: uuid of department
    :return: department object
    """
    department = Department.query.filter_by(uuid=dep_uuid).first_or_404(
        description='Not found. Entry with specified ID is missing.')
    salary = get_average_salary(department.uuid)
    number_of_employees = get_number_of_employees(department.uuid)
    department.average_salary = float(salary) if salary else 0
    department.number_of_employees = number_of_employees
    return department


def update_department_patch(department_uuid, *, name=None, description=None):
    """
    Change existing department entry in without overwriting unspecified fields with None.

    :param department_uuid: uuid of department
    :param name: department name
    :param description: department description
    """
    department = Department.query.filter_by(uuid=department_uuid).first_or_404(
        description='Not found. Entry with specified ID is missing.')
    if name:
        department.name = name
    if description:
        department.description = description
    db.session.add(department)
    db.session.commit()
