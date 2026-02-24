# Q16: Number Guessing Game
# This program lets the computer pick a random number between 1 and 100.
# The user gets 7 attempts to guess the number.
#
# Logic :
# - Computer picks a random number using random.randint(1, 100)
# - User guesses the number
# - After each guess:
#   if guess > number -> too high
#   if guess < number -> too low
#   if guess == number -> correct
# - Show attempts remaining after each guess
# - If user guesses correctly -> show congratulations and attempts used
# - If user fails in 7 attempts -> reveal the number
# - Ask if user wants to play again
# - Track best score (minimum attempts used to guess correctly)
# - Give hint if guess is within 5 of the number

import random

def number_guessing_game():
    best_score = None  # to track minimum attempts

    while True:
        # Step 1: Computer picks random number
        number = random.randint(1, 100)
        attempts = 7
        used_attempts = 0
        print("\n=== NUMBER GUESSING GAME ===")
        print("Guess the number between 1 and 100. You have 7 attempts.")

        # Step 2: Loop for guesses
        while attempts > 0:
            guess = int(input("Enter your guess: "))
            used_attempts += 1
            attempts -= 1

            if guess == number:
                print(f"Congratulations! You guessed the number in {used_attempts} attempts.")
                # Track best score
                if best_score is None or used_attempts < best_score:
                    best_score = used_attempts
                    print("New best score!")
                break
            elif guess > number:
                print(f"Too high! Attempts remaining: {attempts}")
            else:
                print(f"Too low! Attempts remaining: {attempts}")

            # *if guess is close (within 5)
            if abs(guess - number) <= 5 and guess != number:
                print("Hint: You are very close!")

        # Step 3: If failed
        if guess != number:
            print(f"Sorry, you failed. The number was {number}.")

        # Step 4: Show best score if available
        if best_score is not None:
            print(f"Best score so far: {best_score} attempts")

        # Step 5: Ask to play again
        play_again = input("Do you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye.")
            break

# Step 6: Run the function
number_guessing_game()
