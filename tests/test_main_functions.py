import main

from unittest import TestCase
import random


def random_boolean():
    return random.randint(0, 1) == 1


def randomize_case(string):
    characters = []
    for c in string:
        characters.append(c.upper() if random_boolean() else c.lower())
    return ''.join(characters)


class TestMainFunctions(TestCase):
    def test_all_affirmative_or_negative_answers_are_numeric_or_lowercase(self):
        for answer in main.get_all_answers():
            self.assertTrue(answer.isnumeric() or answer.islower(), "answer {} must be lowercase.".format(answer))

    def test_parse_user_affirmative_or_negative_should_work_as_expected(self):
        for string in main.get_affirmative_answers():
            self.assertTrue(main.parse_user_affirmative_or_negative(randomize_case(string)))
        for string in main.get_negative_answers():
            self.assertFalse(main.parse_user_affirmative_or_negative(randomize_case(string)))

    def test_parse_user_affirmative_or_negative_should_raise_an_error_with_unregistered_words(self):
        for word in ["apple", "banana", "cactus", "doll", "entity", "franchise"]:
            self.assertRaises(ValueError, main.parse_user_affirmative_or_negative, word)
