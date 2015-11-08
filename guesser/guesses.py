def levenshtein(a, b):
    if len(a) < len(b):
        return levenshtein(b, a)

    # len(s1) >= len(s2)
    if len(b) == 0:
        return len(a)

    previous_row = range(len(b) + 1)
    for i, c1 in enumerate(a):
        current_row = [i + 1]
        for j, c2 in enumerate(b):
            # j+1 instead of j since previous_row and current_row are one character longer
            insertions = previous_row[j + 1] + 1
            deletions = current_row[j] + 1  # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row

    return previous_row[-1]


def normalize_and_check_for_fuzzy_equality(a, b):
    """
    Compares two strings case-insensitively for fuzzy equality according to the rules specified in the --help output.
    """
    words_of_a = [word for word in a.lower().split()]
    words_of_b = [word for word in b.lower().split()]
    if len(words_of_a) != len(words_of_b):
        return False
    # len(words_of_a) == len(words_of_b) is true here
    pairs = [(words_of_a[i], words_of_b[i]) for i in range(len(words_of_a))]
    distances = [levenshtein(*pair) for pair in pairs]
    # We allow for floor(word_count / 2) typos, with a maximum of one typo (levenshtein distance of one) per word.
    return sum(distances) <= int(len(words_of_a) / 2) and all(distance <= 1 for distance in distances)


class Guess(object):
    def __init__(self, artist, title):
        self.artist = artist
        self.title = title

    def check_artist(self, song):
        return normalize_and_check_for_fuzzy_equality(self.artist, song.artist)

    def check_title(self, song):
        return normalize_and_check_for_fuzzy_equality(self.title, song.title)
