from department_app.app import db
from ..models.employee_model import Employee


def get_all_employees() -> list:
    """
    Select all employees from database.

    :return: list of employee entries
    """
    return db.session.query(Employee).all()


def add_new_employee(name, salary, birthday, position, department):
    """
    Add new employee entry to database.

    :param name: full name of employee
    :param salary: salary of employee
    :param birthday: date of birth of employee
    :param position: position of employee
    :param department: id of employee's department
    """
    employee = Employee(full_name=name, salary=salary, date_of_birth=birthday, position=position,
                        department_id=department)
    db.session.add(employee)
    db.session.commit()


def update_employee(name, salary, birthday, position, department):
    """
    Change existing employee entry.

    :param name: full name of employee
    :param salary: salary of employee
    :param birthday: date of birth of employee
    :param position: position of employee
    :param department: id of employee's department
    """
    employee = Employee.query.get_or_404()
    employee.full_name = name
    employee.salary = salary
    employee.date_of_birth = birthday
    employee.position = position
    employee.department_id = department
    db.session.add(department)
    db.session.commit()


def delete_employee(emp_id):
    """
    Delete employee entry form database.

    :param emp_id: id of employee
    """
    employee = Employee.query.get_or_404(emp_id)
    db.session.delete(employee)
    db.session.commit()


def get_employee_with_date_of_birth(first_date, second_date=None):
    """
    Get employees born on a certain date or in the period between dates

    :param first_date:
    :param second_date:
    :return: list pf employees
    """
    # db.session.query(Employee).filter(first_date <= Employee.date_of_birth <= second_date).all()
    if second_date:
        return Employee.query.filter(first_date <= Employee.date_of_birth <= second_date).all()

    return Employee.query.filter_by(date_of_birth=first_date).all()
