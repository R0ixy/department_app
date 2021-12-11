"""
Module contains class to test department views.
"""
# pylint: disable=no-member
import http

from department_app.tests.conftest import BaseTest


class TestDepartmentViews(BaseTest):
    """
    Class for department views test cases.
    """

    def test_departments(self):
        """
        Test '/departments/' route
        """
        response = self.app.get('/departments/')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_departments_post(self):
        """
        Test '/departments/' route for post request
        """
        response = self.app.post('/departments/',
                                 data={'uuid': 'a4152167-a788-4c39-a232-d45a205aa678',
                                       'title': 'test name',
                                       'description': 'test description'},
                                 follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_add_department_get(self):
        """
        Test '/departments/add/' route
        """
        response = self.app.get('/departments/add/')
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_add_department_post(self):
        """
        Test '/departments/add/' route for post request
        """
        response = self.app.post('/departments/add/', data={'title': 'test name',
                                                            'description': 'test description'},
                                 follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)

    def test_delete_department(self):
        """
        Test '/departments/delete/<uuid>' route
        """
        response = self.app.post('/departments/delete/a4152167-a788-4c39-a232-d45a205aa678',
                                 follow_redirects=True)
        self.assertEqual(response.status_code, http.HTTPStatus.OK)
