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
        self.channel_id = channel_id

    def print_info(self):
        """Выводит в консоль информацию о канале."""
        channel = youtube.channels().list(id=self.channel_id, part='snippet,statistics').execute()
        return channel



vdud = Channel("UCMCgOm8GZkHp8zJ6l7_hIuA")


print(vdud.print_info())