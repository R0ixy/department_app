from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
# from config import SECRET_KEY, DB_username, DB_password, DB_host, DB_port

app = Flask(__name__, static_url_path='/department_app/static/')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql+pymysql://{DB_username}:{DB_password}@{DB_host}:{DB_port}/db'
# app.config['SECRET_KEY'] = SECRET_KEY
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:testpassword@localhost:81/db'
app.config['SECRET_KEY'] = 'gcfgsdhxzncvbsjhuytsgf236uteq2e2t17dcz'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
from .rest import api
app.register_blueprint(api, url_prefix='/api')
from . import views

# login_manager = LoginManager(app)


@app.route('/')
def hello_world():  # put application's code here
    return render_template('index.html')


if __name__ == '__main__':
    db.init_app(app)
    db.create_all()
    app.run(debug=True, use_reloader=True)
