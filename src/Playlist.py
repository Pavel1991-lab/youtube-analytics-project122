

import isodate

from helper.youtube_api_manual import youtube


class PlayList:
    """Класс для ютуб-плейлиста"""

    def __init__(self, playlist_id: str):
        """Экземпляр инициализируется id плейлиста. Дальше все данные будут подтягиваться по API."""
        self._playlist_id = playlist_id
        self.link = youtube.playlists()
    @property
    def playlist(self):
        """Возвращает название плейлиста."""
        return youtube.playlists()

    @property
    def title(self):
        """Возвращает название плейлиста."""
        playlist = self.playlist.list(id=self._playlist_id, part='snippet').execute()
        return playlist['items'][0]['snippet']['title']

    @property
    def url(self):
        """Возвращает ссылку на плейлист."""
        return f'https://www.youtube.com/playlist?list={self._playlist_id}'

    @property
    def videos(self):
        """Возвращает список видео в плейлисте."""
        videos = []
        next_page_token = None
        while True:
            # Запросить список видео в плейлисте
            res = youtube.playlistItems().list(
                playlistId=self._playlist_id,
                part='snippet',
                maxResults=50,
                pageToken=next_page_token
            ).execute()

            # Добавить каждое видео в список
            for item in res['items']:
                video_id = item['snippet']['resourceId']['videoId']
                video_title = item['snippet']['title']
                videos.append({'id': video_id, 'title': video_title})

            # Проверить, есть ли следующая страница с видео
            next_page_token = res.get('nextPageToken')
            if not next_page_token:
                break

        return videos

    @property
    def total_duration(self):
        """Возвращает строку с суммарной длительностью плейлиста в формате "дни:часы:минуты:секунды"."""
        total_duration = isodate.parse_duration('PT0S')
        for video in self.videos:
            # Запросить длительность видео
            res = youtube.videos().list(
                id=video['id'],
                part='contentDetails'
            ).execute()

            # Получить продолжительность видео и добавить к общей продолжительности плейлиста
            duration = res['items'][0]['contentDetails']['duration']
            video_duration = isodate.parse_duration(duration)
            total_duration += video_duration

        return total_duration

    @property
    def show_best_video(self):
        """Возвращает ссылку на видео с максимальным количеством лайков."""
        if not self.videos:
            return None

        best_video = max(self.videos, key=lambda video: int(video.get('likeCount', 0)))
        return f"https://youtu.be/{best_video['id']}"



