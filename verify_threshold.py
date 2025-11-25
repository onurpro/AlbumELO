import sys
import os
import requests
from sqlalchemy.orm import Session

# Add backend to path
sys.path.append(os.path.join(os.getcwd(), "backend"))

from backend import models, database

BASE_URL = "http://localhost:8000"
USERNAME = "test_threshold_user"
SOURCE = "lastfm"

def setup_test_data():
    db = database.SessionLocal()
    try:
        # Clear existing data
        db.query(models.Album).filter(models.Album.username == USERNAME).delete()
        db.query(models.UserSettings).filter(models.UserSettings.username == USERNAME).delete()
        
        # Add test albums
        albums = [
            models.Album(username=USERNAME, source=SOURCE, name="Low Plays", artist_name="Artist A", playcount=10, image_url="", url=""),
            models.Album(username=USERNAME, source=SOURCE, name="Medium Plays", artist_name="Artist B", playcount=50, image_url="", url=""),
            models.Album(username=USERNAME, source=SOURCE, name="High Plays", artist_name="Artist C", playcount=100, image_url="", url="")
        ]
        db.add_all(albums)
        db.commit()
        print("Test data seeded.")
    finally:
        db.close()

def verify_api():
    # 1. Test Default (Threshold 0)
    print("\nTesting Default Threshold (0)...")
    resp = requests.get(f"{BASE_URL}/api/stats/{USERNAME}?source={SOURCE}")
    albums = resp.json()
    print(f"Got {len(albums)} albums.")
    assert len(albums) == 3
    
    # 2. Set Threshold to 20
    print("\nSetting Threshold to 20...")
    requests.post(f"{BASE_URL}/api/settings/{USERNAME}?source={SOURCE}", json={"scrobble_threshold": 20})
    
    resp = requests.get(f"{BASE_URL}/api/stats/{USERNAME}?source={SOURCE}")
    albums = resp.json()
    print(f"Got {len(albums)} albums.")
    names = [a['name'] for a in albums]
    print(f"Albums: {names}")
    
    assert len(albums) == 2
    assert "Low Plays" not in names
    assert "Medium Plays" in names
    assert "High Plays" in names
    
    # 3. Set Threshold to 60
    print("\nSetting Threshold to 60...")
    requests.post(f"{BASE_URL}/api/settings/{USERNAME}?source={SOURCE}", json={"scrobble_threshold": 60})
    
    resp = requests.get(f"{BASE_URL}/api/stats/{USERNAME}?source={SOURCE}")
    albums = resp.json()
    print(f"Got {len(albums)} albums.")
    names = [a['name'] for a in albums]
    print(f"Albums: {names}")
    
    assert len(albums) == 1
    assert "High Plays" in names
    
    print("\nSUCCESS: Threshold verification passed!")

if __name__ == "__main__":
    setup_test_data()
    verify_api()
