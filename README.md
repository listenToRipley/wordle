# Wordle

This repository goes over the [Real Python tutorial on how to build Wordle](https://realpython.com/python-wordle-clone/).

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