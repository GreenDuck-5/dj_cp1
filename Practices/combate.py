#DJ, 1st, Combate
import random as r
import time as t
print("This is the duck fighing game!\nYou have 4 different options for characters.")
t.sleep(1)
while True:
    char_learn = input("1.) The Rubber Duck\n2.) The Dragon Duck\n3.) The Cultist Duck\n4.) The Tank Duck\nPlease enter number of character you would like to learn more about.\n")
    if char_learn == "1":
        print("This is the Rubber Duck\nIt has:\nDuck Points = 20\nMax Health = 30\nDefense = 3\nMax Healing Spell = +30 Heal\nSmall Healing Spell = +10 Heal\nQuack = 5 Damage\nBite = 3 Damage\nHeadbutt = 1 Damage")
        t.sleep(5)
        while True:
            rubber_duck = input("Press 1 if you would like to be The Rubber Duck.\nPress 2 for more details\nPress 3 to go back to menu\n")
            if rubber_duck == "1":
                rubber_duck = True
            elif rubber_duck == "2":
                print("Max Healing Spell costs 10 Duck Points\nSmall Healing Spell costs 5 Duck Points\nQuack costs 3 Duck Points\nBite costs 1 Duck Point\nHeadbutt costs 0 Duck Points")
                t.sleep(5)
            else:
                break
    elif char_learn == "2":
        print("This is The Dragon Duck\n It has:\nDuck Points = 20\nMax Health = 40\nDefense = 5\nMax Healing Spell = +30 Heal\nFire Breath = 10 Damage\nDragon Flap = 5 Damage\nGold Throw = 5 Damage")
        t.sleep(5)
        while True:
            dragon_duck = input("Press 1 if you would like to be The Dragon Duck.\nPress 2 for more details\nPress 3 to go back to menu\n")
            if dragon_duck == "1":
                dragon_duck = True
            elif dragon_duck == "2":
                print("Max Healing Spell costs 10 Duck Points\nFire breath costs 5 Duck Points\nDragon Flap costs 3 Duck Points\nGold Throw costs 1 Duck Point")
                t.sleep(5)
            else:
                break
    elif char_learn == "3":
        print("This is The Cultist Duck\n It has:\nDuck Points = 50\nMax Health = 20\nDefense = 1\nMax Healing Spell = +20 Heal\nStaff Slap = 3 Damage\nShadow Quack = 10 Damage\nGod Summon = 10 Damage")
        t.sleep(5)
        while True:
            cultist_duck = input("Press 1 if you would like to be The Cultist Duck.\nPress 2 for more details\nPress 3 to go back to menu\n")
            if cultist_duck == "1":
                cultist_duck = True
            elif cultist_duck == "2":
                print("Max Healing Spell costs 10 Duck Points\nStaff Slap costs 1 Duck Point\nShadow Quack costs 7 Duck Points\nGod Summon costs 10 health or 50 Duck Points")
                t.sleep(5)
    elif char_learn == "4":
        print("This is The Tank Duck\n It has:\nDuck Points = 10\nMax Health = 30\nDefense = 10\nMax Healing Spell = +25 Heal\nCannon Shot = 5 Damage\nRun Over = 10 Damage\nSelf Destruct = 100 Damage")
        t.sleep(5)
        while True:
            tank_duck = input("Press 1 if you would like to be The Tank Duck.\nPress 2 for more details\nPress 3 to go back to menu\n")
            if tank_duck == "1":
                tank_duck = True
            elif tank_duck == "2":
                print("Max Healing Spell costs 5 Duck Points\nCannon Shot costs 1 Duck Point\nRun Over costs 2 Duck Points\nSlef Desrtuct costs 29 health")
                t.sleep(5)
    else:
        print("Please print valid input")
        continue