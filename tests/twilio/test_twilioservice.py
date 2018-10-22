import os
import unittest
from unittest.mock import MagicMock 
from test.support import EnvironmentVarGuard 
from src.twilio.twilioservice import TwilioService


class TestTwilioService(unittest.TestCase):
    def setUp(self):
        self.env = EnvironmentVarGuard()
        self.env.set('TWILIO_ACCOUNT_SID', 'MY_TWILIO_ACCOUNT_SID')
        self.env.set('TWILIO_AUTH_TOKEN', 'MY_TWILIO_AUTH_TOKEN')

    def test_send_message(self):
        with self.env:
            # given
            message_data = {
                'body': 'My message',
                'from_':'whatsapp:+14155238886',
                'to':'whatsapp:+5511964498206',
            }

            twilio_service = TwilioService()
            twilio_service.client = MagicMock()
            twilio_service.client.messages = MagicMock()
            twilio_service.client.messages.create = MagicMock()

            # when
            twilio_service.send_message(message_data)

            # then
            twilio_service.client.messages.create.assert_called_with(
                body='My message',
                from_='whatsapp:+14155238886',
                to='whatsapp:+5511964498206'
            )
