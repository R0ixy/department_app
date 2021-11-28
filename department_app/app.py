"""
Starts application.
"""
from loader import app, db
from rest import api
from views import page
app.register_blueprint(page)
app.register_blueprint(api, url_prefix='/api')

# login_manager = LoginManager(app)


if __name__ == '__main__':
    db.init_app(app)
    db.create_all()
    app.run(debug=True, use_reloader=True)
