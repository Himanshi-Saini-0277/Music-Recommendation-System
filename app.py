import streamlit as st
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = "42f5d27a2a6e4ef58622fcb380d40a53"
CLIENT_SECRET = "8eb954410e5e43dda1fef88b50863edb"

client_credentials_manager = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

def get_song_info(song_name, artist_name):
    search_query = f"track:{song_name} artist:{artist_name}"
    results = sp.search(q=search_query, type="track")
    
    if results and results["tracks"]["items"]:
        track = results["tracks"]["items"][0]
        album_cover_url = track["album"]["images"][0]["url"]
        return track["name"], track["artists"][0]["name"], album_cover_url
    else:
        return song_name, artist_name, "https://i.posting.cc/0QNxYz4V/social.png"

def recommend(selected_mode):
    if selected_mode == "Happy":
        recommended_music = [
            ("Happy", "Pharrell Williams"),
            ("Walking on Sunshine", "Katrina and the Waves"),
            ("Can't Stop the Feeling!", "Justin Timberlake"),
            ("I Gotta Feeling", "The Black Eyed Peas"),
            ("Happy Together", "The Turtles")
        ]
    elif selected_mode == "Sad":
        recommended_music = [
            ("Someone Like You", "Adele"),
            ("Yesterday", "The Beatles"),
            ("Hurt", "Johnny Cash"),
            ("Everybody Hurts", "R.E.M."),
            ("Nothing Compares 2 U", "Sinead O'Connor")
        ]
    elif selected_mode == "Energetic":
        recommended_music = [
            ("Eye of the Tiger", "Survivor"),
            ("Thunderstruck", "AC/DC"),
            ("Shake It Off", "Taylor Swift"),
            ("Born to Run", "Bruce Springsteen"),
            ("Fight For Your Right", "Beastie Boys")
        ]
    elif selected_mode == "Relaxed":
        recommended_music = [
            ("Hotel California", "Eagles"),
            ("Wonderwall", "Oasis"),
            ("Imagine", "John Lennon"),
            ("Sitting on the Dock of the Bay", "Otis Redding"),
            ("Redemption Song", "Bob Marley")
        ]
    else:
        recommended_music = []
    
    recommended_music_info = [get_song_info(song_name, artist_name) for song_name, artist_name in recommended_music]
    return recommended_music_info

st.header('Music Recommender System')

mode = st.selectbox("What is your current mood?", ["Happy", "Sad", "Energetic", "Relaxed"])

if st.button('Show Recommendation'):
    recommended_music_info = recommend(mode)
    if recommended_music_info:
        col1, col2 = st.columns(2)
        for song_name, artist_name, album_cover_url in recommended_music_info:
            with col1:
                st.text(f"{song_name} by {artist_name}")
                st.image(album_cover_url, width=200)
            col1, col2 = col2, col1  # Swap columns for the next iteration
    else:
        st.write("No recommendations available.")
