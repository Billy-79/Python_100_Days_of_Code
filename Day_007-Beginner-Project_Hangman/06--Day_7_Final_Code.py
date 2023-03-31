#!/usr/bin/env python3

# Final Code
# Testing code has been commented.
# Keeping track of wrong guesses and let user guess again without losing a life.
# Reveal chosen word if user lose.

import random
import os

def cls():
    os.system("cls" if os.name == "nt" else "clear")
#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
from hangman_words import word_list

chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
from hangman_art import logo
print(logo)

#Testing code
# print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
wrong_guesses = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    cls()

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"\nYou've already guessed {guess}")
    elif guess in wrong_guesses:
        print(f"\n{guess} already entered in wrong guesses.")

    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        #print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word and guess not in wrong_guesses:
        wrong_guesses += guess
        #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"\nYou guessed {guess}, that's not in the word. You lose a life.")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("\nYou lose.")
            print(f"\nThe word was: {chosen_word}")

    #Join all the elements in the list and turn it into a String.
    print(f"\n{' '.join(display)}")
    print(f"\nWrong guesses: {' '.join(wrong_guesses)}")

    #Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("\nYou win.")

    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    from hangman_art import stages
    print(stages[lives])