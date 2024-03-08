import settings
from spotify_service import SpotifyService
from youtube_service import YoutubeService

spotify_client_id = settings.SPOTIFY_CLIENT_ID
spotify_client_secret = settings.SPOTIFY_CLIENT_SECRET
youtube_api_key = settings.YOUTUBE_API_KEY

url = "https://open.spotify.com/track/3n3Ppam7vgaVa1iaRUc9Lp"

spotify_service = SpotifyService(spotify_client_id, spotify_client_secret)
print(spotify_service.extract_id(url))
print(spotify_service.get_type(url))
print(spotify_service.get_track_info(spotify_service.extract_id(url)))
