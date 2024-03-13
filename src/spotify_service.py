import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import re

# TODO:
# Error handling
# Docstrings
# Type hints
# Tests
# Logging


class SpotifyService:
    """Spotify Service. Requires client ID and client secret to authenticate."""

    def __init__(self, client_id: str, client_secret: str):
        self.sp = spotipy.Spotify(
            auth_manager=SpotifyClientCredentials(
                client_id=client_id,
                client_secret=client_secret,
            )
        )

    def test_url(self, spotify_url: str) -> bool:
        """
        Test if the URL is a valid Spotify URL.

        :param spotify_url: The URL of the Spotify content.
        :return: True if the URL is a valid Spotify URL, False otherwise.
        """
        url_regex = r"https://open.spotify.com/(track|episode|show|playlist)/\w+"

        if re.match(url_regex, spotify_url):
            return True
        else:
            return False

    def extract_id(self, spotify_url: str) -> str:
        """
        Return the ID of the Spotify content based on the URL.

        :param spotify_url: The URL of the Spotify content.
        :return: The ID of the Spotify content.
        """
        url_types = {
            "track": r"/track/(\w+)",
            "episode": r"/episode/(\w+)",
            "show": r"/show/(\w+)",
            "playlist": r"/playlist/(\w+)",
        }

        if self.test_url(spotify_url):
            for url_type, pattern in url_types.items():
                if url_type in spotify_url:
                    match = re.search(pattern, spotify_url)
                    if match:
                        return match.group(1)

        raise ValueError(f"Invalid Spotify URL: {spotify_url}")

    def get_type(self, spotify_url: str) -> str:
        """
        Return the type of the Spotify content based on the URL.

        :param spotify_url: The URL of the Spotify content.
        :return: The type of the Spotify content ("track", "episode", "show", or "playlist").
        """

        if self.test_url(spotify_url):
            if "track" in spotify_url:
                return "track"
            elif "episode" in spotify_url:
                return "episode"
            elif "show" in spotify_url:
                return "show"
            elif "playlist" in spotify_url:
                return "playlist"

        raise ValueError("Invalid Spotify URL")

    def get_info(self, spotify_id: str, spotify_type: str) -> dict:
        """
        Get information about a specific Spotify content based on its ID and type.

        :param spotify_id: The ID of the Spotify content.
        :param spotify_type: The type of the Spotify content ("track", "episode", "show", or "playlist").
        :return: The information about the specified Spotify content.
        """
        if spotify_type == "track":
            return self.sp.track(spotify_id)
        elif spotify_type == "episode":
            return self.sp.episode(spotify_id)
        elif spotify_type == "show":
            return self.sp.show(spotify_id)
        elif spotify_type == "playlist":
            return self.sp.playlist(spotify_id)
        else:
            raise ValueError(
                "Invalid Spotify type. Expected one of: track, episode, show, playlist"
            )

    def search(
        self, name: str, search_type: str, artist: str = None, show: str = None
    ) -> str:
        """
        Search for content on Spotify and return the URL of the first search result.

        :param name: The name of the content to search for.
        :param search_type: The type of content to search for ("track", "episode", "show", or "playlist").
        :param artist: The name of the artist (for tracks only). This is optional.
        :param show: The name of the show (for episodes only). This is optional.
        :return: The Spotify URL of the first search result.
        """
        query = f"{name['name']} {name['artist'] if artist else ''} {name['show'] if show else ''}"
        search_response = self.sp.search(q=query, limit=1, type=search_type)
        return search_response[search_type + "s"]["items"][0]["external_urls"][
            "spotify"
        ]
