#DJ, 1st, formatting strings notes


# How do I write the format method?

name = "Clang"
age = 21
money = 100025.1
percent = .67


print("Hello {}. you are {:,}. That is so old! You have ${:.2f} you mast be rich! Random percent is {:%}.".format(name, age, money, percent))




# What does the format method allow me to change about my outputs?
# (:,) commas where they should be
# (:E) scientific notation
# (:b) binary
# {:. NUmber of decimal places then f}



# Describe why it is important to format your outputs.
#To make it readable and add context






# What is an f-string?

#A modern way to format your outputs




# How do I create an f-string?

print(f"Hello {name}. you are {age:,}. That is so old! You have ${money:.2f} you mast be rich! Random percent is {percent:%}.")




# What do f-strings allow me to do?

#Form outputs in an easy and reliable way


