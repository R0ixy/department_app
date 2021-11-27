from ..app import db
from ..models.department_model import Department
from ..models.employee_model import Employee


def get_all_departments() -> list:
    """
    Select all data form Departments table.

    :return: list of department entries
    """
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


def delete_department(department_id):
    """
    Delete department form table.
    :param department_id: id of department to delete
    """
    department = Department.query.get_or_404(department_id)
    db.session.delete(department)
    db.session.commit()


def get_average_salary(department_id) -> float:
    """
    Get average_salary department by id.
    :param department_id: id of department to get average salary
    :return: average_salary
    """
    employee = db.session.query(Employee).filter_by(department_id=department_id).all()
    average_salary = 0
    if employee:
        for i in employee:
            average_salary += i.salary
        return average_salary / len(employee)
    return 0


def get_number_of_employees(department_id):
    """
    Get number of employees in department by its id.
    :param department_id: id of department
    :return: number of employees in department
    """
    return db.session.query(Employee).filter_by(department_id=department_id).count()
