"""
CRUD operations for user model.
"""
# pylint: disable=no-member
from department_app import db, login_manager
from department_app.models.user_model import User


@login_manager.user_loader
def load_user(user_id) -> User:
    """
    Load user from database by id.

    :param user_id: id of user
    :return: User object
    """
    return User.query.get(user_id)


def username_exists(username) -> bool:
    """
    Check whether a username exists in database.

    :param username: username to check
    :return: True if username already exists, False if not
    """
    user = User.query.filter_by(username=username).first()
    return bool(user)


def email_exists(email) -> bool:
    """
    Check whether an email exists in database.

    :param email: email to check
    :return: True if email already exists, False if not
    """
    user = User.query.filter_by(email=email).first()
    return bool(user)


def new_user(username, email, psw_hash) -> None:
    """
    Add new user to database.

    :param username: user's username
    :param email: user's email
    :param psw_hash: password hash
    """
    user = User(username=username, email=email, psw_hash=psw_hash)
    db.session.add(user)
    db.session.commit()


def get_user(username) -> User:
    """
    Get user form database by username.

    :param username: user's username
    :return: User object
    """
    return User.query.filter_by(username=username).first()
