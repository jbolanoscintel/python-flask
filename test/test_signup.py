import unittest
import json

from src import app
from src import db


class sign_up_test(unittest.TestCase):
    def SetUp(self):
        self.app = app.test_client()
        self.db = db.get_db()

    def successful_signup(self):
        payload = json.dumps{
            "email": "test12345@mail.com",
            "password": "test"
        }

        response = self.app.post(
            '/api/auth/signup', headers={"Content-Type": "application/json"}, data=payload)

        self.assertEqual(str, type(response.json['id']))
        self.assertEqual(200, response.status_code)

    def tearDown(self):
        # Delete Database collections after the test is complete
        for collection in self.db.list_collection_names():
            self.db.drop_collection(collection)
