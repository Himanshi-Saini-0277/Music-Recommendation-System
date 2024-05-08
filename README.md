# Music-Recommendation-System

## Introduction
The Music Mood Recommender System is a Streamlit web application that recommends music tracks based on the user's mood input. It utilizes the Spotipy library to fetch music data from the Spotify API and provides recommendations according to the detected mood.

## Features
- Detect Mood: The system analyzes the user's input to detect their mood using predefined keywords.
- Recommend Music: Based on the detected mood, the system recommends music tracks that match the mood.
- Display Recommendations: The recommended music tracks are displayed along with their song names, artists, and album cover images.

## Requirements
- Streamlit: Install Streamlit library using pip install streamlit.
- Spotipy: Install Spotipy library using pip install spotipy.
- Spotify API Credentials: Obtain Spotify API credentials (Client ID and Client Secret) by registering your application on the Spotify Developer Dashboard.

## Setup
- Set up Spotify API Credentials: Replace the placeholders CLIENT_ID and CLIENT_SECRET with your Spotify API credentials obtained from the Spotify Developer Dashboard.
- Run the Application: Execute the script (python script_name.py) to run the Streamlit web application.

## Usage
- Input Mood: Enter your current mood in the text input field provided.
- Detect Mood and Show Recommendation: Click the button to detect your mood and receive music recommendations based on it.
- View Recommendations: The recommended music tracks will be displayed along with their song names, artists, and album cover images.

## Workflow
1. #### Detect Mood:
- The system analyzes the user's mood input using predefined keywords associated with different moods.
- A random mood is selected if the input does not match any predefined keywords.
2. #### Recommend Music:
- Based on the detected mood, the system fetches music tracks from Spotify using Spotipy.
- It searches for tracks associated with keywords related to the detected mood and retrieves a limited number of recommendations.
3. #### Display Recommendations:
- The recommended music tracks are displayed in a two-column layout.
- Each recommendation includes the song name, artist name, and album cover image.

## Conclusion
The Music Mood Recommender System simplifies the process of discovering music tracks based on the user's mood input. By leveraging the Spotify API and Streamlit framework, it provides an interactive and engaging experience for users to explore music tailored to their current mood.
