WORD = "SNAKE"

for guess_num in range(1,7):
    guess = input(f"\nGuess a word : ").upper() # verify that the guess will match the all upper current word
    if guess == WORD: # should keep guessing if the word was not correct
        print(f"Correct! the word was {WORD}")
        break #only exit if they guess correctly.
    print("Wrong")

correct_letters = { # verify letter is valid amd om correct location
    letter for letter, correct in zip(guess, WORD) if letter == correct
}

misplaced_letters = set(guess) & set(WORD) - correct_letters # correct letters, wrong location
wrong_letters = set(guess) - set(WORD) # letters not included in word.

print("Correct letters: ",", ".join(sorted(correct_letters)))
print("Misplaced letters: ",", ".join(sorted(misplaced_letters)))
print("Wrong letters: ",", ".join(sorted(wrong_letters)))
