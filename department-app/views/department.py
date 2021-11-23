from flask import render_template, request, redirect, url_for
from ..app import app
from ..service import department_service


@app.route('/departments/', methods=['GET', 'POST'])
def departments():
    """
    Render department page.
    :return:
    """
    if request.method == 'POST':
        department_id = request.form['id']
        name = request.form['title']
        description = request.form['description']
        department_service.update_department(department_id, name, description)

    department_list = department_service.get_all_departments()
    return render_template('departments.html', departments=department_list)


@app.route('/add_department/', methods=['GET', 'POST'])
def add_department():
    """
    Add department to database.

    :return: renders template
    """
    if request.method == 'POST':
        name = request.form['title']
        description = request.form['description']
        department_service.add_new_department(name, description)
        return redirect(url_for('departments'))

    return render_template('add_department.html')
