
class Track():

    def __init__(self, song_id, title, artist, producers):
        self.song_id = song_id
        self.title = title
        self.artist = artist
        self.producers = producers

    @property
    def song_id(self):
        return self.song_id

    @property
    def title(self):
        return self.title

    @property
    def artist(self):
        return self.artist

    @property
    def producers(self):
        return self.producers

    def __str__(self):
        track_str = "Track: " + self.title + "\n" + "Artist: " + self.artist + "\n" + "Producers: " + self.producers
        return track_str.encode('utf-8')
