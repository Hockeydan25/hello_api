"""
Dan Smestad Capstone 2905 class Python API connections

example downloading binary code. For dog api link give a another link to the 
jpg so two requests are used 
"""

import requests


# dog_json = requests.get('https://dog.ceo/api/breeds/image/random').json()

# img_url = dog_json['message']

# actual_image_response = requests.get(img_url)

# with open('dog.jpg', 'wb') as file:
#     for chunk in actual_image_response.iter_content():
#         file.write(chunk)
kitten_url = 'https://placekitten.com/200/300'  # 

response = requests.get(kitten_url) # fetch the api for the data.

with open('kitten.jpg', 'wb') as file:  # open in writing mode
    for chunk in response.iter_content():  # chunk is a data writting format
        file.write(chunk)  # writes in parts a more controled 
