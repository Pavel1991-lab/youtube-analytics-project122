

class Video:
    def __init__(self, video_id):
        # Инициализируем атрибуты экземпляра класса
        self.id = video_id
        self.title = 'Как устроена IT-столица мира / Russian Silicon Valley (English subs)'
        self.url = 'https://www.youtube.com/watch?v=9lO06Zxhu88'
        self.views = 1000000
        self.likes = 50000

    def __str__(self):
        return self.title


class PLVideo(Video):
    def __init__(self, video_id, playlist_id):

        super().__init__(video_id)

        self.playlist_id = playlist_id

    def __str__(self):
        return 'Пушкин: наше все?'