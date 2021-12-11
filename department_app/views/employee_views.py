"""
This module represents the logic on routes starting with /employees
"""
from flask import render_template, request, redirect, url_for, g
from flask_login import login_required

from department_app.service import employee_service
from department_app.service.department_service import get_all_departments
from . import page


@page.route('/employees/', defaults={'dep_uuid': None}, methods=['GET', 'POST'])
@page.route('/employees/<dep_uuid>', methods=['GET', 'POST'])
@login_required
def employees(dep_uuid):
    """
    Renders employees page.

    :param dep_uuid: uuid of department to get it's employees
    :return: rendered 'employees.html' template
    """
    if request.method == 'POST':
        emp_id = request.form['uuid']
        full_name = request.form['full_name']
        salary = request.form['salary']
        date_of_birth = request.form['date_of_birth']
        position = request.form['position']
        department_id = request.form['department']
        employee_service.update_employee(emp_uuid=emp_id,
                                         name=full_name,
                                         salary=salary,
                                         birthday=date_of_birth,
                                         position=position,
                                         department=department_id)
    dep = get_all_departments()
    if dep_uuid:
        employees_list = employee_service.get_employee_with_params(dep_uuid=dep_uuid)
        return render_template('employees.html',
                               employees=employees_list, departments=dep, user=g.user)
    employees_list = employee_service.get_all_employees()
    return render_template('employees.html',
                           employees=employees_list, departments=dep, user=g.user)


@page.route('/employees/add/', methods=['GET', 'POST'])
@login_required
def add_employee():
    """
    Adds new employee to database.

    :return: rendered 'add_employee.html' template
    """
    if request.method == 'POST':
        full_name = request.form['full_name']
        salary = request.form['salary']
        position = request.form['position']
        department = request.form['department']
        date_of_birth = request.form['date_of_birth']

        employee_service.add_new_employee(full_name, salary, date_of_birth, position, department)
        return redirect(url_for('page.employees'))
    departments = get_all_departments()
    return render_template('add_employee.html', departments=departments, user=g.user)


@page.route('/employees/delete/<emp_uuid>', methods=['POST'])
@login_required
def delete_employee(emp_uuid):
    """
    Deletes employee from database.

    :param emp_uuid: uuid of employee to delete
    :return: redirect to employees page
    """
    employee_service.delete_employee(emp_uuid)
    return redirect(url_for('page.employees'))
