from flask import render_template, request, redirect, url_for
from ..app import app


@app.route('/employees/', methods=['GET', 'POST'])
def employees():
    return render_template('employees.html')


@app.route('/add_employee/')
def add_employee():
    return render_template('add_employee.html')
