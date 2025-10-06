#DJ,1st,fix the game

import random
def start_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    number_to_guess = random.randint(1, 100)
    max_attempts = 10
    attempts = 1
    game_over = False
    while not game_over:
        #not int, run time error
        guess = input("Enter your guess: ")
        guess = int(guess)
        if attempts >= max_attempts:
            print(f"Sorry, you've used all {max_attempts} attempts. The number was {number_to_guess}.")
            game_over = True
        if guess == number_to_guess:
            print("Congratulations! You've guessed the number!")
            game_over = True
        elif guess > number_to_guess:
            print("Too high! Try again.")
            attempts += 1
        elif guess < number_to_guess:
            print("Too low! Try again.")
            #was never ending, logic error
            attempts += 1
            #continue is redundent, logic error
    print("Game Over. Thanks for playing!")
start_game()
