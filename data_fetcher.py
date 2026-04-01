import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv('API_KEY', "").strip()
if not API_KEY:
    raise ValueError("API_KEY is missing in .env!")

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
    try:
        res = requests.get(REQUEST_URL + animal, headers=HEADERS, timeout=(3, 7))
        res.raise_for_status()
        data = res.json()
    except requests.exceptions.Timeout:
        raise RuntimeError("Exceeded time limit for API request.")
    except requests.exceptions.ConnectionError:
        raise RuntimeError("API not reachable.")
    except requests.exceptions.HTTPError:
        raise RuntimeError("API HTTP error occurred.")
    except requests.exceptions.JSONDecodeError:
        raise RuntimeError("Invalid response from API.")
    except requests.exceptions.RequestException:
        raise RuntimeError("API error occurred.")
    if isinstance(data, dict):
        if data.get("error") == "Invalid API Key.":
            raise ValueError("Invalid APi key! Add valid API key to .env!")
    return data
