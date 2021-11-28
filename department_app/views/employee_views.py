from flask import render_template, request, redirect, url_for
from . import page
from department_app.service import employee_service


@page.route('/employees/', methods=['GET', 'POST'])
def employees():
    employees_list = employee_service.get_all_employees()
    return render_template('employees.html', employees=employees_list)


@page.route('/add_employee/')
def add_employee():
    return render_template('add_employee.html')

# @app.route()
