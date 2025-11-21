# DJ, 1st, Factorial Calculator
#define function multiply all lower(value:)
def factorial(value):
    #value = int(value)
    value = int(value)
    #for loop x in range(value):
    for x in range(1, value):
        #iter = value-x
        iterator = value - x
        #fact = iterator
        factor = iterator
    #return factorial
    return factor
#print("Welcome to the factorial calculator")
print("Welcome to the factorial calculator")
#loop until user is done(while True):
while True:
    #prevalue = input("please enter a value here:_")
    pre_value = input("Please enter a value here:\n")
    
    #if prevalue can be turned into a integer and doesnt contain a ".":
    if pre_value.isdigit() and "." not in pre_value:
        #print(f"The factorial of {prevalue} is {multiply all lower(prevalue)}")
        print(f"The factorial of {pre_value} is {factorial(pre_value)}")
    #else:
    else:
        #print("you have inputted an invalid value please enter an integer")
        print("You have inputted an invalid value. Please enter an integer.")
