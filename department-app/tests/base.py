import unittest

from app import app, db


class BaseTest(unittest.TestCase):
    """
    Base test case class.
    """

    def setUp(self):
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:testpassword@localhost:80/test_db'
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
