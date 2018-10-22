from injectable import autowired
from src.twilio.twilioservice import TwilioService
from src.services.userservice import UserService
from src.fixer.fixerservice import FixerService


class SendWhatsappJob:
    @autowired
    def __init__(self, *, user_service: UserService,
                          twilio_service: TwilioService,
                          fixer_service: FixerService):
        self.user_service = user_service
        self.twilio_service = twilio_service
        self.fixer_service = fixer_service

        self.SANDBOX_PHONE_NUMBER = 'whatsapp:+14155238886'

    def send_whatsapp_messages(self):
        users = self.user_service.get_users()
        rates = self.fixer_service.get_exchange_rates()

        for user in users:
            assets = user.get('assets')
            if not assets:
                continue

            message = 'Exchange rates: \n'
            for asset in assets:
                rate = rates.get(asset)
                if rate and asset != 'EUR':
                    message = '{}1 EUR = {} {}\n'.format(message, rate, asset)

            message_data = {
                'body': message,
                'from_': self.SANDBOX_PHONE_NUMBER,
                'to': 'whatsapp:+{}'.format(user['phone_number']),
            }
            self.twilio_service.send_message(message_data)
