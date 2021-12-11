"""
This module represents the logic on routes starting with /departments
"""
from flask import render_template, request, redirect, url_for, g
from flask_login import login_required

from department_app.service import department_service
from . import page


@page.route('/departments/', methods=['GET', 'POST'])
@login_required
def departments():
    """
    Render department page.
    """
    if request.method == 'POST':
        department_id = request.form['uuid']
        name = request.form['title']
        description = request.form['description']
        department_service.update_department(department_id, name, description)

    return render_template('departments.html',
                           departments=department_service.get_all_departments(), user=g.user)


@page.route('/departments/add/', methods=['GET', 'POST'])
@login_required
def add_department():
    """
    Add department to database.

    :return: render page
    """
    if request.method == 'POST':
        name = request.form['title']
        description = request.form['description']
        department_service.add_new_department(name, description)
        return redirect(url_for('page.departments'))

    return render_template('add_department.html', user=g.user)


@page.route('/departments/delete/<dep_uuid>', methods=['POST'])
@login_required
def delete_department(dep_uuid):
    """
    Delete department entry form database.

    :param dep_uuid: uuid of department to delete.
    :return: redirect to department page.
    """
    department_service.delete_department(dep_uuid)
    return redirect(url_for('page.departments'))
