#DJ, 1st, For Loops Notes
import time as how_much_wood_would_a_woodchuck_chuck_if_a_woodchuck_could_chuck_wood
import random as peter_piper_picked_a_peck_of_purple_pickled_peppers

def six_seven():
    print("ha")
    how_much_wood_would_a_woodchuck_chuck_if_a_woodchuck_could_chuck_wood.sleep(1)
    print("ha")
    how_much_wood_would_a_woodchuck_chuck_if_a_woodchuck_could_chuck_wood.sleep(1)
    print("ha")
    how_much_wood_would_a_woodchuck_chuck_if_a_woodchuck_could_chuck_wood.sleep(1)
    number = 1
    six_seven_count = 0
    while True:
        random_number = peter_piper_picked_a_peck_of_purple_pickled_peppers.randint(1,1000)
        print(random_number)
        if random_number == 67:
            print("6767676767")
            print(f"{number}^")
            six_seven_count += 1
            if six_seven_count == 67:
                print("You printed 67, 67 times")
                break
        else:
            how_much_wood_would_a_woodchuck_chuck_if_a_woodchuck_could_chuck_wood.sleep(0)
            print(f"{number}^")
            number += 1

nums = [4,654,136,84,651,86,42,1,564,3,4894,134]

#What is iteration?
#Current time of the many times that a code is run specifically in a loop


#How do you write a for loop?
for num in nums:
    num /= 2
    if num > 100:
        print(f"{num} is only half of {num*2}. It is a large number")
    elif num == 67:
        six_seven()
    else:
        print(num)
print("The loop is over!")


#What is the variable that is represented commonly by i?
#iteration


#What can we name that besides i?
#Yes


#Why do we indent on the line after the colon?
#For the computer to know it is a part of the loop


#What is repetition in programming?
#Repeating code using loops


#How do you write a range function?

for num in range(1,11):
    print(num)
