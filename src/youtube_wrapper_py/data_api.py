from googleapiclient.discovery import build
import os


class YouTubeDataAPI:
    
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv('YOUTUBE_API_KEY')
        self.youtube = build('youtube', 'v3', developerKey=self.api_key)

    #Function to retrieve relevant details for a given video
    # @params
    # video_id - video ID of the required video
    def get_video_details(self, video_id):
        request = self.youtube.videos().list(
            part="snippet,statistics",
            id=video_id
        )
        response = request.execute()
        
        return response

    #Function to retrieve a list of videos based on a keyword
    # @params
    # query(str) - keyword used to filter out the list
    # max_results(int) - number of results to be displayed
    def search_videos(self, query, max_results=10):
        request = self.youtube.search().list(
            part="snippet",
            q=query,
            maxResults=max_results
        )
        response = request.execute()
        
        return response

    #Function to retrieve a list of videos for a given channel
    # @params
    # channel_id(str) - ID of required channel
    # max_results(int) - number of results to be displayed
    def list_channel_videos(self, channel_id, max_results=10):
        
        request = self.youtube.search().list(
            part="snippet",
            channelId=channel_id,
            maxResults=max_results,
            order="date"
        )
        response = request.execute()


        return response
