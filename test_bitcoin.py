import unittest
from unittest import TestCase
from unittest.mock import patch

import bitcoin

class TestBitcoin(TestCase):
    """ mock the user input and for it to return a value to use for testing """

    @patch('bitcoin.request_rates')  # 
    def test_currency_to_target(self, mock_rates):  
        mock_rate = 4123.4567                        
        example_api_responce = {"bpi":{"USD":{"code": "USD", "rate_float": mock_rate}}}
        mock_rates.side_effect = [example_api_responce]  # tells function to use our mock example api.
        converted = bitcoin.convert_currency_to_target(100, 'GBP')  # value to use with with test run
        self.assertEqual(412345.67 , converted)  # two arguments to assert to eaqual, mock_rate * 100.


    @patch('requests.Response.json')  # alternative method here using the response library.
    def test_dollars_to_target_2(self, mock_requests_json):
        mock_rate = 4123.4567  
        example_api_response = {"bpi":{"USD":{"code": "USD", "rate_float": mock_rate}}}
        mock_requests_json.return_value = example_api_response
        converted = bitcoin.convert_currency_to_target(100, 'USD')  #converted is working the math too mock_rate * 100
        expected = 412345.67      # expected is the mock_rate * 100   
        self.assertEqual(expected, converted)  

        
          

     # todo - test error conditions 
    # Currency symbol is not found,
    # Dollar value is not a number,
    # Connection errors to exchange rate API,
    # what else?    



if __name__ == '__main__':
    unittest.main()        

# {"USD": {"code": "USD","symbol": "&#36;","rate": "42,558.1050","description": "United States Dollar","rate_float": 42558.105}   
#"bpi": {"USD": {"code": "USD","symbol": "&#36;","rate": "42,209.5575","description": "United States Dollar","rate_float": 42209.5575}