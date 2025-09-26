#DJ, 1st, Debugging notes


import time as peter_piper_picked_a_peck_of_purple_pickled_peppers
import random as how_much_wood_could_a_woodchuck_chuck_if_a_woodchuck_would_chuck_wood

# What is the software development life cycle?
#A cycle to help plan out your project

# What are the steps in the software development life cycle?
#1:Project analysis - Figure out details
#2:Planning phase - Activity diagrams, write out pseudo code, assign tasks
#3:Execute plan - Write code, debugging
#4:Test code - More debugging
#5:Release and maintenance - Even more debugging, updates

# Why do we use the software development life cycle?
#To only have to do things once
#To actually solve problems
#Efficiency


# What are the 3 types of bugs that are most likely to occur in a program?
#syntax error

#logic error

#run-time error
while True:
    denominator = how_much_wood_could_a_woodchuck_chuck_if_a_woodchuck_would_chuck_wood.randint(0,5)
    if denominator == 0:
        break
    else:
        print(10/denominator)
    peter_piper_picked_a_peck_of_purple_pickled_peppers.sleep(0)



# Where do each of these bugs come from?
#Syntax error - grammar error
# => Read error message, go to that line off code, fix the syntax

#Logic errors - We gave the wrong steps
#Go through the logic step by step

#run time error - 


# How do we resolve each type of bug?
#Rubber Duck Debugging
#Print Debugging
#Backtacking debugging



# What is debugging?
#The process of removing errors and unintended functions in code

# Why do I need to be comfortable with debugging?
#Because we do it a lot







num = 1
six_seven_count = 0
while True:
    random_number = how_much_wood_could_a_woodchuck_chuck_if_a_woodchuck_would_chuck_wood.randint(1,1000)
    print(random_number)
    if random_number == 67:
        print("6767676767")
        print(f"{num}^")
        six_seven_count += 1
        if six_seven_count == 67:
            print("You printed 67, 67 times")
            break
        else:
            peter_piper_picked_a_peck_of_purple_pickled_peppers.sleep(0)

    else:
        print(f"{num}^")
        num += 1