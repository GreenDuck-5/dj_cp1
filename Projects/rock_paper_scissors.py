import random


running = True


while running:
    play = input("Would you like to play Rock, Paper, Scissors? Yes or no: ").strip().lower()
    if play == "no":
        print("ok")
        running = False

    else:

        user_choice = input("Rock, Paper, Scissors, Shoot: ").strip().lower()
