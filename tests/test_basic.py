
import unittest
from flask import current_app
from myapp.source import create_app, db
from myapp.config import Config


class BaseCase(unittest.TestCase):

    def setUp(self):
        self.app = create_app(Config).test_client()
        self.db = db.get_db()


    # def tearDown(self):
    #     # Delete Database collections after the test is complete
    #     for collection in self.db.list_collection_names():
    #         self.db.drop_collection(collection)