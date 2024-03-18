import settings
from spotify_service import SpotifyService
from youtube_service import YoutubeService

spotify_client_id = settings.SPOTIFY_CLIENT_ID
spotify_client_secret = settings.SPOTIFY_CLIENT_SECRET
youtube_api_key = settings.YOUTUBE_API_KEY

url = "https://open.spotify.com/track/6rqhFgbbKwnb9MLmUQDhG6"

spotify_service = SpotifyService(spotify_client_id, spotify_client_secret)

print(
    spotify_service.get_info(
        spotify_service.extract_id(url), spotify_service.get_type(url)
    )["name"]
)
