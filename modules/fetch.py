import requests
import json
from types import SimpleNamespace

def fetch_player(username):
    try:
        url = f'https://pemonlist.com/api/player/{username}'
        response = requests.get(url)  # GET request
        response.raise_for_status()  # Raise an exception for HTTP errors
        data = response.json()  # Parse the JSON data from the response
        return SimpleNamespace(**data)

    except requests.exceptions.RequestException as error:
        print(f'There has been a problem with your fetch operation fetch_player: {error}')
        raise