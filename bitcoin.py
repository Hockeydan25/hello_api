"""
Dan Smestad Capstone 2905 class Python API connections\
    # Currency symbol is not found,
    # Dollar value is not a number,
    # Connection errors to exchange rate API,
    # what else?  
"""

import requests
from tkinter import *

def main():
    currency = get_currency_choice()
    cash = get_cash_amount()
    converted = convert_currency_to_target(cash, currency)
    display_result(cash, currency, converted) # output data we want to show the user.

def get_currency_choice():
    """ Get target currency, and return as uppercase symbol. 
    add validation, error handling added. using while loop to check user is inputting data"""
    
    while True:
        try:
            currency = input('Enter a target currency code: EUR, GBP or USD: ')
            currency_list = ['EUR', 'GBP' , 'USD']
            if currency.upper() not in currency_list:  # had to make this upper to work  
                raise ValueError('please use of these symbols EUR, GBP or USD: ')
            elif len(currency) == 0 :
                raise ValueError('please enter a symbols EUR, GBP or USD: ')
            else:      
                return currency.upper()  # converting to upper case
        except:
            print('Alert: please use of these symbols EUR, GBP or USD: ')


def get_cash_amount():

    """ Get number of dollars, validation, error handling added. """
    while True:
        try:
            cash = float(input('Enter amount of dollars to convert: '))
            if cash <= 0:
                raise ValueError('cash amount must be 1 or more.')
            else:
                return cash    
        except:
            print('Enter a positive number.')
        

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
    """ Perform API request, return response, error handling added"""
    try:
        query = {'base': 'USD', 'symbols': currency}  # seup parmerters to get
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json', query)  # URl for rates retreival. 
        response.raise_for_status()  # error code from json chcinking for error codes here
        data = response.json()
        return  data  #requests.get(data, params=params).json()  
    except Exception as e:
         print(e)
         print('There was an error making the request.')  # tested with network down, working [errno 11001] failed to establish new.     

def extract_rate(rates, currency):

    """ Process the JSON response from the API, extract rate data. added error handling  """
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        response.raise_for_status()  # access JSOn content error codes here 
        rates = response.json()
        # print("Entire JSON response")
        # print(jsonResponse) 
        return rates['bpi']['USD']['rate_float']  # dict to quuery for current rate. we could add a print current data time stampt to this.
    except Exception as err:
        print(f'Other error occurred: {err}')   
    
  
def display_result(cash, currency, converted):
    """ Format and display the result """
    print(f'${cash:.2f} {currency} monies is equal to {converted:.2f} of Bitcoin monies.')  # printing summary of query to api with users data.


if __name__ == '__main__':
    main()

    







