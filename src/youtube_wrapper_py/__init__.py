from dotenv import load_dotenv
import os
from .data_api import YouTubeDataAPI
from .transcript_api import YouTubeTranscriptAPI

load_dotenv()

class YouTubeAPI:
    """
    A class to interact with YouTube API to retrieve video details and transcripts.
    
    Attributes:
        api_key (str): API key obtained from the Google Developer Console.
        data_api (YouTubeDataAPI): Instance of YouTubeDataAPI to interact with the data API.
        transcript_api (YouTubeTranscriptAPI): Instance of YouTubeTranscriptAPI to interact with the transcript API.
    """

    def __init__(self, api_key=None):
        """
        Initializes the YouTubeAPI class with the provided API key or from the environment variable.
        
        Args:
            api_key (str): Optional API key. If not provided, it will be fetched from the environment variable.
        
        Raises:
            ValueError: If no API key is provided and it's not set in the environment variables.
        """
        self.api_key = api_key or os.getenv('YOUTUBE_API_KEY')
        if not self.api_key:
            raise ValueError(
                "API key must be provided either as a parameter or set in the environment variable 'YOUTUBE_API_KEY'."
            )

        self.data_api = YouTubeDataAPI(self.api_key)
        self.transcript_api = YouTubeTranscriptAPI()

    def get_video_info_with_transcript(self, video_id, languages=['en']):
        """
        Retrieves both video details and transcript for a given video ID.
        
        Args:
            video_id (str): The ID of the video to retrieve details and transcript for.
            languages (list of str): List of languages required in the transcript (default is ['en']).

        Returns:
            dict: A dictionary containing 'video_details' and 'transcript'.
        """
        video_details = self.data_api.get_video_details(video_id)
        transcript = self.transcript_api.get_transcript_with_translation(video_id, languages)
        return {
            'video_details': video_details,
            'transcript': transcript
        }
