import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import re
import settings
from googleapiclient.discovery import build


class SpotifyAPI:
    def __init__(self, client_id, client_secret):
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyClientCredentials(
                client_id=settings.SPOTIFY_CLIENT_ID,
                client_secret=settings.SPOTIFY_CLIENT_SECRET,
            )
        )

    # Function to extract track ID from Spotify URL
    def extract_id(self, spotify_url):
        # Check if the URL is for a track, episode, or show
        if "track" in spotify_url:
            # Use regular expression to find the track ID from the URL
            match = re.search(r"/track/(\w+)", spotify_url)
            if match:
                return match.group(1)
            else:
                raise ValueError("Invalid Spotify URL")
        elif "episode" in spotify_url:
            raise ValueError("Invalid URL: Podcasts not currently supported.")
        elif "show" in spotify_url:
            raise ValueError("Invalid URL: Url was for a show, not a track.")
        else:
            raise ValueError("Invalid Spotify URL")

    # Function to get track information from Spotify URL
    def get_track_info(self, spotify_url):
        track_id = self.extract_id(spotify_url)

        # Use the extracted track ID to get track information
        track_info = self.sp.track(track_id)
        return track_info


class YoutubeAPI:
    def __init__(self, api_key):
        self.youtube = build("youtube", "v3", developerKey=api_key)

    # Function to search for a video on YouTube based on track information
    def search_youtube_video(self, track_info):
        query = (
            f"{track_info['name']} {track_info['artists'][0]['name']} official video"
        )
        search_response = (
            self.youtube.search().list(q=query, part="id", type="video").execute()
        )

        if "items" in search_response:
            video_id = search_response["items"][0]["id"]["videoId"]
            return f"https://www.youtube.com/watch?v={video_id}"


client_id = settings.SPOTIFY_CLIENT_ID
client_secret = settings.SPOTIFY_CLIENT_SECRET
youtube_api_key = settings.YOUTUBE_API_KEY

# Example usage
url = "https://open.spotify.com/track/7dS5EaCoMnN7DzlpT6aRn2?si=-vinRd7qT7qnfkv345d4rA"
url2 = "https://open.spotify.com/episode/2DpTFSs33YH8kX4JVAXz3G?si=621389cfa1a440fe"
url3 = "https://open.spotify.com/show/2ZUhk9HxrpjNVge0BELaf1?si=594fad92629a4ea3"
spotify_api = SpotifyAPI(client_id, client_secret)
youtube_api = YoutubeAPI(youtube_api_key)
print(youtube_api.search_youtube_video(spotify_api.get_track_info(url)))
print(youtube_api.search_youtube_video(spotify_api.get_track_info(url2)))
print(youtube_api.search_youtube_video(spotify_api.get_track_info(url3)))
