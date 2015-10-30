import json


def read_lines_from_file(filename):
    text = open('lyrics.txt').read()
    lines = text.split('\n')
    return lines


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
