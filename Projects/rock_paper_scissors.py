import random


running = True


while running:
    play = input("Would you like to play Rock, Paper, Scissors? Yes or no: ").strip().lower()
    if play == "no":
        print("ok")
        running = False

    if play == "yes":
        com_choice = random.randint(1,3)
        if com_choice == 1:
            "scissors"
        if com_choice == 2:
            "paper"
        if com_choice == 3:
            "rock"

        user_choice = input("Rock, Paper, Scissors:\n").strip().lower()
        if user_choice == "rock" and com_choice == "rock":
                print("Both picked rock! You tied.")
        
        if user_choice =="rock" and com_choice == "paper":
                print("Computer picked paper! You lose.")
        
        if user_choice == "rock" and com_choice == "scissors":
                print("Computer picked scissors! You win.")

    else:
         print("Actually answer the question")
         running = False