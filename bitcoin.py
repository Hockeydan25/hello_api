"""
Dan Smestad Capstone 2905 class Python API connections
"""

import requests
from pprint import pprint  # getting a printout that is more structored for reading

def main():
    currency = get_currency_to_choice()
    cash = get_cash_amount()
    converted = convert_currency_to_target(cash, currency)
    display_result(cash, currency, converted) # print

def get_currency_to_choice():
    """ Get target currency, and return as uppercase symbol. 
    TODO add validation, error handling """
    currency = input('Enter target currency code e.g. EUR, GBP or USD: ')  #  get on of three choices from user
    return currency.upper()  # converting to upper case


def get_cash_amount():
    """ Get number of dollars.  TODO add validation, error handling """
    return float(input('Enter amount of dollars to convert: '))   


def convert(amount, exchange_rate):
    """ Convert using the given exchange rate """
    return amount * exchange_rate  


def convert_currency_to_target(cash, target_currency):
    """ Convert amount of dollars to target currency """
    exchange_rate = get_exchange_rate(target_currency) 
    converted = convert(cash, exchange_rate)
    return converted


def get_exchange_rate(currency):
    """ Call API and extra data from response """
    response = request_rates(currency)
    rate = extract_rate(response, currency)
    return rate 

    
def request_rates(currency):
    """ Perform API request, return response. TODO add error handling """
    params = {'base': 'USD', 'symbols': currency}
    coindesk_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'  # URl for rates retreival amaving the changes in only a few minutes. 
    return requests.get(coindesk_url, params=params).json()    


def extract_rate(rates,currency):
    """ Process the JSON response from the API, extract rate data. TODO add error handling  """
    return rates['bpi']['USD']['rate_float']  # dict to quuery for current rate. we could add a print current data time stampt to this.
      
  
def display_result(cash, currency, converted):
    """ Format and display the result """
    print(f'${cash:.2f} {currency} monies is eaqual to {converted:.2f} Bitcoin')  # printing


if __name__ == '__main__':
    main()

    # {
    # "USD": {
    #   "code": "USD",
    #   "symbol": "&#36;",
    #   "rate": "42,558.1050",
    #   "description": "United States Dollar",
    #   "rate_float": 42558.105
    # }
    
   




# # curl make a pretty print as nice a pprint.
#     dollars_exchange_rate = data['bpi']['USD']['rate_float']  # getting dictionary vaules we want 
#     pprint(dollars_exchange_rate)  # printing . good variable name here.






