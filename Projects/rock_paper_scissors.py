import random


running = True


while running:
    play = input("Would you like to play Rock, Paper, Scissors? Yes or no: ").strip().lower()
    if play == "no":
        print("ok")
        running = False

    else:
        com_choice = random.randint(1,3)
        if com_choice == 1:
            "scissors"
        if com_choice == 2:
            "paper"
        if com_choice == 3:
            "rock"

        user_choice = input("Rock, Paper, Scissors, Shoot: ").strip().lower()
        
