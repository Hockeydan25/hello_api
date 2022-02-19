"""
Dan Smestad Capstone 2905 class Python API connections
"""
import os
from sqlite3 import Timestamp
import requests
from pprint import pprint
from datetime import datetime

#Example URL
#example url 'https://api.openweathermap.org/data/2.5/forecast?q=minneapolis,us%20code}&appid={key}'

key = os.environ.get('WEATHER_KEY')
query = {'q': 'minneapolis,us', 'units': 'imperial', 'appid': key}

url = 'https://api.openweathermap.org/data/2.5/forecast'



data = requests.get(url, params=query).json()  # could be errors here.
pprint(data)

list_of_forecasts = data['list']  # first key in dict

for forecast in list_of_forecasts:
    temp = forecast['main']['temp']
    time_stamp = forecast['dt']  # time_stamp variable name as I had mis typed the Timestamp internal kep word
    forecast_date = datetime.fromtimestamp(time_stamp)
    print(f'On this forecasted date {forecast_date} and time in Minneapolis, MN it will be {temp}f')
    # end print message for user
    