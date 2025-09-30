#DJ, 1st, Lists notes
import random as peter_piper_picked_a_peck_of_purple_pickled_peppers



random_color = peter_piper_picked_a_peck_of_purple_pickled_peppers.randint(0,4)


colors = ["Green", "Blue", "Yellow", "Purple", "Red"]

print(colors[random_color])



#What are lists? 
# complex data types used to store data



#How do you find the length of a list?
print(f"this list is {len(colors)} colors long")



#What data types can be put inside of lists?
# all



#How do you get one item from a list?
print(colors[0])



#How do you replace a value in a list?

colors[4] = "Pink"
colors[3:4] = ["Brown","Maroon"]


#What does append do?
colors.append("Orange")
# Adds a item to the list



#What does insert do?
colors.insert(2,"Puce")
# Adds an item where you want it to



#What does extend do?
#colors.extend([67,68])
# Adds items at the end of the list


#How do you remove an item from a list?

colors.pop()
colors.pop(0)
colors.remove("Maroon")
print(colors)
#colors.clear()
print(colors)


board = [[1,2,3],
         [4,5,6],
         [7,8,9]
         ] 

fruit = ("Apple", "Orange", "Pineapple") #tuple, ordered, not changeable


veggies = {"Spinach", "Kale", "Broccoli", "Carrot"} #set. unordered, changeable 