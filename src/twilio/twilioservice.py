import os
from twilio.rest import Client


class TwilioService:
    def __init__(self):
        self.account_sid = os.environ['TWILIO_ACCOUNT_SID']
        self.auth_token = os.environ['TWILIO_AUTH_TOKEN']

        self.client = Client(self.account_sid, self.auth_token)

    def send_sample_message(self):
        message_data = {
            'body':'Hello there!',
            'from_':'whatsapp:+14155238886',
            'to':'whatsapp:+5511964498206',
        }
        return self.client.messages.create(**message_data)

    def send_message(self, message_data):
        return self.client.messages.create(**message_data)
