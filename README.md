Here’s a more detailed Markdown file for your documentation, including installation instructions for both Windows and Linux/Mac:

---

# `youtube_wrapper_py` Documentation

## Overview

`youtube_wrapper_py` is a Python package designed to simplify interactions with the YouTube Data API and YouTube Transcript API. It provides an easy-to-use interface for retrieving video details, searching for videos, listing channel videos, and fetching video transcripts with support for multiple languages and translations.

---

## Installation

### Prerequisites

Ensure you have Python 3.9 or later installed on your system.

### Installing `youtube_wrapper_py`

You can install the `youtube_wrapper_py` package using `pip`. Below are instructions for both Windows and Linux/MacOS.

#### For Windows:

1. **Open Command Prompt**:
    - Press `Win + R`, type `cmd`, and press `Enter`.

2. **Install the Package**:
    ```bash
    pip install youtube_wrapper_py
    ```

#### For Linux/MacOS:

1. **Open Terminal**:
    - On Linux, press `Ctrl + Alt + T`.
    - On MacOS, press `Cmd + Space`, type `Terminal`, and press `Enter`.

2. **Install the Package**:
    ```bash
    pip install youtube_wrapper_py
    ```

### Verifying the Installation

To verify that the installation was successful, try importing the package in a Python script or an interactive shell:

```python
import youtube_wrapper_py

print("Package installed successfully!")
```

---

## Configuration

### Setting Up Your API Key

To use the YouTube Data API, you need to provide an API key. The recommended approach is to store the API key in a `.env` file for security and convenience.

1. **Create a `.env` File**:
    - In the root directory of your project, create a `.env` file.

    **Windows Command Prompt**:
    ```bash
    echo YOUTUBE_API_KEY=your_youtube_api_key_here > .env
    ```

    **Linux/MacOS Terminal**:
    ```bash
    touch .env
    echo "YOUTUBE_API_KEY=your_youtube_api_key_here" > .env
    ```

2. **Load the Environment Variables**:
    - Ensure your Python code loads the environment variables using `dotenv`.

    ```python
    from dotenv import load_dotenv
    import os

    load_dotenv()

    api_key = os.getenv("YOUTUBE_API_KEY")
    ```

---

## Usage

### 1. **Initialize the API**

First, import and initialize the `YouTubeAPI` class:

```python
from youtube_wrapper_py import YouTubeAPI

# Initialize with the API key loaded from the environment
yt_api = YouTubeAPI()

# Or initialize with the API key directly
# yt_api = YouTubeAPI(api_key="your_api_key")
```

### 2. **YouTube Data API**

The `YouTubeDataAPI` class provides methods to retrieve video details, search for videos, and list videos on a specific channel.

#### a. **Get Video Details**

Retrieve details of a specific YouTube video using its video ID:

```python
video_id = "dQw4w9WgXcQ"
video_details = yt_api.data_api.get_video_details(video_id)
print(video_details)
```

**Output Example**:
```json
{
    "kind": "youtube#videoListResponse",
    "etag": "2mr-gCW8pi9wUp1GKVla7aLt0Rw",
    "items": [
        {
            "kind": "youtube#video",
            "etag": "Pgk1h32cn-vy5870xIxxxdmZ0js",
            "id": "dQw4w9WgXcQ",
            "snippet": {
                "publishedAt": "2009-10-25T06:57:33Z",
                "channelId": "UCuAXFkgsw1L7xaCfnd5JJOw",
                "title": "Rick Astley - Never Gonna Give You Up (Official Music Video)",
        }
        }
    ]
}
```

#### b. **Search for Videos**

Search for videos based on a query string:

```python
query = "Python programming"
search_results = yt_api.data_api.search_videos(query, max_results=5)
print(search_results)
```

**Output Example**:
```json
[
    {
        "title": "Learn Python Programming - Full Course for Beginners",
        "videoId": "rfscVS0vtbw"
    },
    {
        "title": "Python Tutorial for Beginners [Full Course]",
        "videoId": "YYXdXT2l-Gg"
    }
]
```

#### c. **List Channel Videos**

List the most recent videos from a specific YouTube channel:

```python
channel_id = "UCW5YeuERMmlnqo4oq8vwUpg"
channel_videos = yt_api.data_api.list_channel_videos(channel_id, max_results=5)
print(channel_videos)
```

**Output Example**:
```json
[
    {
        "title": "Python Tutorial",
        "videoId": "exampleVideoId1"
    },
    {
        "title": "Advanced Python Techniques",
        "videoId": "exampleVideoId2"
    }
]
```

### 3. **YouTube Transcript API**

The `YouTubeTranscriptAPI` class provides methods to retrieve video transcripts and handle translations.

#### a. **Get Video Transcript**

Retrieve the transcript of a YouTube video, with support for multiple languages:

```python
video_id = "dQw4w9WgXcQ"
transcript = yt_api.transcript_api.get_transcript_with_translation(video_id, languages=['en', 'es'])
print(transcript)
```

**Output Example**:
```json
[
    {"text": "We're no strangers to love", "start": 0.0, "duration": 4.0},
    {"text": "You know the rules and so do I", "start": 4.0, "duration": 4.2},
    ...
]
```

If a transcript is not available, you will receive an appropriate error message.

### 4. **Unified API Interface**

You can also use the unified interface provided by `YouTubeAPI` to get both video details and its transcript in one call:

```python
video_id = "dQw4w9WgXcQ"
result = yt_api.get_video_info_with_transcript(video_id, languages=['en'])
print(result)
```

This function returns a dictionary containing both the video details and its transcript:

**Output Example**:
```json
{
    "video_details": {
        "title": "Never Gonna Give You Up",
        "description": "Official Rick Astley YouTube Channel",
        "viewCount": "1000000000",
        "likeCount": "10000000"
    },
    "transcript": [
        {"text": "We're no strangers to love", "start": 0.0, "duration": 4.0},
        {"text": "You know the rules and so do I", "start": 4.0, "duration": 4.2}
    ]
}
```

---

## Error Handling

### Transcripts Unavailable

If a transcript is not available for a video, the `get_transcript_with_translation` method will return an error message string.

Example:
```python
result = yt_api.transcript_api.get_transcript_with_translation(video_id)
if isinstance(result, str):
    print(f"Error: {result}")
else:
    print(result)
```

---

## Best Practices

- **Environment Variables**: Store sensitive information like API keys in environment variables and access them securely in your code.
- **Error Handling**: Implement proper error handling to manage cases where data is unavailable or API calls fail.
- **Documentation**: Keep your code well-documented to ensure ease of use and maintenance.

---

## License

This package is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

## Contributing

If you wish to contribute to this project, please fork the repository and submit a pull request. Make sure to update tests as appropriate.

---

Save this as `README.md` in the root directory of your project. This will provide detailed guidance for users on how to install and use your package.