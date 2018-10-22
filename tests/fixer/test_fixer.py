import responses
import unittest
from unittest.mock import MagicMock 
from src.fixer.fixerservice import FixerService


class TestFixerService(unittest.TestCase):
    @responses.activate
    def test_get_exchange_rates_sucess(self):
        FIXER_API_ENDPOINT = 'http://data.fixer.io/api/latest'

        mocked_response_json = {
            'rates': 'mocked_rates'
        }

        responses.add(responses.GET, FIXER_API_ENDPOINT,
                      json=mocked_response_json, status=200)

        fixer_service = FixerService()
        assert fixer_service.get_exchange_rates() == 'mocked_rates'

    @responses.activate
    def test_get_exchange_rates_failure(self):
        FIXER_API_ENDPOINT = 'http://data.fixer.io/api/latest'

        mocked_response_json = {
            'error': 'failure'
        }

        responses.add(responses.GET, FIXER_API_ENDPOINT,
                      json=mocked_response_json, status=500)

        fixer_service = FixerService()
        assert fixer_service.get_exchange_rates() is None
