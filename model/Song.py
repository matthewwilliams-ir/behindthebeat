
class Song():

    def __init__(self, title, artist, producers):
        self.title = title
        self.artist = artist
        self.producers = producers

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
        return self.artist + " - " + self.title + " (Prod. by." + self.producers + ")"
