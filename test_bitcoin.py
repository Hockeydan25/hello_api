import unittest
from unittest import TestCase
from unittest.mock import patch

import bitcoin

class TestBitcoin(TestCase):
    """ mock the user input and for it to return a value to use for testing 
        # todo - test error conditions     """

    @patch('builtins.input', side_effect=['EUR'])  # list of mock inputs here
    def test_get_currency_choice(self, mock_input):
        country = bitcoin.get_currency_choice()  # testing the input is checking correctly housrs entered.
        self.assertEqual('EUR', country)

    @patch('builtins.input', side_effect=['200'])  # list of mock inputs here
    def test_get_cash_amount(self, mock_input):
        country = bitcoin.get_cash_amount()  # testing the input is checking correctly housrs entered.
        self.assertEqual(200, country)          

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

    ##TODO - finish code
    @patch('bitcoin.extract_rate', return_value=[])
    def test_extract_rate(self, mock_response):   


    @patch('extract_rate.request_rates')  # 
    def test_extract_rate(self, mock_rates):  # test mthod
        mock_rate = 123.4567                       # mock rate to use for testing nt a real value from API 
        # api ptyhon dict data and then we use our mock_rate varabile in place of the data from the call.
        example_api_responce = {"rates":{"CAD": mock_rate}, "rate": "USD",}  
        mock_rates.side_effect = [example_api_responce]  # tells function to use our mock example api.
        converted = extract_rate.convert_dollars_to_target(100, 'EUR')  # value to use with with test run
        expected = 12345.67              # expected is the mock_rate * 100    
        self.assertEqual(expected, converted)  # two arguments to assert to eaqual.    
        
       

if __name__ == '__main__':
    unittest.main()        

 
