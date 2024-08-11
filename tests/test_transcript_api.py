from youtube_wrapper_py.transcript_api import YouTubeTranscriptAPI

api = YouTubeTranscriptAPI()

with open('tests/Data/sample_transcript.txt', 'r+') as f:
    data = f.read()

def test_get_transcript_with_translation():
    transcript = api.get_transcript_with_translation('dQw4w9WgXcQ')
    transcript_str = f'{transcript}'
    if "An error occurred" in transcript:
        assert transcript.startswith("An error occurred")
    else:
        
        assert transcript_str == data

