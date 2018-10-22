import requests


class CoindeskService:
    def __init__(self):
        self.COINDESK_ENDPOINT = 'https://api.coindesk.com/v1/bpi/currentprice.json'

    def get_bitcoin_rate_in_dollars(self):
        r = requests.get(self.COINDESK_ENDPOINT)
        if r.status_code != 200:
            return None
        response = r.json()

        usd_rate = response.get('bpi').get('EUR').get('rate_float')
        return usd_rate
