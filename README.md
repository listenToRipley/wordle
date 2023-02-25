# Wordle

This repository holds the code for the Real Python [Build a Wordle Clone With Python and Rich](https://realpython.com/python-wordle-clone/) tutorial.

The tutorial uses the [walrus operator](https://realpython.com/python-walrus-operator/), which was introduced in [Python 3.8](https://realpython.com/python38-new-features/).

The expected functionality of this application should be same as [Wordle](https://www.nytimes.com/games/wordle/index.html).

## Rules

1. Have a 6 letter word that the user has to guess.
2. Provide 6 guesses for the user to attempt to get the correct answer

- They must provide valid characters only.

3. Provide hints to the user to help to guess.

- If the correct letter is guessed, but is in the wrong location, provide the letter highlighted in yellow.
- If the correct letter is guessed in the correct location provide the letter in green.

4. If the user guess the correct work, provide the word in green and a score to the user.

5. If you reach the 6th guess without getting the correct work, provide the word to the user.

## Scoring

Placeholder for scoring.

## How am I going to do this?

1. Create a simple prototype that allows you to guess a secret word and gives you feedback on the individual letters.

2. Make the game more interesting by including a list of words that the game randomly chooses from.

3. Refactor the code to use functions.

4. Add color and style to the game using the Rich library.

5. Provide actionable feedback to your users when they play the game.

6. Improve the user interface by adding the status of all the letters in the alphabet.

## Dependencies

The project uses [Rich](https://rich.readthedocs.io/) for style, color, and formatting in the terminal. You should first create a virtual environment:

```console
$ python -m venv venv
$ source venv/bin/activate
```

You can then install `rich` with `pip`:

```console
(venv) $ python -m pip install rich
```

## Run the Application

Run script:

```console
python wyrld.py
```

Check out the `wordlist.txt` file for a list of the words that are available (in step 2 and later). Edit this file if you want to play with your own words.

### Using Create WordList

This application allows you to added elements from one document to another. Example:

```console
python create_wordlist.py wyrdl.py wordlist.txt
```

## Author

- **Geir Arne Hjelle**, E-mail: [geirarne@realpython.com](geirarne@realpython.com) with contributing notes on this repo from **Natalie Kendrick**, Email: [natalie.m.kendrick@gmail.com](natalie.m.kendrick@gmail.com)

## License

Distributed under the MIT license. See [`LICENSE`](../LICENSE) for more information.

## Notes

### Testing

Used [Alice in Wonderland text](gutenberg.org/cache/epub/11/pg11-images.html)

*Future state* include [Testing built in](https://realpython.com/python-doctest/)

### Other languages

This application is currently set up to work only with the english language. You may need to add regular expression and special sequence matches if you wished to work with another language.

With the [create_wordlist](./create_wordlist.py) you should replace  the following line

```python
   #original
   if all(letter in ascii_letters for letter in word)
   #replace with
   if re.fullmatch(r"\w+", word):
    #add regex to account for new language.
```

Also import `re`

This application uses [Rich](https://rich.readthedocs.io/en/latest/) to provide an interface.
