#DJ. 1st, Strings Notes

#What is a string?
#A collection of symbols that are held together, in python it is “quotation marks”

#Why are they called strings?
#Because they are loosely held together characters.

#How do I make a string?
print("Everything inside the quotation marks is a string")
print('This also works')

scentence = "The quick brown fox jumps over the lazy dog!"
first_name = "Clang"
month = 'September'
book = "The Return of the King"
food = "chocolate"


#Why do I make a string?
#So that it doesn't think that it needs to run it. It's for the user. It's just info.

#Does it matter if I use single or double quotes?
#No. But stay consistent.

#How do we get the length of our string?
length = len(scentence)

#What is an escape character?
print("\"Inkheart\" is the best book ever!")
#Escape charcter is backslash
#Tells computer to ignore whats happening next
print("\"Inkheart\" is the best book\never!")
#\n makes a new line
print("\tInkheart is the best book ever!")
#\t tabs in the scentence

#What does it mean to concatenate a string?
#put 2 strings together
#only works with strings

#How do you concatenate a string?
scentence + book
last_name = "LaRose"
full_name = first_name + " " + last_name
print(full_name)
#Does not put a space inbetween

#How do I slice a string?
print(last_name[:3])
#Starting index to ending index
print(last_name[2:])
#If blank takes last/first number. depends on which side its on

print(scentence[10:15])


#What is index?
#Location of each charater in the string

#How do we count indexes?

#Each character is a number starting form 0