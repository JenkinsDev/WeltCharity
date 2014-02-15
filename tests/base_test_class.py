from weltcharity import welt_charity

import unittest
import os
import mongomock


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        welt_charity.app.config['TESTING'] = True
        self.tester_app = welt_charity.app.test_client(self)
        self.tester_db = mongomock.Connection().db.collection

if __name__ == '__main__':
    unittest.main()