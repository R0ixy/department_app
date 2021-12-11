"""
Module contains base test class.
"""
import unittest

from department_app.models.department_model import Department
from department_app.models.employee_model import Employee
from department_app import app, db
from department_app.config import DB_username, DB_password, DB_host, DB_port


class BaseTest(unittest.TestCase):
    """
    Base test case class.
    """

    @staticmethod
    def fill_db():
        """
        Fill database with test data.
        """
        department = Department(uuid='a4152167-a788-4c39-a232-d45a205aa678',
                                name='Test Department',
                                description='Test Description')
        db.session.add(department)
        db.session.commit()
        employee = Employee(uuid='1',
                            full_name='John Smith',
                            salary=20000,
                            date_of_birth='1987-06-06',
                            position='Developer',
                            department_uuid='a4152167-a788-4c39-a232-d45a205aa678')
        db.session.add(employee)
        db.session.commit()

    def setUp(self):
        """
        Setup test client and database before every test case.
        :return:
        """
        app.config['TESTING'] = True
        app.config['DEBUG'] = False
        app.config['LOGIN_DISABLED'] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = \
            f'mysql+pymysql://{DB_username}:{DB_password}@{DB_host}:{DB_port}/test_db'
        self.app = app.test_client()
        db.create_all()
        self.fill_db()

    def tearDown(self):
        """
        Teardown database after every test case.
        """
        db.session.remove()
        db.drop_all()


if __name__ == '__main__':
    unittest.main()
