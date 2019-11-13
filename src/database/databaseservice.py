import os
from pymongo import MongoClient


class DatabaseService:
    def __init__(self):
        CONNECTION_STRING = os.environ.get('DB_PORT_27017_TCP_ADDR',
            'mongodb://localhost:27017/')

        self.client = MongoClient(CONNECTION_STRING)
        self.model = self.client['bitcoin-alert-database']
