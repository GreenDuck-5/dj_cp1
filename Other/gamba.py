import random as r
import time as t




print("Welcome.")
t.sleep(1.5)
print("It's time to play a game.")
t.sleep(1.5)
print("I am going to give you 10 tokens.")
t.sleep(1)
print("+10 Tokens")
tokens = 10
t.sleep(1)
print("Now go. Go play my game.")
while True:
    user_input = input("1.) Coin Flipping\n2.) \n3.) \n4.)\n")
    if user_input == "1":
        print("This is the coin flipping game")
        t.sleep(0.5)
        while True:
            wager = int(input("How much would you like to gamble? If you win, you double that much.\n"))
            if wager > tokens:
                print(f"You can not wager that much.\n You only have {tokens} tokens.")
                continue
            elif wager == 0:
                print("You cannot wager 0.")
                continue
            else:
                print(f"You are wagering {wager} coins.")
                break

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
                t.sleep(0.5)
                print(f"You won {wager*2} coins")
                tokens += wager*2
                break
            else:
                print("You lose")
                t.sleep(0.5)
                print(f"You lost {wager} coins.")
                t.sleep(0.5)
                print("Goodbye")
                tokens -= wager
                break
    else:
        print("Please enter valid input.")

