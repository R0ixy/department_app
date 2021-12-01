"""
Loads all necessary modules and configs.
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

from department_app.config import SECRET_KEY, DB_username, DB_password, DB_host, DB_port

app = Flask(__name__, static_url_path='/department_app/static/')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = f'mysql+pymysql://{DB_username}:{DB_password}@{DB_host}:{DB_port}/db'
app.config['SECRET_KEY'] = SECRET_KEY
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)

from department_app.rest import rest
from department_app.views import page

app.register_blueprint(page)
app.register_blueprint(rest, url_prefix='/api')
