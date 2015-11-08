from unittest import TestCase

import guesser.songs
import guesser.guesses


class TestGuess(TestCase):
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

    def test_check_artist_should_ignore_whitespace(self):
        song = guesser.songs.Song("right true", "title", ["A", "B"])
        right_guess = guesser.guesses.Guess("right true", "title")
        self.assertTrue(right_guess.check_artist(song))
        right_guess = guesser.guesses.Guess("right  true", "title")
        self.assertTrue(right_guess.check_artist(song))
        right_guess = guesser.guesses.Guess("right   true", "title")
        self.assertTrue(right_guess.check_artist(song))

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

    def test_check_title_should_ignore_whitespace(self):
        song = guesser.songs.Song("artist", "right true", ["A", "B"])
        right_guess = guesser.guesses.Guess("artist", "right true")
        self.assertTrue(right_guess.check_title(song))
        right_guess = guesser.guesses.Guess("artist", "right  true")
        self.assertTrue(right_guess.check_title(song))
        right_guess = guesser.guesses.Guess("artist", "right   true")
        self.assertTrue(right_guess.check_title(song))

    def test_checks_should_allow_for_small_typos_in_artist(self):
        # It is also asserted that the artist guess check does not influence the title guess check.
        song = guesser.songs.Song("Iron Maiden", "These Colours Don't Run", ["A", "B"])
        perfect_guess = guesser.guesses.Guess("Iron Maiden", "These Colours Don't Run")
        self.assertTrue(perfect_guess.check_artist(song))
        self.assertTrue(perfect_guess.check_title(song))
        artist_one_character_typo = guesser.guesses.Guess("Iron Maden", "These Colours Don't Run")
        self.assertTrue(artist_one_character_typo.check_artist(song))
        self.assertTrue(artist_one_character_typo.check_title(song))
        # Too many mistakes, the following artist guesses should fail.
        artist_too_many_typos = guesser.guesses.Guess("Iron Made", "These Colours Don't Run")
        self.assertFalse(artist_too_many_typos.check_artist(song))
        self.assertTrue(artist_too_many_typos.check_title(song))
        artist_even_more_typos = guesser.guesses.Guess("Air Made", "These Colours Don't Run")
        self.assertFalse(artist_even_more_typos.check_artist(song))
        self.assertTrue(artist_even_more_typos.check_title(song))

    def test_checks_should_allow_for_small_typos_in_title(self):
        # It is also asserted that the title guess check does not influence the artist guess check.
        song = guesser.songs.Song("Iron Maiden", "These Colours Don't Run", ["A", "B"])
        perfect_guess = guesser.guesses.Guess("Iron Maiden", "These Colours Don't Run")
        self.assertTrue(perfect_guess.check_artist(song))
        self.assertTrue(perfect_guess.check_title(song))
        title_one_character_typo = guesser.guesses.Guess("Iron Maiden", "These Colors Don't Run")
        self.assertTrue(title_one_character_typo.check_artist(song))
        self.assertTrue(title_one_character_typo.check_title(song))
        title_two_characters_typo = guesser.guesses.Guess("Iron Maiden", "These Colors Dont Run")
        self.assertTrue(title_two_characters_typo.check_artist(song))
        self.assertTrue(title_two_characters_typo.check_title(song))
        # Too many mistakes, the following title guesses should fail.
        title_too_many_typos = guesser.guesses.Guess("Iron Maiden", "This Colors Do Run")
        self.assertTrue(title_too_many_typos.check_artist(song))
        self.assertFalse(title_too_many_typos.check_title(song))
        title_even_more_typos = guesser.guesses.Guess("Iron Maiden", "Deez Colors Do Run")
        self.assertTrue(title_even_more_typos.check_artist(song))
        self.assertFalse(title_even_more_typos.check_title(song))
