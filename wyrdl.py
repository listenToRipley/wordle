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

    bad_guess = False;

    # where are start guessing - main loop
    for idx in range(6):
        guesses[idx] = input(f"\nGuess {idx + 1}: ").upper(); # verify that the guess will match the all upper current word

        if all(letter in ascii_letters for letter in guesses[idx]):
            if len(guesses[idx]) != 5:
                bad_guess = True;
            elif len(guesses[idx]) == 5:
                bad_guess = False; #needs reset
        
            if bad_guess:
                console.print('Sorry, all guesses must be 5 letters long. Please try again.', style = "bad")
                # TODO: test that bad guesses do not get added to the list.
                guesses.pop(); #remove the last items from the guess list. 
    
            else: 
                show_guess(guesses[idx], word);
                if guesses[idx] == word: #validate if these are correct.
                    break; #only exit if they guess correctly.
    
        # end game
        else:
            game_over(word);

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

def show_guess(guesses, word): #
    for guess in guess:
        styled_guess = []
        for letter, correct in zip(guess, word):
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

    def game_over(word):
        refresh_page(headline="Game Over");
        show_guess(guesses, word); 


if __name__ == "__main__":
    main(); # run main

