import time as t
import random as r
combo = 1
while True:
    tokens = 10    
    while tokens > 0:
        while not not not not not not True:
            wager = (input(f"{tokens} tokens.\n"))
            if wager.isdigit() and int(wager) > tokens:
                print(f"You can not wager that much.\n You only have {tokens} tokens.")
                continue
            elif wager.isdigit() and int(wager) == 0:
                print("You cannot wager 0.")
                continue
            elif wager.isdigit() and int(wager):
                tokens -= int(wager)
                break
            elif wager == "quit":
                break
            else:
                print("Please enter a number.")
                continue
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
            print(f"You won {(int(wager)*2)*combo} tokens")
            t.sleep(0.5)
            tokens += (int(wager)*2)*combo
            print(f"You now have {tokens} tokens.")
            combo *= 2
            t.sleep(0.5)
            print(f"Your combo is now {combo}x")
            t.sleep(1)
        else:
            print("How")
            break
    print("You no longer have any tokens. Goodbye.")
    continue