import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Initializing Spotipy
client_credentials_manager = SpotifyClientCredentials(client_id='ebb7294612234deeacf18e765e445949',
                                                      client_secret='4614ce14af6d4abcaf1b099ee9708953')
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

# Function to search Spotify for the song and return the album cover URL
def get_album_cover_url(track_name, artist_name):
    query = f"track:{track_name} artist:{artist_name}"
    results = sp.search(q=query, type='track', limit=1)
    items = results['tracks']['items']
    if items:
        # Assuming the first search result is the correct track
        album_url = items[0]['album']['images'][0]['url']  # URL of the first (largest) image
        return album_url
    else:
        return "Not Found"

# Load CSV file
df = pd.read_csv("spotify-2023.csv", encoding='ISO-8859-1')

# Add a new column for album cover URLs, initialized with empty strings
df['album_cover_url'] = ''

# Iterate over each row in the DataFrame and fetch the album cover URL
for index, row in df.iterrows():
    df.at[index, 'album_cover_url'] = get_album_cover_url(row['track_name'], row['artist(s)_name'])

# Save the updated DataFrame to a new CSV file
df.to_csv("spotify-2023-updated.csv", index=False)

print("Updated CSV file has been saved.")
