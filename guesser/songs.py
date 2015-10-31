import collections
import random


class Song(object):
    def __init__(self, artist, title, lyrics):
        assert isinstance(artist, str), "artist should be a string"
        assert len(artist) > 0, "artist should have at least one character"
        assert isinstance(title, str), "title should be a string"
        assert len(title) > 0, "title should have at least one character"
        assert isinstance(lyrics, list), "lyrics should be a list"
        # Note that lyrics may be empty logically.
        self.artist = artist
        self.title = title
        self.lyrics = lyrics


def get_shifted_lyrics(song):
    shifted = collections.deque(song.lyrics)
    shifted.rotate(random.randrange(0, len(shifted)))
    return shifted
