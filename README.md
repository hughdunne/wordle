# wordle
Tool to help you solve Wordle by filtering a word list based on the feedback from your guesses.

## Prerequisites

Should work with any recent version of Python.

## Usage

Start a python shell in the directory where you have installed this code, and type:

    from wordle import *
    w = Wordle(wordlist_file)

wordlist_file should be the name of a file which contains a list of five-letter words, one to each line. This repo includes a sample word list file,
wordle-list.txt. To use it, you would type `w = Wordle('wordle-list.txt')`. I make no guarantee that this file contains all possible 5-letter words.

Now suppose you enter the guess "atone" into the Wordle web page and get the feedback 🟨⬜⬜⬜🟩 . You translate the colors grey, yellow and green to 0,
1 and 2 respectively. To filter the word list based on this feedback, give the command:

    w.try_word('atone', '10002')

You will see some output like:

    Narrowed down to 270 matches
    Suggested next guess is ['badge', 'bagie', 'baize', 'barde', 'barge', ...]

The program offers up to 40 suggestions, based on words which match the feedback you have been given so far, and which maximize the number of different
letters in each word and minimize the overlap between the word and your latest guess. Bear in mind that the solution might have a repeated letter and
therefore might not show up in the top 40 suggestions.

You can see the entire filtered word list by typing:

    w.w
