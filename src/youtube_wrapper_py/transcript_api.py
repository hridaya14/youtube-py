from youtube_transcript_api import YouTubeTranscriptApi


class YouTubeTranscriptAPI:

    def get_transcript_with_translation(self, video_id, languages=['en']):
        try:
            
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=languages)
            if isinstance(transcript, list): 
                return transcript

            
            transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['en'])
            return transcript
        
        except Exception as e:
            return f"An error occurred while retrieving the transcript: {str(e)}"
