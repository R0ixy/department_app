from app import db


# class User(db.Model):
#     id = db.Column(db.Integer, primary_key=True, nullable=False)
#     username = db.Column(db.String(length=16), unique=True, nullable=False)
#     email = db.Column(db.String(length=32), unique=True, nullable=False)
#     psw_hash = db.Column(db.String(length=256), nullable=False)
#
#     def __repr__(self):
#         return f'<User {self.username}>'


class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    full_name = db.Column(db.String(length=64), nullable=False)
    salary = db.Column(db.Integer)
    date_of_birth = db.Column(db.Date)
    department_id = db.Column(db.Integer, db.ForeignKey('department.id'), nullable=False)

    def __repr__(self):
        return f'<Employee {self.username}>'
