"""
CRUD operations form employee model.
"""
# pylint: disable=no-member
from datetime import datetime, date
from ..loader import db
from ..models.employee_model import Employee


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


def add_new_employee(name, salary, birthday, position, department):
    """
    Add new employee entry to database.

    :param name: full name of employee
    :param salary: salary of employee
    :param birthday: date of birth of employee in format yyyy-mm-dd
    :param position: position of employee
    :param department: id of employee's department
    """
    employee = Employee(full_name=name, salary=salary, date_of_birth=birthday, position=position,
                        department_id=department)
    db.session.add(employee)
    db.session.commit()


def update_employee(emp_id, name, salary, birthday, position, department):
    """
    Change existing employee entry.

    :param emp_id: id of employee
    :param name: full name of employee
    :param salary: salary of employee
    :param birthday: date of birth of employee in format yyyy-mm-dd
    :param position: position of employee
    :param department: id of employee's department
    """
    employee = Employee.query.get_or_404(emp_id)
    employee.full_name = name
    employee.salary = salary
    employee.date_of_birth = birthday
    employee.position = position
    employee.department_id = department
    db.session.add(employee)
    db.session.commit()


def delete_employee(emp_id):
    """
    Delete employee entry form database.

    :param emp_id: id of employee
    """
    employee = Employee.query.get_or_404(emp_id)
    db.session.delete(employee)
    db.session.commit()


def get_employee_with_params(emp_id=None, first_date=None, second_date=None):
    """
    Get employees born on a certain date or in the period between dates.

    :param first_date: date in format yyyy-mm-dd
    :param second_date: date in format yyyy-mm-dd
    :return: list pf employees
    """
    today = date.today()
    if first_date:
        first_date = datetime.strptime(first_date, "%Y-%m-%d").date()
        if second_date:
            second_date = datetime.strptime(second_date, "%Y-%m-%d").date()
            employees = Employee.query.filter(Employee.date_of_birth.between(first_date, second_date)).filter_by(
                id=emp_id).all()
        else:
            employees = Employee.query.filter_by(date_of_birth=first_date).filter_by(id=emp_id).all()
    else:
        employees = Employee.query.filter_by(id=emp_id).all()
    for employee in employees:
        born = employee.date_of_birth
        age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        employee.age = age
    return employees
