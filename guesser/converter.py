# The file that converts all plain text lyrics into JSON.
# The first line of the text file identifies the artist, the second one identifies the title of the opus, and the
# remaining text represents the lyrics.

import json
import logging
import os


def get_sources_path():
    path = os.path.join(os.path.dirname(__file__), "..", "sources")
    return path


def read_lines_from_file(filename):
    return open(filename).readlines()


def get_clean_lines_from_file(filename):
    lines = read_lines_from_file(filename)
    # Remove leading and tailing whitespace.
    lines = [line.strip() for line in lines]
    # Remove empty lines.
    lines = [line for line in lines if line != '']
    return lines


def json_from_file(filename):
    prepared_lines = get_clean_lines_from_file(filename)
    if len(prepared_lines) < 4:
        raise Exception("Only got {} lines from {}. Expected at least 4.".format(len(prepared_lines), filename))
    return {"artist": prepared_lines[0], "title": prepared_lines[1], "lyrics": prepared_lines[2:]}


def make_lyrics_file(path):
    logging.debug("Started making the lyrics file.")
    json_list = []
    sources_folder = get_sources_path()
    for root, directories, files in os.walk(sources_folder):
        for file in files:
            json_list.append(json_from_file(os.path.join(root, file)))
    with open(path, 'w') as output:
        json.dump({"songs": json_list}, output)
    logging.debug("Finished making the lyrics file.")
