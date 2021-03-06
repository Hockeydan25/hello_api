"""
Dan Smestad Capstone 2905 class Python API connections
"""

import requests
from pprint import pprint  # makes printing out put cleaner. first time using this import.
import os                  # needed to get to global key where we set the weather_key key is saved could we encypt  
from datetime import datetime  # needed to deal with time fomort conversions. 

key = os.environ.get('WEATHER_KEY')  # key will be local varial key forword and get the key value to insert into our url
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
    pprint(f'Your current temp: {current_temp[0]}, local time date is {current_temp[1]}, skies are {current_temp[2]}, with a wind speed {current_temp[3]} in {location}.')
    
           
def get_location():
    city, country = '',''  # empty string variables for storing the users choice.  
    while len(city)== 0:  # can't have empty data to request from api checking 
        city = input('Please enter the city you would like: ')
        print(city)
    while len(country)== 0:  # can't have empty data to request from api checking 
        country = input('Please enter a 2-letter country code(example: USA country = US): ').strip()

    location = f'{city}, {country}'
    print(location)            
    return location


def get_current_weather(location):
    try:
        query = {'q': location, 'units': 'imperial', 'appid': key} # picking keys from dictionary 
        response = requests.get(url, params=query)  # request does the query from our params in query variable
        response.raise_for_status()  # raise exception for 400-500 codes. try except blocks should be used.Maybe a network or sever issue.
        data = response.json()  # data holds the json formatted data in a dictionary  
        return data
    except Exception as e:
         print(e)
         print('There was an error making the request.')
        

def get_temp(weather_data):
    try:
       temp = weather_data['main']['temp']  # getting data for temp
       time = weather_data['dt']
       time_date = datetime.fromtimestamp(time)  #  non internalional format  
       description = weather_data['weather'][0]['description']
       wind = weather_data['wind']['speed']
       return  temp, time_date, description, wind #description
    #time_date, description, wind
    except Exception as e:
         print(e)
         print('There was an error making the request.')  # general error message.  
         return 'Unknown?'  # could this be more spefic   


if __name__ == '__main__':
    main()


# query = {'q': 'minneapolis', 'units': 'metric', 'appid': '{key}'}


# data= requests.get(url, params=query).json()  # fetch url api weblink.

# pprint(data)  # pretty print i a readable format.

# temp = data['main']['temp']
# print(f'The current temperature in Minneapolis is {temp}F')  #what params do you need. 

