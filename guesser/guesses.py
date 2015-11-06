class Guess(object):
    def __init__(self, artist, title):
        self.artist = artist
        self.title = title

    def check_artist(self, song):
        return self.artist.lower() == song.artist.lower()

    def check_title(self, song):
        return self.title.lower() == song.title.lower()
