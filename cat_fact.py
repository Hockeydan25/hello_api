"""
Dan Smestad Capstone 2905 class Python API connections
"""
import logging
import requests

# data = requests.get('https://catfact.ninja/fact').json()  # url fetching
# print(data)

# fact =data['fact']  # dictionary key
# print(f'A random cat fact for you: {fact}')

 #  non json
try: 
    response = requests.get('https://catfact.ninja/fact')  # url fetching
    print(response)  # codes (100-500) show if your request work ok or not. 
    response.raise_for_status()  # raise exceptionfor 400-500 codes. try except blocks should be used.Maybe a network or sever issue.
    print(response.text)
    print(response.json())  # json converts to python dictionary. reads nice and we

    data =response.json()  # using requests json parser .json()format we get a python diction structor.nice read output. 
    fact =data['fact']  # dictionary key.
    print(f'A random cat fact for you: {fact}')

except Exception as e:
    print(e)
    print('There was an error making the request.')  

logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
logging.debug('This message should appear on the console')
logging.info('So should this')
logging.warning('And this, too')    