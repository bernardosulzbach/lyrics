from unittest import TestCase

import guesser.logic.songs
import guesser.logic.guesses


class TestGuess(TestCase):
    def test_check_title_base_case(self):
        song = guesser.logic.songs.Song("artist", "right", [])
        right_guess = guesser.logic.guesses.Guess("right", "artist")
        self.assertTrue(right_guess.check_title(song))
        wrong_guess = guesser.logic.guesses.Guess("wrong", "artist")
        self.assertFalse(wrong_guess.check_title(song))

    def test_check_title_should_ignore_case(self):
        song = guesser.logic.songs.Song("artist", "Right", [])
        right_guess = guesser.logic.guesses.Guess("right", "artist")
        self.assertTrue(right_guess.check_title(song))
        wrong_guess = guesser.logic.guesses.Guess("Wrong", "artist")
        self.assertFalse(wrong_guess.check_title(song))

    def test_check_artist_base_case(self):
        song = guesser.logic.songs.Song("right", "title", [])
        right_guess = guesser.logic.guesses.Guess("title", "right")
        self.assertTrue(right_guess.check_artist(song))
        wrong_guess = guesser.logic.guesses.Guess("title", "wrong")
        self.assertFalse(wrong_guess.check_artist(song))

    def test_check_artist_should_ignore_case(self):
        song = guesser.logic.songs.Song("Right", "title", [])
        right_guess = guesser.logic.guesses.Guess("title", "right")
        self.assertTrue(right_guess.check_artist(song))
        wrong_guess = guesser.logic.guesses.Guess("title", "Wrong")
        self.assertFalse(wrong_guess.check_artist(song))
