import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import re


class SpotifyService:
    """Spotify Service. Requires client ID and client secret to authenticate."""

    def __init__(self, client_id, client_secret):
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyClientCredentials(
                client_id=client_id,
                client_secret=client_secret,
            )
        )

    def extract_id(self, spotify_url):
        url_types = {
            "track": r"/track/(\w+)",
            "episode": r"/episode/(\w+)",
            "show": r"/show/(\w+)",
            "playlist": r"/playlist/(\w+)",
        }

        for url_type, pattern in url_types.items():
            if url_type in spotify_url:
                match = re.search(pattern, spotify_url)
                if match:
                    return match.group(1)

        raise ValueError("Invalid Spotify URL")

    def get_type(self, spotify_url):
        if "track" in spotify_url:
            return "track"
        elif "episode" in spotify_url:
            return "episode"
        elif "show" in spotify_url:
            return "show"
        elif "playlist" in spotify_url:
            return "playlist"
        raise ValueError("Invalid Spotify URL")

    def get_track_info(self, track_id):
        return self.sp.track(track_id)

    def search_track(self, track_info):
        query = f"{track_info['name']} {track_info['artists'][0]['name']}"
        search_response = self.sp.search(q=query, limit=1, type="track")
        return search_response["tracks"]["items"][0]["external_urls"]["spotify"]

    def get_episode_info(self, episode_id):
        return self.sp.episode(episode_id)

    def search_episode(self, episode_info):
        query = f"{episode_info['name']} {episode_info['artists'][0]['name']}"
        search_response = self.sp.search(q=query, limit=1, type="episode")
        return search_response["episodes"]["items"][0]["external_urls"]["spotify"]

    def get_show_info(self, show_id):
        return self.sp.show(show_id)

    def search_show(self, show_info):
        query = f"{show_info['name']} {show_info['artists'][0]['name']}"
        search_response = self.sp.search(q=query, limit=1, type="show")
        return search_response["shows"]["items"][0]["external_urls"]["spotify"]

    def get_playlist_info(self, playlist_id):
        return self.sp.playlist(playlist_id)

    def search_playlist(self, playlist_info):
        query = f"{playlist_info['name']} {playlist_info['artists'][0]['name']}"
        search_response = self.sp.search(q=query, limit=1, type="playlist")
        return search_response["playlists"]["items"][0]["external_urls"]["spotify"]
