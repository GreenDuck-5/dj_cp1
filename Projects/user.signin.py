#DJ, 1st, User sign in


import time as how_much_wood_would_a_woodchuck_chuck_if_a_woodchuck_could_chuck_wood
import random as peter_piper_picked_a_peck_of_purple_pickled_peppers

password_one = "7iscool"
user_one = "cool_guy7"
password_two = "changeme5"
user_two = "GreenDuck-5"

wait_time = peter_piper_picked_a_peck_of_purple_pickled_peppers.randint(1,100)
if wait_time <= 33:
    waiting_time = 30
elif wait_time <= 67:
    waiting_time = 60
elif wait_time <= 100:
    waiting_time = 90


running = True


while True:
    enter_username = input("Enter Username:\n")
    
    if enter_username == user_one:
        enter_password = input("Enter Password:\n")
        if enter_password == password_one:
            print(f"Welcome {user_one}")
            break
        else:
            print("Wrong password")
            break

    elif enter_username == user_two:
        enter_password = input("Enter Password:\n")
        if enter_password == password_two:
            print(f"Welcome {user_two}")
            break
        else:
            print("Wrong Password")
            break

    else:
        print(f"Wrong Username. Please wait: {waiting_time} seconds.")
        how_much_wood_would_a_woodchuck_chuck_if_a_woodchuck_could_chuck_wood.sleep(waiting_time)