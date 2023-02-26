import pathlib;
import random;
from string import ascii_letters;
from rich.console import Console;
from rich.theme import Theme;

console = Console(width=40, theme=Theme({"warning": "red on yellow"}, {"bad": "bold red"})); 

def main():
    # find the current word.
    words_path = pathlib.Path(__file__).parent / "wordlist.txt"; #location of file where words are stored.
    word = get_random_word(words_path.read_text(encoding="utf-8").split("\n")); #param is the list of words you want to pick from
    guesses = ["_" * 5] * 6;

    # where are start guessing - main loop
    for idx in range(6):
        refresh_page(headline=f"Guess {idx + 1}"); #provide header
        show_guess(guesses, word); # create table to display
        
        guesses[idx] = input(f"\nGuess {idx + 1}: ").upper()

        #short circuit
        if guesses[idx] == word: 
            break; 
    
        # end game
        game_over(guesses, word);

def refresh_page(headline):
    console.clear(); 
    # rule added decorative line
    console.rule(f"[bold blue]:leafy_green: {headline} :leafy_green:[/]\n");

def get_random_word(word_list):
    words = [
        word.upper()
        for word in word_list # create an array to go through
        if len(word) == 5 and all(letter in ascii_letters for letter in word) # validate letters will be readable
    ];

    return random.choice(words);


def show_guess(guesses, word): 
    for guess in guesses:
        styled_guess = []

        if len(guess) != 5:
            bad_guess(guesses, "len");

        for letter, correct in zip(guess, word):

            if letter not in ascii_letters:
                bad_guess(guesses, None);
            
            if letter == correct:
                style = "bold white on green";
            elif letter in word:
                style = "bold white on yellow";
            elif letter in ascii_letters:
                style = "white on #666666"
            else:
                style = "dim"
            styled_guess.append(f"[{style}]{letter}[/]")
    
    console.print("".join(styled_guess), justify="center")

def bad_guess(guesses, error):
    # TODO: test that bad guesses do not get added to the list.
    if error == "len":
        console.print('Sorry, all guesses must be 5 letters long. Please try again.', style = "bad")
    else: 
        console.print('Sorry, all letter must be from the english alphabet. Please try again', style="bad")
    guesses.pop(); #remove the last items from the guess list. 

def game_over(guesses, word):
    refresh_page(headline="Game Over");
    show_guess(guesses, word); 


if __name__ == "__main__":
    main(); # run main

