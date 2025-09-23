#DJ, 1st, Conditionals notes
running = True

import random
import time

while True:


    player_hp = 20
    player_attack = 5
    player_damage = 5
    player_defense = 5


    clang_hp = 15
    clang_attack = 3
    clang_damage = 10
    clang_defense = 2

    hit_roll = random.randint(1,20) 
    damage_roll = random.randint(1,8) + player_damage

    if hit_roll == 20:
        print("You got a crit! That means you get to roll for damage twice")
        damage_roll = random.randint(1,8) +  random.randint(1,8) + player_damage
        print(f"You did {damage_roll} damage")
        clang_hp -= (damage_roll-clang_defense)
    
    elif hit_roll == 1:
        print("You rolled a critical failure! Now the monster gets to attack you!")
        damage_roll = random.randint(1,12) + clang_damage
        player_hp -= (damage_roll - player_defense)
        print(f"Your hp is now {player_hp}")

    elif hit_roll + player_attack >= 12:
        print("You hit! Roll for damage!")
        damage_roll = random.randint(1,8) + player_damage
        if damage_roll > clang_defense:
            print(f"You did {damage_roll-clang_defense} damage.")
            clang_hp -= (damage_roll-clang_defense)
        else:
            print("You did no damage.")

    else:
        print("You missed.")



#What are conditionals in python? 
#uses boolean to pick what will run


#How do we write an if statement? 
# if: if this is true below will run
    #what you want to run


#How do we write conditions?
    if clang_hp <= 0:
        print("You win")
        break
    elif player_hp <= 0:
        print("You lose.")
        break
    else:
        print("Round 2")
        time.sleep(3)

        


#Why does the code need to be indented after the if?
# So the computer knows what to run if that condition is true


#Why do we want to have else statements?
#Backup


#How many else if statements can you create? 
#As many as you want


#Why does the order of your statements matter in a conditional?
#Because if one condition is filled it skips the rest


#How do we use boolean instead of boolean statements? 
#True


