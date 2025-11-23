import os
import requests
from dotenv import load_dotenv
from typing import List, Optional

load_dotenv()

API_KEY = os.getenv("API_KEY")
BASE_URL = "http://ws.audioscrobbler.com/2.0"

def get_data(username: str, page: int) -> Optional[dict]:
    params = {
        'method': 'user.gettopalbums',
        'user': username,
        'api_key': API_KEY,
        'format': 'json',
        'limit': 1000, # Max limit
        'page': page
    }
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        print(f"Error fetching data from Last.fm: {e}")
        return None

def fetch_albums_from_lastfm(username: str) -> List[dict]:
    """
    Fetches all top albums for a user from Last.fm and returns a list of dicts
    ready to be inserted into the database.
    """
    if not API_KEY:
        print("Error: API_KEY not found in environment variables.")
        return []

    albums_data = []
    page = 1
    
    # Initial fetch to get total pages
    data = get_data(username, page)
    if not data or 'topalbums' not in data:
        return []
        
    total_pages = int(data['topalbums']['@attr']['totalPages'])
    
    def parse_page(data):
        for item in data['topalbums']['album']:
            # Get the largest image
            image_url = ""
            if 'image' in item and len(item['image']) > 0:
                image_url = item['image'][-1]['#text']
                
            albums_data.append({
                "name": item['name'],
                "artist_name": item['artist']['name'],
                "url": item['url'],
                "mbid": item.get('mbid'),
                "image_url": image_url,
                "playcount": int(item.get('playcount', 0)),
                "username": username,
                "elo_score": 1500.0,
                "ignored": False
            })

    parse_page(data)
    
    # Fetch remaining pages
    if total_pages > 1:
        for p in range(2, total_pages + 1):
            print(f"Fetching page {p}/{total_pages}...")
            p_data = get_data(username, p)
            if p_data:
                parse_page(p_data)
                
    return albums_data
