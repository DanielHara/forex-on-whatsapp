from pymongo import MongoClient


class DatabaseService:
    def __init__(self):
        CONNECTION_STRING = 'mongodb://localhost:27017/'

        self.client = MongoClient(CONNECTION_STRING)
        self.model = self.client['bitcoin-alert-database']
