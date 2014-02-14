from .base_test_class import BaseTestCase


class WeltCharityUrlTesting(BaseTestCase):

    def test_urls_should_redirect_if_no_leading_slash(self):
        redirect_response = self.tester_app.get('/login', content_type='html/text')
        # Here we want to make sure that our url is correctly being redirected
        self.assertEqual(redirect_response.status_code, 301)

    def test_login_url_exists(self):
        response = self.tester_app.get('/login/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

    def test_register_url_exists(self):
        response = self.tester_app.get('/register/', content_type='html/text')
        self.assertEqual(response.status_code, 200)