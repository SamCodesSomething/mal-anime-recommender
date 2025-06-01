import requests
import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://api.myanimelist.net/v2"
_CLIENT_ID = None

def get_client_id():
    # Retrieve client ID from environment variable
    return os.getenv("MAL_CLIENT_ID")

def search_anime_by_title(title, client_id=None, limit=5):
    # title is the title of anime name, client id is the mal api client id, limit is the limit for results
    url = f"{BASE_URL}/anime" #creates the full API URL for search using BASE_URL
    headers = {"X-MAL-CLIENT-ID": client_id} #sets the http header with client id
    params = {"q": title, "limit": limit,"fields": "id, title, main_picture, mean, num_episodes, genres"} #sets query params
    response = requests.get(url, headers=headers, params=params) #sends get request to mal api
    if response.status_code != 200:
        raise Exception(response.status_code)
    return response.json()

