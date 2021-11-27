import unittest

from department_app.app import app, db


class BaseTest(unittest.TestCase):
    """
    Base test case class.
    """

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:testpassword@127.0.0.1:3306/test_db'  # 3306
        self.app = app.test_client()
        db.create_all()

    def tearDown(self):
        """
        Execute after every test case
        """
        db.session.remove()
        db.drop_all()


if __name__ == '__main__':
    unittest.main()
