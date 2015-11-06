import collections
import random


class Song(object):
    def __init__(self, artist, title, lyrics):
        assert isinstance(artist, str), "artist should be a string"
        assert len(artist) > 0, "artist should have at least one character"
        assert isinstance(title, str), "title should be a string"
        assert len(title) > 0, "title should have at least one character"
        assert isinstance(lyrics, list), "lyrics should be a list"
        assert len(lyrics) >= 2, "song should have at least two lines"
        self.artist = artist
        self.title = title
        self.lyrics = lyrics


class ShiftedLyrics(object):
    """
    The lyrics of a song, possibly shifted, as if they were rolled a few lines forward.
    """

    def __init__(self, lyrics):
        """
        Creates a new ShiftedLyrics object.
        :param lyrics: a list of strings
        """
        assert isinstance(lyrics, list), "lyrics should be a list of strings"
        lyrics = collections.deque(lyrics)
        # Split begin and end for the indentation used in the command line apply to both strings.
        lyrics.appendleft("--- BEGIN ---")
        lyrics.append("--- END ---")
        rotate_amount = random.randrange(0, len(lyrics))
        lyrics.rotate(rotate_amount)
        self.lyrics = tuple(lyrics)
        start_index = rotate_amount
        end_index = (len(self.lyrics) - 1 + rotate_amount) % len(self.lyrics)
        self.free_indices = (start_index, end_index)

    def get(self, count):
        """
        Returns the first count shifted lines. Lines indicating the beginning and ending of the song are not counted.
        """
        result = []
        index = 0
        while count > 0:
            result.append(self.lyrics[index])
            if index not in self.free_indices:
                count -= 1
            index += 1
        return result

    def get_line_count(self):
        """
        Returns how many lines make up the lyrics of the song.
        """
        return len(self.lyrics) - 2
