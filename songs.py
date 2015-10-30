import collections
import random


class Song(object):
    def __init__(self, artist, name, lyrics):
        assert isinstance(artist, str), "artist should be a string"
        assert len(artist) > 0, "artist should have at least one character"
        assert isinstance(name, str), "name should be a string"
        assert len(name) > 0, "name should have at least one character"
        assert isinstance(lyrics, list), "lyrics should be a list"
        # Note that lyrics may be empty logically.
        self.artist = artist
        self.name = name
        self.lyrics = lyrics


def get_shifted_lyrics(song):
    shifted = collections.deque(song.lyrics)
    shifted.rotate(random.randrange(0, len(shifted)))
    return shifted
