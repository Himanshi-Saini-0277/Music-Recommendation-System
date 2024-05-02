import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random

CLIENT_ID = "  "
CLIENT_SECRET = "  "

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_song_info(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=search_query, type="track")
    
    if results and results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        album_cover_url = track["album"]["images"][0]["url"]
        return track["name"], artist_name, album_cover_url
    else:
        return song_name, artist_name, "https://i.posting.cc/0QNxYz4V/social.png"

def recommend(selected_mode):
    mood_keywords = {
        "Happy": ["happy", "joyful", "uplifting"],
        "Sad": ["sad", "melancholic", "tearful"],
        "Energetic": ["energetic", "dynamic", "exciting"],
        "Relaxed": ["relaxed", "calm", "peaceful"]
    }

    filtered_songs = []
    for keyword in mood_keywords.get(selected_mode, []):
        search_results = sp.search(q=keyword, type="track", limit=5)
        if search_results and search_results["tracks"]["items"]:
            for track in search_results["tracks"]["items"]:
                song_name = track["name"]
                artist_name = track["artists"][0]["name"]
                filtered_songs.append((song_name, artist_name))
    
    return filtered_songs

def detect_mood(user_input):
    return random.choice(["Happy", "Sad", "Energetic", "Relaxed"])

st.header('Music Recommender System')

user_input = st.text_input("How are you feeling today?")

if st.button('Detect Mood and Show Recommendation'):
    detected_mood = detect_mood(user_input)
    if detected_mood:
        st.write(f"Detected mood: {detected_mood}")
        recommended_music_info = recommend(detected_mood)
        if recommended_music_info:
            col1, col2 = st.columns(2)
            for song_name, artist_name in recommended_music_info:
                song_name, artist_name, album_cover_url = get_song_info(song_name, artist_name)
                with col1:
                    st.text(f"Song: {song_name}")
                    st.text(f"Artist: {artist_name}")
                    st.image(album_cover_url, width=200)
                col1, col2 = col2, col1 
        else:
            st.write("No recommendations available.")
    else:
        st.write("Could not detect mood. Please provide more information.")
