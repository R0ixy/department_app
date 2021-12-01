from flask_login import UserMixin
from department_app.loader import db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    username = db.Column(db.String(length=16), unique=True, nullable=False)
    email = db.Column(db.String(length=32), unique=True, nullable=False)
    psw_hash = db.Column(db.String(length=256), nullable=False)

