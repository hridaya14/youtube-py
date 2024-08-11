from youtube_wrapper_py.transcript_api import YouTubeTranscriptAPI

api = YouTubeTranscriptAPI()

with open('tests/Data/sample_transcript.txt','r+') as f:
    data = f.read()

def test_get_transcript_with_translation():
    transript = api.get_transcript_with_translation('dQw4w9WgXcQ')
    str_transcript = f'{transript}'

    assert str_transcript == data
