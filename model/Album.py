
class Album():

    def __init__(self, title, artist, songs):
        self.title = title
        self.artist = artist
        self.songs = songs

    @property
    def title(self):
        return self.title

    @property
    def artist(self):
        return self.artist

    @property
    def songs(self):
        return self.songs
