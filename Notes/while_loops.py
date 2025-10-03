#DJ. 1st, While Loops
import random
#What is a while loop?
# A loop over as much code as you want it to


#How are while loops different from for loops?
# while loops gpo on forever where as a for loop goes for a predetermined amount of time


#Why do we need a counter in a while loop?
# It would go on forever if you didn't


#What is a break statement?
# A statement that ends the loops


#How do we use an else statement with a while loop?
goose = random.randint(1,20)
count = 0
while count != goose:
    count += 1
    if count == goose: 
        break
    else:
        print("duck")


else:
    print("The code is done")
    



#Does a break statement let the else statement happen?
# No


#What does continue do?
# Skips to a new iteration of the loops


for num in range(1,21):
    print(num)

num = 1
while num <= 20:
    print(num)
    num += 1