"""
Module contains base test class.
"""
import unittest

from department_app.loader import app, db
from department_app.config import DB_username, DB_password, DB_host, DB_port


class BaseTest(unittest.TestCase):
    """
    Base test case class.
    """

    def setUp(self):
        """
        Setup test client and database before every test case.
        :return:
        """
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['LOGIN_DISABLED'] = True
        app.config["SQLALCHEMY_DATABASE_URI"] =\
            f'mysql+pymysql://{DB_username}:{DB_password}@{DB_host}:{DB_port}/test_db'
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        """
        Teardown database after every test case.
        """
        db.session.remove()
        db.drop_all()


if __name__ == '__main__':
    unittest.main()
