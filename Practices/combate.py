#DJ, 1st, Combate
import random as r
name = input("Welcome to training! First I need to know some things about you!\nEnter name:\n").title().strip()
while True:
    user_class = input("Enter class:\n1.) Fighter\n2.) Mage\n3.) Rogue")
    if user_class == "1": 
        user_class = "Fighter"
        health = 30
        defense = 14
        attack = r.randint(1,20)+3
        damage = r.randint(1,8)+4
        print(f"You are a {user_class}\nYou have {health} health\nYou have {defense} defense\nYou have an attack modifier of +3\nYour damage is D8+4")
        break
    elif user_class == "2": 
        user_class = "Mage"
        health = 10
        defense = 10
        attack = r.randint(1,20)+1
        damage = r.randint(1,4)+1
        print(f"You are a {user_class}\nYou have {health} health\nYou have {defense} defense\nYou have an attack modifier of +1\nYour damage is D4+1")
        break
    elif user_class == "3": 
        user_class = "Rogue"
        health = 25
        defense = 15
        attack = r.randint(1,20)+5
        damage = r.randint(1,10)+5
        print(f"You are a {user_class}\nYou have {health} health\nYou have {defense} defense\nYou have an attack modifier of +5\nYour damage is D10+5")
        break
    else:
        print("Please enter valid input.")
        continue
print("situation")
print("combat instructions")