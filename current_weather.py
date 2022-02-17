"""
Dan Smestad Capstone 2905 class Python API connections
"""
from distutils.log import error
import requests
from pprint import pprint  # not needed here in updated version.
import os

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
    weather_data = get_current_weather(location, key)
    current_temp = get_temp(weather_data)
    print('current{current_temp}f')

def get_location():
    city, country = '',''  # empty string variables for storing the users choice.  
    while len(city)== 0:  # can't have empty data to request from api checking 
        city = input('Please enter the city you would like: ')
        print(city)
    while len(country)== 0:  # can't have empty data to request from api checking 
        country = input('Please enter the 2-letter (USA country = us) contry you would like: ').strip()

    location = f'{city}', {country}            
    return location

def get_current_weather(location,key):
    try:
        query = {'q': location, 'units': 'imperial', 'appid': key}
        response = requests.get(url, params=query)
        response.raise_for_status()  # raise exception for 400-500 codes. try except blocks should be used.Maybe a network or sever issue.
        data = response.json() 
        return data, None
    except Exception as e:
         print(e)
         print('There was an error making the request.')
        

def get_temp(weather_data):
    try:
       temp = weather_data['main']['temp']
       return temp

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

