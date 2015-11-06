import string
from unittest import TestCase

import guesser.songs


def get_list_of_ascii_letters():
    return list(string.ascii_letters)


class TestShiftedLyrics(TestCase):
    def test_shifted_lyrics_should_preserve_all_lines(self):
        lines = get_list_of_ascii_letters()
        shifted_lyrics = guesser.songs.ShiftedLyrics(lines)
        for line in lines:
            self.assertIn(line, shifted_lyrics.get(shifted_lyrics.get_line_count()))

    def test_shifted_lyrics_should_have_correct_line_count(self):
        lines = get_list_of_ascii_letters()
        shifted_lyrics = guesser.songs.ShiftedLyrics(lines)
        self.assertEqual(len(lines), shifted_lyrics.get_line_count())
