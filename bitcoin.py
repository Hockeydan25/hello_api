"""
Dan Smestad Capstone 2905 class Python API connections
"""

import requests
from pprint import pprint  # getting a printout that is more structored for reading

coindesk_url = 'https://api.coindesk.com/v1/bpi/currentprice.json'  # url fetching
print(coindesk_url)  # codes (100-500) show if your request work ok or not. 

responce = requests.get(coindesk_url)  # url fetching
# raise exceptionfor 400-500 codes. try except blocks should be used.Maybe a network or sever issue.
print(responce.text)
data = responce.json()
pprint(data)  # calling pprint here formatting
# curl make a pretty print as nice a pprint.
dollars_exchange_rate = data['bpi']['USD']['rate_float']  # getting dictionary vaules we want 
pprint(dollars_exchange_rate)  # printing . good variable name here.

bitcoin = float(input('Enter your bitcoin amount to convert: '))

bitcoin_value_in_us_dollars = bitcoin * dollars_exchange_rate

print(f'{bitcoin} Bitcoin is eaqual to ${bitcoin_value_in_us_dollars}')