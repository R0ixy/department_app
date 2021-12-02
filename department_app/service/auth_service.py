from department_app.loader import db
from department_app.models.user_model import User


def username_exists(username):
    user = User.query.filter_by(username=username).first()
    return True if user else False


def email_exists(email):
    user = User.query.filter_by(email=email).first()
    return True if user else False


def new_user(username, email, psw_hash):
    user = User(username=username, email=email, psw_hash=psw_hash)
    db.session.add(user)
    db.session.commit()


def get_user(username):
    return User.query.filter_by(username=username).first()
