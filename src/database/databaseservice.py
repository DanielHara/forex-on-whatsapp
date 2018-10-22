from pymongo import MongoClient


class DatabaseService:
    def __init__(self):
        CONNECTION_STRING = 'mongodb://localhost:27017/'

        self.client = MongoClient(CONNECTION_STRING)
        self.model = self.client['bitcoin-alert-database']

    def create_dump_database(self):
        users = self.model.users

        user = {
            'name': 'Daniel Hara',
            'phone_number': '5511964498206',
            'assets': [
                'USD',
                'EUR',
                'BRL',
                'BIT'
            ]
        }
        user_id = users.insert_one(user).inserted_id
        if user_id:
            print('inserted successfully!')
