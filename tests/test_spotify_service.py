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
        self.maxDiff = None

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
        self.assertEqual(
            self.service.extract_id(
                "https://open.spotify.com/episode/2alNsrB9p601PFWvt50yZx?si=f59dd04963714d44"
            ),
            "2alNsrB9p601PFWvt50yZx",
            "extract_id is not returning the correct ID.",
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
    def test_get_info(self):
        info = self.service.get_info(
            "https://open.spotify.com/episode/2alNsrB9p601PFWvt50yZx?si=f59dd04963714d44",
            "episode",
        )
        expected_keys = [
            "audio_preview_url",
            "description",
            "duration_ms",
            "explicit",
            "external_urls",
            "href",
            "html_description",
            "id",
            "images",
            "is_externally_hosted",
            "is_playable",
            "language",
            "languages",
            "name",
            "release_date",
            "release_date_precision",
            "show",
            "type",
            "uri",
        ]
        self.assertCountEqual(
            info.keys(), expected_keys, "The returned keys are not correct."
        )
        self.assertEqual(
            info["name"], "Guido van Rossum: Python", "The name is not correct."
        )
        self.assertEqual(info["id"], "2alNsrB9p601PFWvt50yZx", "The ID is not correct.")

        info2 = self.service.get_info(
            "https://open.spotify.com/track/6rqhFgbbKwnb9MLmUQDhG6",
            "track",
        )
        expected_keys2 = [
            "album",
            "artists",
            "available_markets",
            "disc_number",
            "duration_ms",
            "explicit",
            "external_ids",
            "external_urls",
            "href",
            "id",
            "is_local",
            "name",
            "popularity",
            "preview_url",
            "track_number",
            "type",
            "uri",
        ]
        self.assertCountEqual(
            info2.keys(), expected_keys2, "The returned keys are not correct."
        )
        self.assertEqual(
            info2["name"],
            "Speak To Me - 2011 Remastered Version",
            "The name is not correct.",
        )
        self.assertEqual(
            info2["id"], "6rqhFgbbKwnb9MLmUQDhG6", "The ID is not correct."
        )
