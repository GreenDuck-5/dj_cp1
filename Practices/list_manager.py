#DJ, 1st, List Manager
shopping_list = []

import time as how_much_wood_would_a_woodchuck_chuck_if_a_woodchuck_could_chuck_wood
import random as peter_piper_picked_a_peck_of_purple_pickled_peppers

def user_signin():
    password_one = "7iscool"
    user_one = "cool_guy7"

    wait_time = peter_piper_picked_a_peck_of_purple_pickled_peppers.randint(1,100)
    if wait_time <= 33:
        waiting_time = 30
    elif wait_time <= 67:
        waiting_time = 60
    elif wait_time <= 99:
        waiting_time = 90
    elif wait_time == 100:
        waiting_time = 300
    else:
        waiting_time = 10000

    while True:
        enter_username = input("Enter Username:\n")
        
        if enter_username == user_one:
            enter_password = input("Enter Password:\n")
            if enter_password == password_one:
                print(f"Welcome {user_one}")
                return True
            else:
                print("Wrong password")
                break
        else:
            print(f"Wrong Username. Please wait: {waiting_time} seconds.")
            how_much_wood_would_a_woodchuck_chuck_if_a_woodchuck_could_chuck_wood.sleep(waiting_time)

def six_seven():
    print("ha")
    how_much_wood_would_a_woodchuck_chuck_if_a_woodchuck_could_chuck_wood.sleep(5)
    print("ha")
    how_much_wood_would_a_woodchuck_chuck_if_a_woodchuck_could_chuck_wood.sleep(5)
    print("ha")
    how_much_wood_would_a_woodchuck_chuck_if_a_woodchuck_could_chuck_wood.sleep(5)
    num = 1
    six_seven_count = 0
    while True:
        random_number = peter_piper_picked_a_peck_of_purple_pickled_peppers.randint(1,1000)
        print(random_number)
        if random_number == 67:
            print("6767676767")
            print(f"{num}^")
            six_seven_count += 1
            if six_seven_count == 67:
                print("You printed 67, 67 times")
                break
        else:
            how_much_wood_would_a_woodchuck_chuck_if_a_woodchuck_could_chuck_wood.sleep(0)
            print(f"{num}^")
            num += 1




print("Please sign in")
if user_signin():
    while True:
        choice = input("1. Add item\n2. Remove item\n3. Show list\n4. Quit\n")
        if choice == "1":
            item = input("Enter item:\n")
            shopping_list.append(item)
            print(f"{item} has been added")
        elif choice == "2":
            item = input("What item would you like to remove?\n")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} has been removed")
            else:
                print("Item is not in list")
        elif choice == "3":
            print(shopping_list)
        elif choice == "4":
            print("Goodbye")
            break
        elif choice == "67":
            six_seven()
        else:
            print("Please input valid action")