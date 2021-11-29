from flask import render_template, request, redirect, url_for
from . import page
from department_app.service import employee_service
from department_app.service.department_service import get_all_departments


@page.route('/employees/', methods=['GET', 'POST'])
def employees():
    employees_list = employee_service.get_all_employees()
    dep = get_all_departments()
    return render_template('employees.html', employees=employees_list, departments=dep)


@page.route('/add_employee/', methods=['GET', 'POST'])
def add_employee():
    if request.method == 'POST':
        full_name = request.form['full_name']
        salary = request.form['salary']
        position = request.form['position']
        department = request.form['department']
        date_of_birth = request.form['date_of_birth']

        employee_service.add_new_employee(full_name, salary, date_of_birth, position, department)
        return redirect(url_for('page.employees'))
    departments = get_all_departments()
    return render_template('add_employee.html', departments=departments)
