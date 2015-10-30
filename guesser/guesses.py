class Guess(object):
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

    def check_title(self, song):
        return self.title.lower() == song.title.lower()

    def check_artist(self, song):
        return self.artist.lower() == song.artist.lower()
