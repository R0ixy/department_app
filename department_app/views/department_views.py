"""
This module represents the logic on routes starting with /departments
"""
from flask import render_template, request, redirect, url_for
from department_app.service import department_service
from . import page


@page.route('/departments/', methods=['GET', 'POST'])
def departments():
    """
    Render department page.
    :return: render page
    """
    if request.method == 'POST':
        department_id = request.form['id']
        name = request.form['title']
        description = request.form['description']
        department_service.update_department(department_id, name, description)

    return render_template('departments.html', departments=department_service.get_all_departments())


@page.route('/departments/add/', methods=['GET', 'POST'])
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

    return render_template('add_department.html')


@page.route('/departments/delete/<dep_id>', methods=['POST'])
def delete_department(dep_id):
    """
    Delete department entry form database.

    :param dep_id: id of department to delete.
    :return: redirect to department page.
    """
    if request.method == 'POST':
        department_service.delete_department(dep_id)
        return redirect(url_for('page.departments'))
