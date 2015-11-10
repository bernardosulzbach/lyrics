# Lyric Guesser

![Travis CI](https://travis-ci.org/mafagafogigante/lyrics.svg?branch=master)

A small Python 3 game of lyrics guessing.
It shows you a part of a song and you must guess what it is.

## Playing

You will need [Python **3**](https://www.python.org/downloads/). As the game is
written in pure python, you will not need any additional libraries.

After you have Python 3, you can download the [latest snapshot as a .zip file]
(https://github.com/mafagafogigante/lyrics/archive/master.zip) and extract it.

Then you just issue

    $ python3 main.py

to play the game in the folder of the game.

> The game supposedly runs in all majors platforms. If you have any
> compatibility issues, just email me and I'll be glad to help you out.

## Developing

Follow PEP-8 and remember to check that all tests pass before opening a PR.

## Adding, maintaining lyrics

Do not add covers. Only original songs are allowed.

## Project Structure
Directory   |  description
------------|-----------------------------------------------------
`sources/`  |  has all text files required to generate the lyrics.
`lyrics/`   |  contains all application logic.
`tests/`    |  contains all the tests.
