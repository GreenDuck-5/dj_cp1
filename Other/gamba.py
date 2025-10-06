import random as r
import time as t

def coin_game():
    #coin flipping game
    print("Welcome.")
    t.sleep(1.5)
    print("It's time to play a game.")
    t.sleep(1.5)
    while True:
        user_choice = input("Heads or Tails\n").lower().strip()
        if user_choice == "heads" or "tails":
            pass
        else:
            print("please print valid input")
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
            print("Round 2")
            continue
        else:
            print("You lose")
            t.sleep(0.5)
            print("Goodbye")
            break


coin_game()
