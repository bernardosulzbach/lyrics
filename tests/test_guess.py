from unittest import TestCase

import guesser.songs
import guesser.guesses


class TestGuess(TestCase):
    def test_check_title_base_case(self):
        song = guesser.songs.Song("artist", "right", ["A", "B"])
        right_guess = guesser.guesses.Guess("artist", "right")
        self.assertTrue(right_guess.check_title(song))
        wrong_guess = guesser.guesses.Guess("artist", "wrong")
        self.assertFalse(wrong_guess.check_title(song))

    def test_check_title_should_ignore_case(self):
        song = guesser.songs.Song("artist", "Right", ["A", "B"])
        right_guess = guesser.guesses.Guess("artist", "right")
        self.assertTrue(right_guess.check_title(song))
        wrong_guess = guesser.guesses.Guess("artist", "Wrong")
        self.assertFalse(wrong_guess.check_title(song))

    def test_check_artist_base_case(self):
        song = guesser.songs.Song("right", "title", ["A", "B"])
        right_guess = guesser.guesses.Guess("right", "title")
        self.assertTrue(right_guess.check_artist(song))
        wrong_guess = guesser.guesses.Guess("wrong", "title")
        self.assertFalse(wrong_guess.check_artist(song))

    def test_check_artist_should_ignore_case(self):
        song = guesser.songs.Song("Right", "title", ["A", "B"])
        right_guess = guesser.guesses.Guess("right", "title")
        self.assertTrue(right_guess.check_artist(song))
        wrong_guess = guesser.guesses.Guess("Wrong", "title")
        self.assertFalse(wrong_guess.check_artist(song))
