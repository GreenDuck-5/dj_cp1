#DJ, 1st, Rock paper scissors
import random
import time
tie_count = 0 
loss_count = 0
win_count = 0
while True:
    computer_choice = random.randint(1,3)
    start = input("Would you like you like to play rock paper scissors?:\n").strip().lower()
    if start == "no":
        print("ok bye")
        break 
    else:
        print("Welcome!")
    user_choice = input("Rock, Paper, Scissors, Shoot!:\n").strip().lower()
    if user_choice == "rock" and computer_choice == 1:
        print("Computer chose rock! You tied.")
        tie_count += 1
    elif user_choice == "rock" and computer_choice == 2:
        print("Computer chose paper! You lost.")
        loss_count += 1
    elif user_choice == "rock" and computer_choice == 3:
        print("Computer chose scissors! You win.")
        win_count += 1
    elif user_choice == "paper" and computer_choice == 1:
        print("Computer chose rock! You win.")
        win_count += 1
    elif user_choice == "paper" and computer_choice == 2:
        print("Computer chose paper! You tied.")
        tie_count += 1
    elif user_choice == "paper" and computer_choice == 3:
        print("Computer chose scissors! You lost.")
        loss_count += 1
    elif user_choice == "scissors" and computer_choice == 1:
        print("Computer chose rock! You lost.")
        loss_count += 1
    elif user_choice == "scissors" and computer_choice == 2:
        print("Computer chose paper! You win.")
        win_count += 1
    elif user_choice == "scissors" and computer_choice == 3:
        print("Computer chose scissors! You tied.")
        tie_count += 1
    elif user_choice == "no":
        print("ok bye")
        break
    else:
        print("Please enter valid input.")
        continue
    print(f"You have lost: {loss_count} times\nYou have tied: {tie_count} times\nYou have won: {win_count} times")
    time.sleep(1)
    continue