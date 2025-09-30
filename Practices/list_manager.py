#DJ, 1st, List Manager
shopping_list = []
import random
import time



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
        print("ha")
        time.sleep(5)
        print("ha")
        time.sleep(5)
        print("ha")
        time.sleep(5)
    else:
        print("Please input valid action")