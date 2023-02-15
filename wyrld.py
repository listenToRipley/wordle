import pathlib
import random
from string import ascii_letters

def main():
    # find the current word.
    word = get_random_word(...);

    for guess_num in range(1,7):
        guess = input(f"\nGuess {guess_num}: ").upper();

        show_guess(...);

        if guess == word:
            break;
    
    else:
        game_over(...);

# WORDLIST = pathlib.Path("wordlist.txt") #get word from txt doc.
# words = [
#     word.upper() # make sure the word provided is all upper.
#     for word in WORDLIST.read_text(encoding="utf-8").strip().split("\n") # create an array to go through
#     if len(word) == 5 and all(letter in ascii_letters for letter in word) # validate letters will be readable
# ]

# word = random.choice(words)

# WORD= "SNAKE"

# for guess_num in range(1,7):
#     guess = input(f"\nGuess a word : ").upper() # verify that the guess will match the all upper current word
#     if guess == word: # should keep guessing if the word was not correct
#         print(f"Correct! the word was {word}")
#         break #only exit if they guess correctly.

#     #3 types of options for letters provided in guess
#     # verify letter is valid amd in correct location
#     correct_letters = { 
#         letter for letter, correct in zip(guess, word) if letter == correct
#     } # ZIP: element-by-element comparisons between elements, in our case, the guess and the word.

#     # correct letters, wrong location
#     misplaced_letters = set(guess) & set(word) - correct_letters # remove the already accounted for letter

#     # set() and set() provide intersecting elements

#     # letters not included in word.
#     wrong_letters = set(guess) - set(word) 

#     print("Correct letters: ",", ".join(sorted(correct_letters)))
#     print("Misplaced letters: ",", ".join(sorted(misplaced_letters)))
#     print("Wrong letters: ",", ".join(sorted(wrong_letters)))
# else:
#     print(f"The word was {word}")
