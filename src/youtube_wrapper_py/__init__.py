from dotenv import load_dotenv
import os
from .data_api import YouTubeDataAPI
from .transcript_api import YouTubeTranscriptAPI


load_dotenv()


class YouTubeAPI:
    
    # @params
    # api_key - key obtained from the google developer console
    def __init__(self, api_key=None):
        
        self.api_key = api_key or os.getenv('YOUTUBE_API_KEY')
        if not self.api_key:
            raise ValueError("API key must be provided either as a parameter or set in the environment variable 'YOUTUBE_API_KEY'.")
        
        
        self.data_api = YouTubeDataAPI(self.api_key)
        self.transcript_api = YouTubeTranscriptAPI()


    #Function to retrieve both Details and Transcript of a given video
    # @params
    # video_id - video id for the required video
    # languages - list of all languages required in the transcript
    def get_video_info_with_transcript(self, video_id, languages=['en']):
        video_details = self.data_api.get_video_details(video_id)
        transcript = self.transcript_api.get_transcript_with_translation(video_id, languages)
        return {
            'video_details': video_details,
            'transcript': transcript
        }
