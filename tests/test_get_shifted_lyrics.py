from unittest import TestCase

import guesser.songs


class TestSongFunctions(TestCase):
    def test_get_shifted_lyrics(self):
        verses = ["A", "B", "C"]
        song = guesser.songs.Song("band", "song", verses)
        for i in range(10):
            copy_of_verses = list(verses)
            for line in guesser.songs.get_shifted_lyrics(song):
                self.assertIn(line, copy_of_verses)
                copy_of_verses.remove(line)
