import logging

import guesser.guesses
import guesser.loader
import guesser.songs


def print_first_lines(collection, amount):
    for i in range(amount):
        print(collection[i])


def shuffle_and_print_first_lines(song):
    print()
    print_first_lines(guesser.songs.get_shifted_lyrics(song), 2)
    print()


def print_song_artist_and_title(song):
    print("That was", song.title, "by", song.artist + ".")


def check_if_user_wants_to_play():
    positive_answers = ("y", "yes", "yeah", "yup")
    negative_answers = ("n", "no", "nope", "nah")
    while True:
        answer = input("Do you want to play again? ")
        if answer in positive_answers:
            return True
        elif answer in negative_answers:
            return False
        else:
            print("I don't understand that. Please use one of the following:")
            print(" ", " ".join(positive_answers + negative_answers))


def ask_for_guesses():
    title = input("Guess the song's title: ")
    artist = input("Guess the song's artist: ")
    print()
    return guesser.guesses.Guess(title, artist)


def print_score(score):
    print("Your score so far:", score)


def initialize_logger():
    logging.basicConfig(filename="log.log", format="%(asctime)-15s %(levelname)s %(message)s", level=logging.DEBUG)


def mainloop():
    score = 0
    while True:
        random_song = guesser.songs.Song(**guesser.loader.get_random_song())
        shuffle_and_print_first_lines(random_song)
        user_guesses = ask_for_guesses()
        if user_guesses.check_title(random_song) and user_guesses.check_artist(random_song):
            print("You got everything right.")
            score += 5
        elif user_guesses.check_title(random_song):
            print("You only got the title right.")
            score += 2
        elif user_guesses.check_artist(random_song):
            print("You only got the artist right.")
            score += 2
        else:
            print("You are wrong.")
            score -= 1
        print_song_artist_and_title(random_song)
        print_score(score)
        if not check_if_user_wants_to_play():
            break


if __name__ == '__main__':
    initialize_logger()
    mainloop()
