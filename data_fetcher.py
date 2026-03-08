import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY')
REQUEST_URL = 'https://api.api-ninjas.com/v1/animals?name='
HEADERS = {'X-Api-Key': API_KEY}


def fetch_data(animal):
    """
    Make a request to fetch data from an API.
    :param animal: animal to get information about
    :return: a list of animals; each animal is a dictionary:
    {
        'name': ...,
        'taxonomy': {
        ...
        },
        'locations': [
        ...
        ],
        'characteristics': {
        ...
        }
    },
    """
    res = requests.get(REQUEST_URL + animal, headers=HEADERS)
    return res.json()
