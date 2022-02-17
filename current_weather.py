"""
Dan Smestad Capstone 2905 class Python API connections
"""
import requests
from pprint import pprint
import os

key = os.environ.get('WEATHER_KEY')
#print(key)

url = 'https://api.openweathermap.org/data/2.5/weather?q=minneapolis,mn,us&units=imperial&appid={key}'
#We can adjust city, state, temp units. understand the url to make requests read url's documnet about the api.

# users can request a change of city and location
# city= input('Enter city you would like: ')
# country= input('Enter country 2-letter code: ')
# location = f'{city}, {country}'

query = {'q': 'minneapolis', 'units': 'metric', 'appid': '{key}'}


data= requests.get(url, params=query).json()  # fetch url api weblink.

pprint(data)  # pretty print i a readable format.

temp = data['main']['temp']
print(f'The current temperature in Minneapolis is {temp}F')  #what params do you need. 

