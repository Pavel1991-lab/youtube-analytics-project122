
import json
import os

from googleapiclient.discovery import build
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

api_key: str = os.getenv('Api_Key')

youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str):
        self._channel_id = channel_id

    @property
    def channel(self):
        return youtube.channels().list(id=self._channel_id, part='snippet,statistics').execute()['items'][0]

    @property
    def title(self):
        return self.channel['snippet']['title']

    @property
    def video_count(self):
        return int(self.channel['statistics']['videoCount'])

    @property
    def link(self):
        return f'https://www.youtube.com/channel/{self._channel_id}'

    @classmethod
    def get_service(cls):
        return youtube

    def to_json(self, filename: str):
        data = {
            'title': self.title,
            'video_count': self.video_count,
            'link': self.link
        }
        with open(filename, 'w') as file:
            json.dump(data, file)

    def print_info(self):
        channel = self.channel
        print(f"Channel: {channel['snippet']['title']}")
        print(f"Subscribers: {channel['statistics']['subscriberCount']}")
        print(f"Views: {channel['statistics']['viewCount']}")

    def __str__(self):
        return f"{self.title} ({self.link})"

    def __add__(self, other):
        return self.video_count + other.video_count

    def __sub__(self, other):
        return self.video_count - other.video_count

    def __gt__(self, other):
        return self.video_count > other.video_count

    def __ge__(self, other):
        return self.video_count >= other.video_count

    def __lt__(self, other):
        return self.video_count < other.video_count

    def __le__(self, other):
        return self.video_count <= other.video_count

    def __eq__(self, other):
        return self._channel_id == other._channel_id