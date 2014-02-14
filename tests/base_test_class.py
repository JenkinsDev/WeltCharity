from weltcharity import welt_charity

import unittest
import os


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        welt_charity.app.config['TESTING'] = True
        self.tester_app = welt_charity.app.test_client(self)

    def test_index(self):
        response = self.tester_app.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()