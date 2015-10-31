from unittest import TestCase

import guesser.loader


class TestResources(TestCase):
    def test_resources(self):
        all_songs = guesser.loader.get_all_songs()
        for song in all_songs:
            for field in (song["artist"], song["title"]):
                self.assertEquals(field, field.strip())
            trimmed_lyrics = list(song["lyrics"])
            self.assertTrue(len(trimmed_lyrics) > 0, "song must have at least one line.")
            map(lambda string: string.stip(), trimmed_lyrics)
            self.assertSequenceEqual(song["lyrics"], trimmed_lyrics)
