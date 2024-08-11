import json
from youtube_wrapper_py.data_api import YouTubeDataAPI


with open('tests/Data/sample_video_details.json', 'r') as f:
    video_details = json.load(f)



api = YouTubeDataAPI()

def test_get_video_details():

    details = api.get_video_details('dQw4w9WgXcQ')


    expected_item = video_details['items'][0]
    actual_item = details['items'][0]


    assert actual_item['id'] == expected_item['id'], 'Video ID mismatch'
    assert actual_item['snippet']['title'] == expected_item['snippet']['title'], 'Video title mismatch'
    assert actual_item['snippet']['channelTitle'] == expected_item['snippet']['channelTitle'], 'Channel title mismatch'
    assert actual_item['snippet']['publishedAt'] == expected_item['snippet']['publishedAt'], 'Published date mismatch'
    assert actual_item['snippet']['description'] == expected_item['snippet']['description'], 'Description mismatch'

def test_search_videos():
    keyword = "Overwatch 2"
    related_terms = ['blizzard' , 'overwatch' , 'activision']


    videos = api.search_videos(keyword)


    assert len(videos['items']) == 10, f"Expected 10 videos, but got {len(videos['items'])}"


    for video in videos['items']:
        title = video["snippet"]["title"].lower()
        description = video["snippet"]["description"].lower()

        

        
        assert any(term in title or term in description for term in [keyword.lower()] + related_terms), \
            f"Keyword '{keyword}' or related terms not found in video title '{title}' or description '{description}'"
