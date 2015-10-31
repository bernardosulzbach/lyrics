# The file that converts all plain text lyrics into JSON.
# The first line of the text file identifies the artist, the second one identifies the title of the opus, and the
# remaining text represents the lyrics.

import json


def read_lines_from_file(filename):
    return open(filename).readlines()


def get_clean_lines_from_file(filename):
    lines = read_lines_from_file(filename)
    # Remove leading and tailing whitespace.
    lines = [line.strip() for line in lines]
    # Remove empty lines.
    lines = [line for line in lines if line != '']
    return lines


if __name__ == '__main__':
    prepared_lines = get_clean_lines_from_file('lyrics.txt')
    output = open('lyrics.json', 'w')
    dictionary = {"artist": prepared_lines[0], "title": prepared_lines[1], "lyrics": prepared_lines[2:]}
    json.dump(dictionary, output)
