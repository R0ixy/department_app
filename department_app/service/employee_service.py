"""
CRUD operations form employee model.
"""
# pylint: disable=no-member
from datetime import datetime, date
from uuid import uuid4

from department_app import db
from department_app.models.employee_model import Employee


def get_all_employees() -> list:
    """
    Select all employees from database and calculate each employee's age.

    :return: list of employee entries
    """
    employees = db.session.query(Employee).all()
    today = date.today()
    for employee in employees:
        born = employee.date_of_birth
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        employee.age = age
    return employees


def get_one_employee(emp_uuid):
    """
    Select one employee from database by id and calculate age.

    :param emp_uuid uuid of employee
    :return: employee object
    """
    employee = Employee.query.filter_by(uuid=emp_uuid).first_or_404()
    today = date.today()
    born = employee.date_of_birth
    employee.age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    return employee


def add_new_employee(name, salary, birthday, position, department) -> Employee:
    """
    Add new employee entry to database.

    :param name: full name of employee
    :param salary: salary of employee
    :param birthday: date of birth of employee in format yyyy-mm-dd
    :param position: position of employee
    :param department: uuid of employee's department
    """
    employee = Employee(uuid=uuid4(),
                        full_name=name,
                        salary=salary,
                        date_of_birth=birthday,
                        position=position,
                        department_uuid=department)
    db.session.add(employee)
    db.session.commit()

    emp = db.session.query(Employee).order_by(Employee.id.desc()).first()
    today = date.today()
    born = emp.date_of_birth
    emp.age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    return emp


def update_employee(emp_uuid, name, salary, birthday, position, department):
    """
    Change existing employee entry.

    :param emp_uuid: id of employee
    :param name: full name of employee
    :param salary: salary of employee
    :param birthday: date of birth of employee in format yyyy-mm-dd
    :param position: position of employee
    :param department: id of employee's department
    """
    employee = Employee.query.filter_by(uuid=emp_uuid).first_or_404()
    employee.full_name = name
    employee.salary = salary
    employee.date_of_birth = birthday
    employee.position = position
    employee.department_uuid = department
    db.session.add(employee)
    db.session.commit()


def delete_employee(emp_uuid):
    """
    Delete employee entry form database.

    :param emp_uuid: id of employee
    """
    employee = Employee.query.filter_by(uuid=emp_uuid).first_or_404()
    db.session.delete(employee)
    db.session.commit()


def get_employee_with_params(*, dep_uuid=None, first_date=None, second_date=None):
    """
    Get employees born on a certain date or in the period between dates.

    :param dep_uuid: id of department
    :param first_date: date in format yyyy-mm-dd
    :param second_date: date in format yyyy-mm-dd
    :return: list pf employees
    """
    today = date.today()
    if first_date:
        first_date = datetime.strptime(first_date, "%Y-%m-%d").date()
        if second_date:
            second_date = datetime.strptime(second_date, "%Y-%m-%d").date()
            if dep_uuid:
                employees = Employee.query.filter(
                    Employee.date_of_birth.between(first_date, second_date)).filter_by(
                    department_uuid=dep_uuid).all()
            else:
                employees = Employee.query.filter(
                    Employee.date_of_birth.between(first_date, second_date)).all()
        else:
            if dep_uuid:
                employees = Employee.query.filter_by(
                    date_of_birth=first_date).filter_by(department_uuid=dep_uuid).all()
            else:
                employees = Employee.query.filter_by(date_of_birth=first_date).all()
    else:
        if dep_uuid:
            employees = Employee.query.filter_by(department_uuid=dep_uuid).all()
        else:
            employees = Employee.query.all()
    for employee in employees:
        born = employee.date_of_birth
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        employee.age = age
    return employees


# pylint: disable=line-too-long
def update_employee_patch(emp_uuid, *, name=None, salary=None, birthday=None, position=None, department=None):
    """
    Change existing employee entry without overwriting unspecified fields with None.

    :param emp_uuid: uuid of employee
    :param name: full name of employee
    :param salary: salary of employee
    :param birthday: date of birth of employee in format yyyy-mm-dd
    :param position: position of employee
    :param department: uuid of employee's department
    """
    employee = Employee.query.filter_by(uuid=emp_uuid).first_or_404()
    if name:
        employee.full_name = name
    if salary:
        employee.salary = salary
    if birthday:
        employee.date_of_birth = birthday
    if position:
        employee.position = position
    if department:
        employee.department_uuid = department
    db.session.add(employee)
    db.session.commit()
