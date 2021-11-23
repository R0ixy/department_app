from app import db


class Department(db.Model):
    id = db.Column(db.Integer, primary_key=True, nullable=False)
    name = db.Column(db.String(length=32))
    description = db.Column(db.Text)

    def __repr__(self):
        return f'<Department {self.name}>'
