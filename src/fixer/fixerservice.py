import os
import requests


class FixerService:
    def __init__(self):
        self.FIXER_API_ENDPOINT = 'http://data.fixer.io/api/latest'
        self.FIXER_API_KEY = os.environ.get('FIXER_API_KEY', None)

    def get_exchange_rates(self):
        params = {
            'access_key': self.FIXER_API_KEY
        }
        r = requests.get(self.FIXER_API_ENDPOINT, params=params)
        if r.status_code != 200:
            return None
        response = r.json()

        rates = response.get('rates')
        return rates
