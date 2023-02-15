import pathlib
import random
from string import ascii_letters

def main():
    # find the current word.
    words_path = pathlib.Path(__file__).parent / "wordlist.txt"; #location of file where words are stored.
    word = get_random_word(words_path.read_text(encoding="utf-8").split("\n")); #param is the list of words you want to pick from

    # where are start guessing - main loop
    for guess_num in range(1,7):
        guess = input(f"\nGuess {guess_num}: ").upper(); # verify that the guess will match the all upper current word

        show_guess(guess, word);
        if guess == word: #validate if these are correct.
            break; #only exit if they guess correctly.
    
    # end game
    else:
        game_over(...);

def get_random_word(word_list):
    words = [
        word.upper()
        for word in word_list # create an array to go through
        if len(word) == 5 and all(letter in ascii_letters for letter in word) # validate letters will be readable
    ];

    return random.choice(words);

def show_guess(guess, word): #
    #3 types of options for letters provided in guess
    # verify letter is valid amd in correct location
    correct_letters = { 
        letter for letter, correct in zip(guess, word) if letter == correct
    } # ZIP: element-by-element comparisons between elements, in our case, the guess and the word.

    # correct letters, wrong location
    misplaced_letters = set(guess) & set(word) - correct_letters # remove the already accounted for letter

    # set() and set() provide intersecting elements

    # letters not included in word.
    wrong_letters = set(guess) - set(word) 

    print("Correct letters: ",", ".join(sorted(correct_letters)));
    print("Misplaced letters: ",", ".join(sorted(misplaced_letters)));
    print("Wrong letters: ",", ".join(sorted(wrong_letters)));

def game_over(word):
    print(f"The word was {word}");

if __name__ == "__main__":
    main(); # run main
