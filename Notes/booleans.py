#DJ, 1st, Booleans Notes


import time

import datetime as date

current_time = time.time()
readable_time = time.ctime(current_time)
new_current_time = date.datetime.now()
hour = new_current_time.strftime("%H")
# minutes = %M
# weekday = %A, %a
# day = %d
# month = %B, %b
# month num = %m
# year = %Y, %y
# seconds = %S



print(f"Current time in seconds since January 1. 1970 (epoch): {current_time}")
print(f"Current time from datetime: {new_current_time}")
print(f"Today is {readable_time}")
print(f"The hour is: {hour}")

print(f"The hour is saved as an integer: {isinstance(hour, int)}")
print(f"The hour is saved as an float: {isinstance(hour, float)}")
print(f"The hour is saved as an string: {isinstance(hour, str)}")

print(f"Has a value: {bool(0)}")




#What can a Boolean hold? (i.e. what is a Boolean?)
True
False



#What are Booleans normally used for?
#While loops and conditionals




#What does bool() let you do?
#Converts datatype to boolean


#What values are considered True? 
# True 1




#What values are considered False?
#False 0



#What are some python built-in functions that return a Boolean value?(Try and find 1 more than the example you are given!)
#Conditionals



#What are the simple data types?
# Integers, floats, strings, booleans



#What would you use each data type for?

#Strings = text that is not true of false
#Integers = math
#Floats = more complex math
#Booleans = while loops and conditionals