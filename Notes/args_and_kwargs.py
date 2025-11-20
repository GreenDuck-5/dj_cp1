# DJ, 1st, *args and **kwargs notes
def hello(name, age):
    return f"hello {name}"

print(hello(age = 23, name = "Xaveir"))


#What are positional arguments?
# arguments defined by where they are in the function


#What are keyword arguments?
# specifying which parameter regardless of position


#How do you set a default parameter value?
# in the function definition set the parameter, set using *args and **kwargs


#How do alter a function to take in an unknown number of arguments?
# they will ne stored with *(for list) or **(for dictionary)

def summary(**story):
    sum = ""
    if "name" in story.keys():
        sum += f"{story['name']} is the main character of this story"
    if "place" in story.keys():
        sum += f"The story takes place in {story['place']}."
    if "conflict" in story.keys():
        sum +=f"The problem is {story['conflict']}."
    
    return sum

print(summary(name = "Luke Skywalker", place = "A galaxy far far away"))
print(summary(name = "Harry Potter", conflict = "Evil wizard wants to kill him"))