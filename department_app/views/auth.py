from flask import render_template, request, flash, redirect, url_for
# from flask_login import login_user
# from werkzeug.security import generate_password_hash, check_password_hash
# from department_app.loader import login_manager, db
# from models.employee import User
from . import page


@page.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


# @login_manager.user_loader
# def load_user(user_id):
#     return User.get(user_id)
#
#
# @page.route('/login/', methods=['GET', 'POST'])
# def login():
#     if request.method == 'POST':
#         username = request.form['username']
#         user = User.query.filter_by(username=username).first()
#         if not user or not check_password_hash(user.psw_hash, request.form['password']):
#             flash('Wrong password or email')
#         else:
#             login_user(user)
#
#     return render_template('login.html')
#
#
# @page.route('/register/', methods=['GET', 'POST'])
# def register():
#     if request.method == 'POST':
#         username = request.form['username']
#         email = request.form['email']
#         psw = generate_password_hash(request.form['password'])
#         new_user = User(
#             username=username,
#             email=email,
#             psw_hash=psw
#         )
#         db.session.add(new_user)
#         db.session.commit()
#         return redirect(url_for('login'))
#
#     return render_template('registration.html')
