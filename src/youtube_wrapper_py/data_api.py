from googleapiclient.discovery import build
import os

class YouTubeDataAPI:
    """
    A class to interact with the YouTube Data API.
    
    Attributes:
        api_key (str): API key obtained from the Google Developer Console.
        youtube (Resource): YouTube API client resource.
    """

    def __init__(self, api_key=None):
        """
        Initializes the YouTubeDataAPI class with the provided API key or from the environment variable.
        
        Args:
            api_key (str): Optional API key. If not provided, it will be fetched from the environment variable.
        """
        self.api_key = api_key or os.getenv('YOUTUBE_API_KEY')
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)

    def get_video_details(self, video_id):
        """
        Retrieves relevant details for a given video ID.
        
        Args:
            video_id (str): The ID of the video to retrieve details for.

        Returns:
            dict: The response from the YouTube API.
        """
        request = self.youtube.videos().list(
            part="snippet,statistics",
            id=video_id
        )
        response = request.execute()
        return response

    def search_videos(self, query, max_results=10):
        """
        Retrieves a list of videos based on a keyword.
        
        Args:
            query (str): Keyword used to filter the list of videos.
            max_results (int): Number of results to be displayed (default is 10).

        Returns:
            dict: The response from the YouTube API.
        """
        request = self.youtube.search().list(
            part="snippet",
            q=query,
            maxResults=max_results
        )
        response = request.execute()
        return response

    def list_channel_videos(self, channel_id, max_results=10):
        """
        Retrieves a list of videos for a given channel ID.
        
        Args:
            channel_id (str): The ID of the channel to retrieve videos from.
            max_results (int): Number of results to be displayed (default is 10).

        Returns:
            dict: The response from the YouTube API.
        """
        request = self.youtube.search().list(
            part="snippet",
            channelId=channel_id,
            maxResults=max_results,
            order="date"
        )
        response = request.execute()
        return response
