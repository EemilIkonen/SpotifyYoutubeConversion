import os
from os.path import join, dirname
from dotenv import load_dotenv

# Load .env file
dotenv_path = join(dirname(__file__), ".env")
load_dotenv(dotenv_path)

# Set up Spotify API credentials
SPOTIFY_CLIENT_ID = os.environ.get("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.environ.get("SPOTIFY_CLIENT_SECRET")

# Set up Youtube API credentials
YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY")
