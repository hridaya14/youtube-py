from youtube_transcript_api import YouTubeTranscriptApi

class YouTubeTranscriptAPI:
    """
    A class to interact with the YouTube Transcript API.
    """

    def get_transcript_with_translation(self, video_id, languages=['en']):
        """
        Retrieves the transcript with translation for a given video ID.
        
        Args:
            video_id (str): The ID of the video to retrieve the transcript for.
            languages (list of str): List of languages to retrieve the transcript in (default is ['en']).

        Returns:
            list or str: The transcript as a list of dictionaries or an error message if an exception occurs.
        """
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
            if isinstance(transcript, list):
                return transcript

            # Fallback to default language if no transcript is found for requested languages
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
            return transcript

        except Exception as e:
            return f"An error occurred while retrieving the transcript: {str(e)}"
