import os
import unittest
from unittest.mock import MagicMock 
from src.services.userservice import UserService


class TestTwilioService(unittest.TestCase):
    def make_mocked_database_service(self):
        mocked_database_service = MagicMock()
        mocked_database_service.model = MagicMock()
        mocked_database_service.model.users = MagicMock()
        mocked_database_service.model.users.insert_one = MagicMock()
        mocked_database_service.model.users.find = \
            MagicMock(return_value = ['user 1', 'user 2'])
        mocked_database_service.model.users.remove = \
            MagicMock()

        return mocked_database_service

    def test_insert_user(self):
        mocked_database_service = self.make_mocked_database_service()
        user_service = UserService(database_service=mocked_database_service)

        # given
        user_data = {
            'phone_number': '+5511964498206'
        }

        # when
        user_id = user_service.insert_user(user_data)

        # then
        user_service.database_service.model.users.insert_one.assert_called_with(user_data)

    def test_get_users(self):
        mocked_database_service = self.make_mocked_database_service()
        user_service = UserService(database_service=mocked_database_service)

        assert user_service.get_users() == ['user 1', 'user 2']

    def test_delete_users_with_phone_number(self):
        mocked_database_service = self.make_mocked_database_service()
        user_service = UserService(database_service=mocked_database_service)

        phone_number = '+5511964498206'

        # given
        user_data = {
            'phone_number': phone_number,
        }

        # when
        user_id = user_service.delete_users_with_phone_number(phone_number)

        # then
        user_service.database_service.model.users.remove.assert_called_with(user_data)
