
class Album():

    def __init__(self, album_id, title, artist, songs):
        self.album_id = album_id
        self.title = title
        self.artist = artist
        self.songs = songs

    @property
    def album_id(self):
        return self.album_id

    @property
    def title(self):
        return self.title

    @property
    def artist(self):
        return self.artist

    @property
    def songs(self):
        return self.songs
