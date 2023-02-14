WORD = "SNAKE"

for guess_num in range(1,7):
    guess = input(f"\nGuess a word : ").upper() # verify that the guess will match the all upper current word
    if guess == WORD: # should keep guessing if the word was not correct
        print(f"Correct! the word was {WORD}")
        break #only exit if they guess correctly.
    print("Wrong")

#3 types of options for letters provided in guess
# verify letter is valid amd in correct location
correct_letters = { 
    letter for letter, correct in zip(guess, WORD) if letter == correct
}

# correct letters, wrong location
misplaced_letters = set(guess) & set(WORD) - correct_letters 

# letters not included in word.
wrong_letters = set(guess) - set(WORD) 

print("Correct letters: ",", ".join(sorted(correct_letters)))
print("Misplaced letters: ",", ".join(sorted(misplaced_letters)))
print("Wrong letters: ",", ".join(sorted(wrong_letters)))
