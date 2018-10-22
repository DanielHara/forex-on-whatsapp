from injectable import autowired
from src.database.databaseservice import DatabaseService


class UserService:
    @autowired
    def __init__(self, *, database_service: DatabaseService):
        self.database_service = database_service

    def insert_user(self, user_data):
        if not user_data.get('phone_number'):
            return None

        users = self.database_service.model.users
        return users.insert_one(user_data).inserted_id

    def get_users(self):
        users = self.database_service.model.users
        return users.find({})

    def delete_users_with_phone_number(self, phone_number):
        if phone_number:
            users = self.database_service.model.users
            return users.remove({'phone_number': phone_number})
        return None
