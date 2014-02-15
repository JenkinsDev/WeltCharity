from flask import session
from .base_test_class import BaseTestCase


class UserTests(BaseTestCase):

    def test__registration_form_data_should_not_redirect_if_invalid_data(self):
        response = self.tester_app.post(
            '/register/',
            data={
                "username": "Malazath",
                "password": "password1234",
                "password_conf": "not the same!",
                "email": "Not a valid email address!"
            },
            content_type="html/text"
        )
        # If the user supplies invalid data then we will just reload the registration view with
        # the errors supplied.  To check this we will simply check if the status code is 200.
        self.assertEqual(response.status_code, 200)

    def test__login_form_logs_user_in_on_correct_data(self):
        response = self.tester_app.post(
            '/login/',
            data={
                "username_or_email": "Aquabeardlb",
                "password": "password1234"
            },
            content_type="html/text"
        )
        self.assertEqual(response.status_code, 301)