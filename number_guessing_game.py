# Number Guessing Game - Oasis Infobyte Internship

import random

def guess_game():
    print("=== Welcome to the Number Guessing Game ===")
    number_to_guess = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Guess a number between 1 and 100: "))
            attempts += 1

            if guess < number_to_guess:
                print("Too low! Try again.\n")
            elif guess > number_to_guess:
                print("Too high! Try again.\n")
            else:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.\n")

# Run the game
guess_game()
