"""
Dan Smestad Capstone 2905 class Python API connections
"""

import requests

# data = requests.get('https://catfact.ninja/fact').json()  # url fetching
# print(data)

# fact =data['fact']  # dictionary key
# print(f'A random cat fact for you: {fact}')

 #  non json
try: 
    responce = requests.get('https://catfact.ninja/fact')  # url fetching
    print(responce)  # codes (100-500) show if your request work ok or not. 
    responce.raise_for_status()  # raise exceptionfor 400-500 codes. try except blocks should be used.Maybe a network or sever issue.
    print(responce.text)
    print(responce.json())  # json converts to python dictionary. reads nice and we

    data =responce.json()  # using requests json parser .json()format we get a python diction structor.nice read output. 
    fact =data['fact']  # dictionary key.
    print(f'A random cat fact for you: {fact}')

except Exception as e:
    print(e)
    print('There was an error making the request.')  