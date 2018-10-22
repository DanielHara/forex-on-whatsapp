import unittest
from unittest.mock import MagicMock
from src.jobs.sendwhatsapp import SendWhatsappJob


class TestTwilioService(unittest.TestCase):
    def test_send_whatsapp(self):
        # given
        mocked_user_service = MagicMock()
        mocked_twilio_service = MagicMock()
        mocked_fixer_service = MagicMock()

        mocked_users = [
            {
                'phone_number': '+5511123456789',
                'assets': [
                    'BRL',
                    'USD'
                ],
            },
            {
                'phone_number': '+5511123456780',
                'assets': [
                    'CHF',
                    'USD'
                ],
            }
        ]

        mocked_exchange_rates = {
            'BRL': 4.00,
            'USD': 3.50,
            'CHF': 1.10,
        }

        mocked_user_service.get_users = MagicMock(return_value=mocked_users)
        mocked_fixer_service.get_exchange_rates = MagicMock(return_value=mocked_exchange_rates)
        mocked_twilio_service.send_message = MagicMock()


        # when
        send_whatsapp_job = SendWhatsappJob(user_service=mocked_user_service,
                                            twilio_service=mocked_twilio_service,
                                            fixer_service=mocked_fixer_service)

        send_whatsapp_job.send_whatsapp_messages()

        # then
        message_datas = [
            {
                'body': 'Exchange rates: \n1 EUR = 4.0 BRL\n1 EUR = 3.5 USD\n',
                'from_': 'whatsapp:+14155238886',
                'to': 'whatsapp:++5511123456789',
            },
            {
                'body': 'Exchange rates: \n1 EUR = 1.1 CHF\n1 EUR = 3.5 USD\n',
                'from_': 'whatsapp:+14155238886',
                'to': 'whatsapp:++5511123456780',
            },
        ]

        for message_data in message_datas:
            mocked_twilio_service.send_message.assert_any_call(message_data)
