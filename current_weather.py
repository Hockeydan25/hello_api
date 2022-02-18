"""
Dan Smestad Capstone 2905 class Python API connections
"""

import requests
from pprint import pprint  # not needed here in updated version.
import os
from datetime import datetime

key = os.environ.get('WEATHER_KEY')
#print(key)

url = 'https://api.openweathermap.org/data/2.5/weather' #?q=minneapolis,mn,us&units=imperial&appid={key}'
#We can adjust city, state, temp units. understand the url to make requests read url's documnet about the api.

# users can request a change of city and location
# city= input('Enter city you would like: ')
# country= input('Enter country 2-letter code: ')
# location = f'{city}, {country}'
def main():
    
    location = get_location()
    weather_data = get_current_weather(location)
    current_temp = get_temp(weather_data)
    pprint(f'current temp and time{current_temp}f in {location}')
    
           
def get_location():
    city, country = '',''  # empty string variables for storing the users choice.  
    while len(city)== 0:  # can't have empty data to request from api checking 
        city = input('Please enter the city you would like: ')
        print(city)
    while len(country)== 0:  # can't have empty data to request from api checking 
        country = input('Please enter the 2-letter (USA country = us) contry you would like: ').strip()

    location = f'{city}, {country}'
    print(location)            
    return location


def get_current_weather(location):
    try:
        query = {'q': location, 'units': 'imperial', 'appid': key}
        response = requests.get(url, params=query)
        response.raise_for_status()  # raise exception for 400-500 codes. try except blocks should be used.Maybe a network or sever issue.
        data = response.json() 
        return data
    except Exception as e:
         print(e)
         print('There was an error making the request.')
        

def get_temp(weather_data):
    try:
       temp = weather_data['main']['temp']
       time = weather_data['dt']
       time_date = datetime.fromtimestamp(time)
       description = weather_data['weather'][0]['description']
       wind = weather_data['wind']['speed']
       return  temp, time_date, description, wind #description
    #time_date, description, wind
    except Exception as e:
         print(e)
         print('There was an error making the request.') 
         return 'Unknown?'   

if __name__ == '__main__':
    main()


# query = {'q': 'minneapolis', 'units': 'metric', 'appid': '{key}'}


# data= requests.get(url, params=query).json()  # fetch url api weblink.

# pprint(data)  # pretty print i a readable format.

# temp = data['main']['temp']
# print(f'The current temperature in Minneapolis is {temp}F')  #what params do you need. 

