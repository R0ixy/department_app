"""
This module represents the logic for login or registration
"""
from flask import render_template, request, flash, redirect, url_for, g
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from department_app.service import auth_service
from . import page


@page.route('/')
def index():
    """
    Render main page.

    :return: rendered page
    """
    user = g.user
    return render_template('index.html', user=user)


@page.route('/login/', methods=['GET', 'POST'])
def login():
    """
    Render login page.

    :return: rendered page
    """
    if request.method == 'POST':
        username = request.form['username']
        user = auth_service.get_user(username=username)
        if not user or not check_password_hash(user.psw_hash, request.form['password']):
            flash('Wrong password or email')
        else:
            login_user(user)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)

            return redirect(url_for('page.index'))

    return render_template('login.html')


@page.route('/register/', methods=['GET', 'POST'])
def register():
    """
    Render registration page.

    :return: rendered page
    """
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        if auth_service.username_exists(username.lower()):
            flash('Username is already taken', 'username')
        elif auth_service.email_exists(email.lower()):
            flash('User with this email already exists', 'email')
        else:
            psw = generate_password_hash(request.form['password'])
            auth_service.new_user(username.lower(), email.lower(), psw)
            return redirect(url_for('page.login'))

    return render_template('registration.html')


@page.route('/logout')
@login_required
def logout():
    """
    Logout user.

    :return: redirect to main page.
    """
    logout_user()
    return redirect(url_for('page.index'))


@page.after_request
def redirect_to_login(response):
    """
    Redirect unauthorised user to login page.

    :param response: page where user tried to visit.
    :return: if unauthorised - redirect to login page.
    """
    if response.status_code == 401:
        return redirect(url_for('page.login') + '?next=' + request.url)
    return response


@page.before_request
def before_request():
    """
    Get current user before every request.
    :return:
    """
    g.user = current_user
