# Lyric Guesser

![Travis CI](https://travis-ci.org/mafagafogigante/lyric-guesser.svg?branch=master)

A small Python 3 game of lyrics guessing.
It shows you a part of a song and you must guess what it is.

Just issue

    $ python3 guesser/main.py

to play the game.

## Project Structure
Directory   |  description
------------|-----------------------------------------------------
`gatherer/` |  contains a stub for the Scrapy crawler.
`guesser/`  |  contains all application logic.
`sources/`  |  has all text files required to generate the lyrics.
`tests/`    |  contains all the tests.
