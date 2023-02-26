import contextlib;
import pathlib;
import random;
from string import ascii_letters, ascii_uppercase;
from rich.console import Console;
from rich.theme import Theme;

console = Console(width=40, theme=Theme({"warning": "red on yellow"})); 

# for easy update
NUM_LETTERS = 5
NUM_GUESSES = 6
WORDS_PATH = pathlib.Path(__file__).parent / "wordlist.txt"

def main():
    # find the current word.
    word = get_random_word(WORDS_PATH.read_text(encoding="utf-8").split("\n"));

    # create board
    guesses = ["_" * NUM_LETTERS] * NUM_GUESSES

    with contextlib.suppress(KeyboardInterrupt): #allows to easy restart 
        # where are start guessing - main loop
        for idx in range(NUM_GUESSES):
            refresh_page(headline=f"Guess {idx + 1}"); #provide header
            show_guesses(guesses, word); # create table to display

            guesses[idx] = guess_word(previous_guesses=guesses[:idx]); #pass as reference

            #short circuit
            if guesses[idx] == word:
                break;

            # end game
            game_over(guesses, word, guessed_correctly=guesses[idx] == word);

def refresh_page(headline):
    console.clear(); 
    # rule added decorative line
    console.rule(f"[bold blue]:glowing_star: {headline} :glowing_star:[/]\n");

def get_random_word(word_list):
    if words := [
        word.upper()
        for word in word_list # create an array to go through
        if len(word) == NUM_LETTERS and all(letter in ascii_letters for letter in word) # validate letters will be readable
    ]:
        return random.choice(words);
    else:
        console.print(f"No words of length {NUM_LETTERS} in the word list", style="warning");
        raise SystemExit();


def show_guesses(guesses, word):
        
    letter_status = {letter: letter for letter in ascii_uppercase}; #dictionary letter check
    
    for guess in guesses:
        styled_guess = []

        for letter, correct in zip(guess, word):
            if letter == correct:
                style = "bold white on green";
            elif letter in word:
                style = "bold white on yellow";
            elif letter in ascii_letters:
                style = "white on #666666";
            else:
                style = "dim"
            styled_guess.append(f"[{style}]{letter}[/]");
        
            if letter != "_":
                letter_status[letter] = f"[{style}]{letter}[/]"

        console.print("".join(styled_guess), justify="center");

    console.print("\n" + "".join(letter_status.values()), justify="center"); #show tracker

# error handling
def guess_word(previous_guesses):

    guess = console.input("\nGuess word: ").upper();

    if guess in previous_guesses:
        console.print(f"You've already guessed {guess}.", style="warning");
        return guess_word(previous_guesses);

    if len(guess) != NUM_LETTERS:
        console.print("Your guess must be 5 letters.", style="warning");
        return guess_word(previous_guesses)

    if any((invalid := letter) not in ascii_letters for letter in guess):
        console.print(
            f"Invalid letter: '{invalid}'. Please use English letters.",
            style="warning",
        );
        return guess_word(previous_guesses);

    return guess;

def game_over(guesses, word, guessed_correctly):
    refresh_page(headline="Game Over");
    show_guesses(guesses, word); 

    if guessed_correctly:
        console.print(f"\n[bold white on green]Correct, the word is {word}[/]")
    else:
        console.print(f"\n[bold white on red]Sorry, the word was {word}[/]")


if __name__ == "__main__":
    main(); # run main

