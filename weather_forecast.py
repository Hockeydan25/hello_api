"""
Dan Smestad Capstone 2905 class Python API connections
"""

import requests
from pprint import pprint  # makes printing out put cleaner. first time using this import.
import os                  # needed to get to global key where we set the weather_key key is saved could we encypt  
from datetime import datetime  # needed to deal with time fomort conversions. 

key = os.environ.get('WEATHER_KEY')  # key will be local varial key forword and get the key value to insert into our url
url = 'https://api.openweathermap.org/data/2.5/forecast'#?lat=35&lon=139&appid=5ec0b48124dcfb49d9ffd7b75d503ee7
#url = 'https://api.openweathermap.org/data/2.5/weather' #?q=minneapolis,mn,us&units=imperial&appid={key}'

## TODO checks: spaces, spelling, more testing,comments, error handling complete
def main():    
    location = get_location()
    weather_data = get_current_weather(location)
    current_forecast = get__five_day_forecast(weather_data)
    pprint(f'Your current temp: {current_forecast}, local time date is {current_forecast}, skies are {current_forecast}, with a wind speed {current_forecast} in {location}.')
    
           
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

    ## TODO international time conversion
    ## TODO windspeed three hour intervals - may need a new url to choose or maybe 5 day has that option.
    ## TODO add a 5 day time frame. Unix Time or UTC. 
def get__five_day_forecast(data):
    list_of_forecasts = data['list']
    try:
       for forecast in list_of_forecasts: 
        temp = forecast['main']['temp']  # getting data for temp.
        time = forecast['dt']
        time_date = datetime.fromtimestamp(time)  #  non internalional format.  
       #description = weather_data['weather'][0]['description']
       #wind = weather_data['wind']['speed']
       return  temp, time_date#, description, wind #description.
    #time_date, description, wind.
    except Exception as e:
         print(e)
         print('There was an error making the request.')  # general error message.  
         return 'Unknown?'  # could this be more spefic   

    ## TODO add logging     

if __name__ == '__main__':
    main()