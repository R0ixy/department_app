from flask import render_template, request, flash, redirect, url_for, g
from flask_login import login_user, current_user, logout_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash

from department_app.loader import login_manager, db
from department_app.models.user_model import User
from . import page


@page.before_request
def before_request():
    """
    Get's current user before every request.
    :return:
    """
    g.user = current_user


@page.route('/')
def index():
    """
    Render main page.

    :return: rendered page
    """
    user = g.user
    return render_template('index.html', user=user)


@login_manager.user_loader
def load_user(user_id):
    """
    Loads user from database by id.

    :param user_id: id of user
    :return: User object
    """
    return User.query.get(user_id)


@page.route('/login/', methods=['GET', 'POST'])
def login():
    """
    Render login page.

    :return: rendered page
    """
    if request.method == 'POST':
        username = request.form['username']
        user = User.query.filter_by(username=username).first()
        if not user or not check_password_hash(user.psw_hash, request.form['password']):
            flash('Wrong password or email')
        else:
            login_user(user)
            next_page = request.args.get('next')
            if next_page:
                redirect(next_page)
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
        psw = generate_password_hash(request.form['password'])
        new_user = User(
            username=username,
            email=email,
            psw_hash=psw
        )
        db.session.add(new_user)
        db.session.commit()
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
