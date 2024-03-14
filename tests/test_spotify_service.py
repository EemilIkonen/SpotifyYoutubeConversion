import sys
import os
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from spotify_service import SpotifyService
import settings

spotify_client_id = settings.SPOTIFY_CLIENT_ID
spotify_client_secret = settings.SPOTIFY_CLIENT_SECRET


class TestSpotifyService(unittest.TestCase):
    def setUp(self):
        self.service = SpotifyService(spotify_client_id, spotify_client_secret)

    def test_test_url(self):
        self.assertTrue(
            self.service.test_url(
                "https://open.spotify.com/track/6rqhFgbbKwnb9MLmUQDhG6"
            )
        )

    def test_extract_id(self):
        self.assertEqual(
            self.service.extract_id(
                "https://open.spotify.com/track/6rqhFgbbKwnb9MLmUQDhG6"
            ),
            "6rqhFgbbKwnb9MLmUQDhG6",
        )

    def test_get_type(self):
        self.assertEqual(
            self.service.get_type(
                "https://open.spotify.com/track/6rqhFgbbKwnb9MLmUQDhG6"
            ),
            "track",
        )

        self.assertEqual(
            self.service.get_type(
                "https://open.spotify.com/episode/6rqhFgbbKwnb9MLmUQDhG6"
            ),
            "episode",
        )

        self.assertEqual(
            self.service.get_type(
                "https://open.spotify.com/show/6rqhFgbbKwnb9MLmUQDhG6"
            ),
            "show",
        )

        self.assertEqual(
            self.service.get_type(
                "https://open.spotify.com/playlist/6rqhFgbbKwnb9MLmUQDhG6"
            ),
            "playlist",
        )
