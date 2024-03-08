import re
from googleapiclient.discovery import build


class YoutubeService:
    """Class for YouTube service. Requires API key to authenticate."""

    def __init__(self, api_key):
        self.youtube = build("youtube", "v3", developerKey=api_key)

    def extract_youtube_id(youtube_url):
        # TODO: Not needed? Can we query the API with the full URL?
        if "youtu.be" in youtube_url:
            match = re.search(r"youtu\.be/([0-9A-Za-z_-]{10,})", youtube_url)
        else:
            match = re.search(r"v=([0-9A-Za-z_-]{10,})", youtube_url)
        return match.group(1) if match else None

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

    def get_video_info(self, video_id):
        # Implementation...
        pass
