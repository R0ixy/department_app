"""
Enable logging and start application.
"""
import sys
import logging

from department_app.loader import app, db

# logging
formatter = logging.Formatter(u'%(filename)s [LINE:%(lineno)d] #%(levelname)-8s [%(asctime)s]  %(message)s')

file_handler = logging.FileHandler(filename='app.log', mode='w')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

console_handler = logging.StreamHandler(sys.stdout)
console_handler.setFormatter(formatter)
console_handler.setLevel(logging.DEBUG)

# pylint: disable=no-member
logger = app.logger
logger.handlers.clear()
app.logger.addHandler(file_handler)
app.logger.addHandler(console_handler)
app.logger.setLevel(logging.DEBUG)

werkzeug_logger = logging.getLogger('werkzeug')
werkzeug_logger.handlers.clear()
werkzeug_logger.addHandler(file_handler)
werkzeug_logger.addHandler(console_handler)
werkzeug_logger.setLevel(logging.DEBUG)

# sqlalchemy_logger = logging.getLogger('sqlalchemy.engine')
# sqlalchemy_logger.addHandler(file_handler)
# sqlalchemy_logger.addHandler(console_handler)
# sqlalchemy_logger.setLevel(logging.DEBUG)
if __name__ == '__main__':
    db.init_app(app)
    db.create_all()
    app.run(use_reloader=True)
