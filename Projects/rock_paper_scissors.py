import random


running = True


while running:
    play = input("Would you like to play Rock, Paper, Scissors? Yes or no: ").strip().lower()
    if play == "no":
        print("ok")

    if play == "yes":
        com_choice = random.randint(1,3)
        if com_choice == 1:
            com_choice == "scissors"
        if com_choice == 2:
            com_choice == "paper"
        if com_choice == 3:
            com_choice == "rock"

        user_choice = input("Rock, Paper, Scissors:\n").strip().lower()
        
        # is user picks rock

        if user_choice == "rock" and com_choice == "rock":
            print("Both picked rock! You tied.")
        
        if user_choice =="rock" and com_choice == "paper":
            print("Computer picked paper! You lose.")
        
        if user_choice == "rock" and com_choice == "scissors":
            print("Computer picked scissors! You win.")

        # if user picks paper

        if user_choice == "paper" and com_choice == "paper":
            print("Computer picked paper! You tied.")

        if user_choice == "paper" and com_choice == "rock":
            print("Computer picked rock! You win.")

        if user_choice == "paper" and com_choice == "scissors":
            print("Computer picked scissors! You lose.")

        # if user picks scissors

        if user_choice == "scissors" and com_choice == "rock":
            print("Computer picked scissors! You lose.")
        
        if user_choice == "scissors" and com_choice == "paper":
            print("Computer picked paper! You win.")
        
        if user_choice == "scissors" and com_choice == "scissors":
            print("Computer picked scissors! You tied.")

    else:
        print("no")