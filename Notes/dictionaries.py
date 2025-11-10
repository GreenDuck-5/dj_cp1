#DJ, 1st, Dictionaries Notes
import random as r

#What are dictionaries?
# Saving variables in, Key: Value, pairs

#How do dictionaries simply variables in a project?
# keeps it condensed and in one place

#What are key and value pairs?
# A key is the name for the value that you can access

#How do you build a dictionary?
person = {
    #key:value,
    "name": "Xavier",
    "age": 22,
    "job": "Mavrick",
    "sibling": ["Alex", "Katie", "Andrew", "Vienna", "Tia", "Treyson", "Jake"],
    "random": r.randint(1,5),
    "other": input("...:\n")
}

print(f"\n\n\n\n{person['random']}")
print(f"{person['other']}")
#How do you call a value from a dictionary?
# dicitonary_name[key]

#How do you get each of the keys from a dictionary?
# dicitonary(keys)

#How do you update a value in a dictionary?
person["age"] += 1

#Can you add new key and value pairs to a dictionary during runtime?
# dictionary_name[new_key] = new_value
