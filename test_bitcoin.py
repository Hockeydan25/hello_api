import unittest
from unittest import TestCase
from unittest.mock import patch, call

import bitcoin

class TestBitcoin(TestCase):
    """ mock the user input and for it to return a value to use for testing """

    @patch('exchange_rate.request_rates')  # 
    def test_currency_to_target(self, mock_rates):  
        mock_rate = 123.4567                        
        example_api_responce = {"bpi":"USD": {"code": "USD","symbol": "&#36;", "rate": "42,558.1050", "description": "United States Dollar", "rate_float": 42558.105}  
        mock_rates.side_effect = [example_api_responce]  # tells function to use our mock example api.
        converted = exchange_rate.convert_dollars_to_target(100, 'USD')  # value to use with with test run
        expected = 12345.67              # expected is the mock_rate * 100    
        self.assertEqual(expected, converted)  # two arguments to assert to eaqual.



if __name__ == '__main__':
    unittest.main()        


# {
#     "USD": {
#       "code": "USD",
#       "symbol": "&#36;",
#       "rate": "42,558.1050",
#       "description": "United States Dollar",
#       "rate_float": 42558.105
#     }    