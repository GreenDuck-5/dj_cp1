import random as r
import time as t
while not not not not not not not not not not not not not not True:
    name = input("Enter name:\n")
    print(f"Welcome, {name}.")
    t.sleep(1)
    print("It's time to play a game.")
    t.sleep(1)
    print("I am going to give you 10 tokens.")
    t.sleep(1)
    print("+10 Tokens")
    tokens = 10
    t.sleep(1)
    print("Now go. Go play my game.")
    
    while True:
        user_input = input("1.) Coin Flip\n2.) Rock, Paper, Scissors\n3.) Lottery\n4.)\n")
        if user_input == "1":
            while True:
                print("This is the coin flipping game.")
                t.sleep(0.5)
                while True:
                    wager = (input(f"How much would you like to gamble? If you win, you double that much. If you lose, you lose that wager.\nYou currently have {tokens} tokens.\n"))
                    print("Enter quit to leave")
                    if wager.isdigit() and int(wager) > tokens:
                        print(f"You can not wager that much.\n You only have {tokens} tokens.")
                        continue
                    elif wager.isdigit() and int(wager) == 0:
                        print("You cannot wager 0.")
                        continue
                    elif wager.isdigit() and int(wager):
                        print(f"You are wagering {wager} coins.")
                        tokens -= int(wager)
                        break
                    elif wager == "quit":
                        break
                    else:
                        print("Please enter a number.")

                while True:
                    user_choice = input("Heads or Tails\n").lower().strip()
                    if user_choice == "heads" or "tails":
                        break
                    else:
                        print("please enter valid input")
                        continue

                print("flipping coin...")
                t.sleep(1)
                print("flipping coin...")
                t.sleep(1)
                print("flipping coin...")
                coin = r.randint(1,2)
                if coin == 1:
                    coin = "heads"
                elif coin == 2:
                    coin = "tails"
                t.sleep(1)
                print(f"The coin is {coin}.")
                t.sleep(1)
                if user_choice == coin:
                    print("You win!")
                    t.sleep(0.5)
                    print(f"You won {int(wager)*2} tokens")
                    tokens += int(wager)*2
                    print(f"You now have {tokens} tokens.")
                    break
                else:
                    print(f"You lost {wager} tokens.")
                    print(f"You now have {tokens} tokens.")
                    break
        if user_input == "2":
            while True:
                print("This is rock, paper, scissors.")
                t.sleep(0.5)
                while True:
                    wager = (input(f"How much would you like to gamble? If you win, you double that much. If you lose, you lose that wager. If you tie, you lose nothing and gain nothing.\nYou currently have {tokens} tokens.\n"))
                    print("Enter quit if you want to leave")
                    if wager.isdigit() and int(wager) > tokens:
                        print(f"You can not wager that much.\n You only have {tokens} tokens.")
                        continue
                    elif wager.isdigit() and int(wager) == 0:
                        print("You cannot wager 0.")
                        continue
                    elif wager.isdigit() and int(wager):
                        print(f"You are wagering {wager} coins.")
                        tokens -= int(wager)
                        break
                    elif wager == "quit":
                        break
                    else:
                        print("Please enter a number.")
                while True:
                    computer_choice = r.randint(1,3)
                    user_choice = input("Rock, Paper, Scissors, Shoot!:\n").strip().lower()
                    if user_choice == "rock" and computer_choice == 1:
                        print("Computer chose rock! You tied.")
                        tokens += int(wager)
                        break
                    elif user_choice == "rock" and computer_choice == 2:
                        print("Computer chose paper! You lost.")
                        break
                    elif user_choice == "rock" and computer_choice == 3:
                        print("Computer chose scissors! You win.")
                        tokens += int(wager)*2
                        break
                    elif user_choice == "paper" and computer_choice == 1:
                        print("Computer chose rock! You win.")
                        tokens += int(wager)*2
                        break
                    elif user_choice == "paper" and computer_choice == 2:
                        print("Computer chose paper! You tied.")
                        tokens += int(wager)
                        break
                    elif user_choice == "paper" and computer_choice == 3:
                        print("Computer chose scissors! You lost.")
                        break
                    elif user_choice == "scissors" and computer_choice == 1:
                        print("Computer chose rock! You lost.")
                        break
                    elif user_choice == "scissors" and computer_choice == 2:
                        print("Computer chose paper! You win.")
                        tokens += int(wager)*2
                        break
                    elif user_choice == "scissors" and computer_choice == 3:
                        print("Computer chose scissors! You tied.")
                        tokens += int(wager)
                        break
                    else:
                        print("Please enter valid input.")
                        continue
                print(f"You now have {tokens} tokens.")
                break
        if user_input == "3":
            print("Welcom to the lottery!")
            print("You can purchase a ticket here!")
            purchase = input("Would you like to buy a ticket? It is 10 tokens.\nEnter quit is you want to leave.")
            if purchase == "quit":
                break
        else:
            print("Please enter valid input.")
        if tokens <= 0:
            print(f"You lose. Goodbye, {name}.")
            break
        else:
            continue
    continue
