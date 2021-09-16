"""
Program: Spotify playlist creator
Author: Subhashish Dhar
Date: 14/09/2021
"""

import os
import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

CLIENT_ID = "a15464f0304b42678d02b71305e78517"
CLIENT_SECRET = os.environ.get("SECRET")
REDIRECT_URI = "http://example.com"
SCOPE = "playlist-modify-private"

# Authorize the spotify account
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope=SCOPE,
        redirect_uri=REDIRECT_URI,
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)

# Create the list of songs
date = input("Tell me for which date you want to look for the top songs? YYYY-MM-DD : ")
BILLBOARD_URL = f"https://www.billboard.com/charts/hot-100/{date}"

response = requests.get(BILLBOARD_URL)

songs_list = []
if response.status_code != 200:
    print("Can't find the webpage. Is the date format OK?")
else:
    soup = BeautifulSoup(response.text, features='lxml')
    songs_list = [song.get_text() for song in
                  soup.find_all(class_="chart-element__information__song")]

# Create the list of song URIs
song_uris = []
year = date.split("-")[0]
for song in songs_list:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")

# Create the playlist
user_id = sp.current_user()["id"]
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
