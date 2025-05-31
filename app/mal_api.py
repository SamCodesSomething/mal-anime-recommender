import requests
import os

BASE_URL = "https://api.myanimelist.net/v2"


def search_anime_by_title(title, client_id, limit=5):
    # title is the title of anime name, client id is the mal api client id, limit is the limit for results
    print(f"Searching anime by title: {title}") #prints what we are searching for
    url = f"{BASE_URL}/anime" #creates the full API URL for search using BASE_URL
    headers = {"X-MAL-CLIENT-ID": client_id} #sets the http header with client id
    params = {"q": title, "limit": limit} #sets query params
    response = requests.get(url, headers=headers, params=params) #sends get request to mal api
    print(f"Status Code: {response.status_code}") #replies if we are successful
    if response.status_code != 200:
        print(f"Error: {response.text}")
        return None
    data = response.json() #converts response into python dictionary
    print(f"Response data keys: {list(data.keys())}") #prints the keys at top level of json response
    return data


def get_anime_recommendations(anime_id, client_id):
    url = f"{BASE_URL}/anime/{anime_id}/recommendations"
    headers = {"X-MAL-CLIENT-ID": client_id}
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"Error: {response.text}")
        return None
    return response.json()

#results = search_anime_by_title(input("Please enter the anime you wish to search for: "), client_id)
#print(results)