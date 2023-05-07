import json
import os

from googleapiclient.discovery import build
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

# YT_API_KEY скопирован из гугла и вставлен в переменные окружения
api_key: str = os.getenv('YT_API_KEY')

# создать специальный объект для работы с API
youtube = build('youtube', 'v3', developerKey=api_key)


class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str):
        """Экземпляр инициализируется id канала. Дальше все данные будут подтягиваться по API."""
        self._channel_id = channel_id

    @property
    def title(self):
        """Возвращает название канала."""
        channel = youtube.channels().list(id=self._channel_id, part='snippet').execute()
        return channel['items'][0]['snippet']['title']

    @property
    def video_count(self):
        """Возвращает количество видео на канале."""
        channel = youtube.channels().list(id=self._channel_id, part='statistics').execute()
        return int(channel['items'][0]['statistics']['videoCount'])

    @property
    def link(self):
        """Возвращает ссылку на канал."""
        return f'https://www.youtube.com/channel/{self._channel_id}'

    @classmethod
    def get_service(cls):
        """Возвращает объект для работы с API."""
        return youtube

    def to_json(self, filename: str):
        """Сохраняет данные о канале в json файл."""
        data = {
            'title': self.title,
            'video_count': self.video_count,
            'link': self.link
        }
        with open(filename, 'w') as file:
            json.dump(data, file)

    def print_info(self):
        """Выводит в консоль информацию о канале."""
        channel = youtube.channels().list(id=self._channel_id, part='snippet,statistics').execute()
        print(f"Название канала: {channel['items'][0]['snippet']['title']}")
        print(f"Количество видео: {int(channel['items'][0]['statistics']['videoCount'])}")
        print(f"Ссылка на канал: https://www.youtube.com/channel/{self._channel_id}")


vdud = Channel("UCMCgOm8GZkHp8zJ6l7_hIuA")
