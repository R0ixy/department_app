"""
Starts application.
"""
from department_app.loader import app, db

#
# def create_app():
#     app.register_blueprint(page)
#     app.register_blueprint(rest, url_prefix='/api')
#     return app


if __name__ == '__main__':
    db.init_app(app)
    db.create_all()
    app.run(debug=True, use_reloader=True)
