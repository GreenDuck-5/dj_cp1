# DJ, 1st, Random Numbers


# Can computers really generate a "random" number?
# No



# What is a python library?
# A whole collection of prebuilt functions that we can call and bring into our code


import random

print(f"This is a random number from 1 - 0: {random.random()}")
print(f"This is a random number from 1 - 0: {random.randint(1,20)}")



# What are functions?
# A collection of code made to do a task, an algoritham




# How do you call a function?
#saying its name and giving it parentheses




# What have we already learned that is similar to a function?
#string methods
name = input("What is your character name?\n").strip().title()


# What function to I call to get a random number?
random.randint(6,7)




# What are arguments?
#Numbers we put inside our function



# What arguments are needed to generate a random number?




#D&D Nerd stuff
#Generate stat options
stat_one = random.randint(1,10) + random.randint(1,10)
stat_two = random.randint(1,10) + random.randint(1,10)
stat_three = random.randint(1,10) + random.randint(1,10)
stat_four = random.randint(1,10) + random.randint(1,10)
stat_five = random.randint(1,10) + random.randint(1,10)
stat_six = random.randint(1,10) + random.randint(1,10)
stat_seven = random.randint(1,10) + random.randint(1,10)

#Telling user stat choices
print(f"Your stat options are: {stat_one}, {stat_two}, {stat_three}, {stat_four}, {stat_five}, {stat_six}, {stat_seven}")

#set stats
strength = int(input("Which stat do you want as your stength: \n")) + 2








































