from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__, static_url_path='static')
# db_url = 'mysql+pymysql://root:testpassword@localhost:80/db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:testpassword@localhost:80/db'

app.config['SECRET_KEY'] = 'gcfgsdhxzncvbsjhuytsgf236uteq2e2t17dcz'

db = SQLAlchemy(app)


# login_manager = LoginManager(app)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':

    db.init_app(app)
    # db.create_all()
    Migrate(app, db)
    app.run(debug=True, use_reloader=True)
