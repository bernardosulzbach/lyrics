import random
import json


def get_random_song():
    """Retrieves any song as a dictionary containing artist, name, and lyrics."""
    lyrics_file = open("res/lyrics.json")
    song_list = json.load(lyrics_file)["songs"]
    song_data = random.choice(song_list)
    return song_data
