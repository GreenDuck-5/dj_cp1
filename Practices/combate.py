#DJ, 1st, Combate
#importing to use time and random
import random as r
import time as t
#setting characters to false
rubber_duck = False
dragon_duck = False
cultist_duck = False
tank_duck = False
#Introducing the game 
print("This is the duck fighing game!\nYou have 4 different options for characters.")
t.sleep(1)
while True:
    #introducing the characters
    char_learn = input("1.) The Rubber Duck\n2.) The Dragon Duck\n3.) The Cultist Duck\n4.) The Tank Duck\nPlease enter number of character you would like to learn more about.\n")
    #Info dump about rubber duck
    if char_learn == "1":
        #stats
        print("This is the Rubber Duck\nIt has:\nDuck Points = 20\nMax Health = 30\nDefense = 12")
        t.sleep(5)
        while True:
            rubber_duck = input("Press 1 if you would like to be The Rubber Duck.\nPress 2 to look at more characters\n")
            #setting variable to true for later use
            if rubber_duck == "1":
                rubber_duck = True
                t.sleep(1)
            else:
                break
            break
    #info dump about dragon duck
    elif char_learn == "2":
        print("This is The Dragon Duck\nIt has:\nDuck Points = 20\nMax Health = 40\nDefense = 14")
        t.sleep(5)
        while True:
            dragon_duck = input("Press 1 if you would like to be The Dragon Duck.\nPress 2 to look at more characters\n")
            #setting varible to true to pick later
            if dragon_duck == "1":
                dragon_duck = True
                t.sleep(1)
            else:
                break
            break
    elif char_learn == "3":
    #same thing as previous 2
        print("This is The Cultist Duck\nIt has:\nDuck Points = 50\nMax Health = 20\nDefense = 10")
        t.sleep(5)
        while True:
            cultist_duck = input("Press 1 if you would like to be The Cultist Duck.\nPress 2 to look at more characters\n")
            if cultist_duck == "1":
                cultist_duck = True
                t.sleep(1)
            else:
                break
            break
    elif char_learn == "4":
        #same thing as previous 2
        print("This is The Tank Duck\nIt has:\nDuck Points = 10\nMax Health = 30\nDefense = 16")
        t.sleep(5)
        while True:
            tank_duck = input("Press 1 if you would like to be The Tank Duck.\nPress 2 to look at more characters")
            if tank_duck == "1":
                tank_duck = True
                t.sleep(1)
            else:
                break
            break
    #failsafe for stupid people
    else:
        print("Please enter valid input")
        continue
    #setting it so that if the player picks a character, combat starts
    if rubber_duck == True or dragon_duck == True or cultist_duck == True or tank_duck == True:
        break
#assigning stats based on character 
if rubber_duck == True:
    char_choice = "rubber"
    health = 30
    dp = 20#dp = Duck Points
    defense = 12
elif dragon_duck == True:
    char_choice = "dragon"
    health = 40
    dp = 20
    defense = 14
elif cultist_duck == True:
    char_choice = "cultist"
    health = 20
    dp = 50
    defense = 10
elif tank_duck == True:
    char_choice = "tank"
    health = 30
    dp = 10
    defense = 16
print("Combat time, I trust you'll figure it out.")
#setting basic enemy for now
enemy_health = 30
enemy_defense = 1
#randomly pick who starts
start = r.randint(1,2)
#setting player turn function
def player_turn():
    global dp
    global enemy_health
    global enemy_defense
    if char_choice == "rubber":
        while True:    
            user_input = input("1.) Attack\n2.) Heal\n")
            if user_input == "1":
                attack_choice = input(f"1.)Quack = 2d6+1, 3 Duck Points, -1 to hit\n2.)Bite = 1d6 Damage+2, 1 Duck Point, +0 to hit\n3.)Headbutt = 1d4 Damage, 0 Duck Points, +1 to hit\n4.)Back\n")    
                if attack_choice == "1":
                    dp -= 3
                    print("Rolling to hit...")
                    t.sleep(1)
                    print("Rolling to hit...")
                    t.sleep(1)
                    print("Rolling to hit...")
                    attack_roll = r.randint(1,20)-1
                    print(f"You rolled a {attack_roll}")
                    if attack_roll > enemy_defense:
                        print("You hit!")
                        quack_attack = r.randint(1,6)+r.randint(1,6)+1
                        print(f"You do {quack_attack} damage")
                        enemy_health -= quack_attack
                        quack_attack = 0
                        return
                    else:
                        print("You missed :(")
                        return
                elif attack_choice == "2":
                    dp -= 1
                    print("Rolling to hit...")
                    t.sleep(1)
                    print("Rolling to hit...")
                    t.sleep(1)
                    print("Rolling to hit...")
                    t.sleep(1)
                    attack_roll = r.randint(1,20)
                    print(f"You rolled a {attack_roll}")
                    if attack_roll > enemy_defense:
                        print("You hit!")
                        bite_attack = r.randint(1,6)+2
                        print(f"You did {bite_attack} damage")
                        enemy_health -= bite_attack
                        bite_attack = 0
                        return
                    else:
                        print("You missed :(")
                        return
                elif attack_choice == "3":
                    print("Rolling to hit...")
                    t.sleep(1)
                    print("Rolling to hit...")
                    t.sleep(1)
                    print("Rolling to hit...")
                    t.sleep(1)
                    attack_roll = r.randint(1,20)+1
                    print(f"You rolled a {attack_roll}")
                    if attack_roll > enemy_defense:
                        print("You hit!")
                        headbutt_attack = r.randint(1,4)
                        print(f"You do {headbutt_attack} damage")
                        enemy_health -= headbutt_attack
                        headbutt_attack = 0
                        return
                    else:
                        print("You missed :(")
                        return
                else:
                    continue
            elif user_input == "2":
                heal_choice = input("1.)Max Heal, 5 Duck Points\n2.)Small Heal, +10 HP, 3 Duck Points\n3.)Back")
                if heal_choice == "1":
                    dp -= 5
                    health = 30
                    return
                elif heal_choice == "2":
                    dp -= 3
                    health += 10
                    if health > 30:
                        health = 30
                        return
                    else:
                        return
                elif heal_choice == "3":
                    continue
    if char_choice == "dragon":
        while True:
            user_input = input("1.) Attack\n2.) Heal\n")
            if user_input == "1":
                attack_choice = input(f"1.)Dragon Breath = 3d6, 5 Duck Points, -1 to hit\n2.)Tail Whip = 1d6 Damage+2, 1 Duck Point\n3.)Coin Throw = 2d4 Damage, 0 Duck Points, +5 to hit\n4.)Back\n")
                if attack_choice == "1":
                    dp -= 5
                    print("Rolling to hit...")
                    t.sleep(1)
                    print("Rolling to hit...")
                    t.sleep(1)
                    print("Rolling to hit...")
                    attack_roll = r.randint(1,20)-1
                    print(f"You rolled a {attack_roll}")
                    if attack_roll > enemy_defense:
                        print("You hit!")
                        breath_attack = r.randint(1,6)+r.randint(1,6)+r.randint(1,6)
                        print(f"You do {breath_attack} damage")
                        enemy_health -= breath_attack
                        breath_attack = 0
                        return
                    else:
                        print("You missed :(")
                        return
                if attack_choice == "2":
                    dp -= 1
                    print("Rolling to hit...")
                    t.sleep(1)
                    print("Rolling to hit...")
                    t.sleep(1)
                    print("Rolling to hit...")
                    attack_roll = r.randint(1,20)
                    print(f"You rolled a {attack_roll}")
                    if attack_roll > enemy_defense:
                        print("You hit!")
                        tail_attack = r.randint(1,6)+2
                        print(f"You do {tail_attack} damage")
                        enemy_health -= tail_attack
                        tail_attack = 0
                        return
                    else:
                        print("You missed :(")
                        return
                if attack_choice == "3":
                    print("Rolling to hit...")
                    t.sleep(1)
                    print("Rolling to hit...")
                    t.sleep(1)
                    print("Rolling to hit...")
                    attack_roll = r.randint(1,20)+5
                    print(f"You rolled a {attack_roll}")
                    if attack_roll > enemy_defense:
                        print("You hit!")
                        coin_attack = r.randint(1,4)+r.randint(1,4)
                        print(f"You do {coin_attack} damage")
                        enemy_health -= coin_attack
                        coin_attack = 0
                        return
                    else:
                        print("You missed :(")
                        return
                else:
                    continue
            elif user_input == "2":
                heal_choice = input("1.)Max Heal, 5 Duck Points\n2.)Small Heal, +15 HP, 3 Duck Points\n3.)Back")
                if heal_choice == "1":
                    dp -= 5
                    health = 40
                    return
                elif heal_choice == "2":
                    dp -= 4
                    health += 10
                    if health > 40:
                        health = 40
                        return
                    else:
                        return
                elif heal_choice == "3":
                    continue
def enemy_turn():
    print("enemy")
if start == 1:
    turn_count = 0
    while True:
        player_turn()
        turn_count += 1
        print(f"Turn {turn_count}")
        t.sleep(1)
        enemy_turn()
        turn_count += 1
        print(f"Turn {turn_count}")
        t.sleep(1)
elif start == 2:
    turn_count = 0
    while True:
        enemy_turn()
        turn_count += 1
        print(f"Turn {turn_count}")
        t.sleep(1)
        player_turn()
        turn_count += 1
        print(f"Turn {turn_count}")
        t.sleep(1)