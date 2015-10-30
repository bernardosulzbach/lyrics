import random
import json
import os


def get_lyrics_json_path():
    """Returns the path of lyrics.json."""
    cur_dir = os.path.dirname(__file__)
    lyrics_json = os.path.join(cur_dir, "res", "lyrics.json")
    return lyrics_json


def get_random_song():
    """Retrieves any song as a dictionary containing artist, title, and lyrics."""
    lyrics_file = open(get_lyrics_json_path())
    song_list = json.load(lyrics_file)["songs"]
    song_data = random.choice(song_list)
    return song_data