# DJ, 1st, Mapping Notes
numbers = [543,52356,367,54,7,456,34,53,5,523,3]



"""new_numbers = []

for num in numbers: new_numbers.append(num/3)
print(new_numbers)"""

def divide(num):
    return num/3

new_nums = map(lambda num: num/3, numbers)
print(list(new_nums))
for num in new_nums:
    print(num)


#What information does map need?
# a function and a list or tuple

#What does map return?
# one thing that is after the colon

#What is a lambda function
# single line fuction, but can only return one thing


#How does using a lambda function and the map function shorten your code?
# makes it line
