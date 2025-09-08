#DJ, 1st, String Methods Notes

subject = "Computer Programming 1!"

print(subject.upper())

print(subject)

name = "Clang"





# Stupid/Idiot Proofing Inputs
color = input("What is your favorite color?").strip().lower()
#lower() makes it all lowercase
#upper() makes it all uppercase
#capitalize() capitalizes the first letter of the first word
#title() capitalizes the first letter of every word
full_name = input("What is you full name?").strip().title()
print("That is cool. " + full_name + " I like " + color + " too!")




#f-strings
print(f"That is cool {full_name}. I like {color} too")


pi = 3.14159
#print(f"We all know pi is equal to {pi:.3f}")
#print(pi.isdecimal())

sentence = "The quick brown fox jumps over the lazy dog."
word = "fox"
print(sentence.find(word))
start = (sentence.index(word))
length = len(word)
print(sentence[start:start+length])
print(sentence.replace(word,"swims"))
print(sentence)


#What is a method?
#Allows you to alter a string in a specific way that doesn't reset the variable





#How do I write a method?
#The method you are using()





#What methods can I use to change the formatting of my string?
#Use an f string (f"sting is in here")




#What methods allow me to search the contents of my string?
#find() and .rfind()





#What methods allow me to change the contents of my string?

#replace(variable with the word in the sentence in it, "what is being replace with")




#Why is it important to know what type of output a method will give me?
#So you can build the code around that output


