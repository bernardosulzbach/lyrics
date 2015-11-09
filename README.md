# Lyric Guesser

![Travis CI](https://travis-ci.org/mafagafogigante/lyric-guesser.svg?branch=master)

A small Python 3 game of lyrics guessing.
It shows you a part of a song and you must guess what it is.

Just issue

    $ python3 main.py

to play the game.

## Developing

You can use

    $ nosetests3

to run all tests.

## Adding, maintaining lyrics

Do not mention that a song is a cover. I foresee this being an issue, but
having to say that something is a cover and remembering whose the original is
is just annoying.

## Project Structure
Directory   |  description
------------|-----------------------------------------------------
`guesser/`  |  contains all application logic.
`sources/`  |  has all text files required to generate the lyrics.
`tests/`    |  contains all the tests.
