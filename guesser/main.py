from guesser import songs, loader


def print_first_lines(collection, amount):
    for i in range(amount):
        print(collection[i])


def shuffle_and_print_first_lines(song):
    print_first_lines(songs.get_shifted_lyrics(song), 2)


def print_song_artist_and_name(song):
    print("That was", song.name, "by", song.artist + ".")


def mainloop():
    random_song = songs.Song(**loader.get_random_song())
    shuffle_and_print_first_lines(random_song)
    print_song_artist_and_name(random_song)


if __name__ == '__main__':
    mainloop()
