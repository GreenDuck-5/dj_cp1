#DJ, 1st, Password strength checker
#set point value so we can track the score
points = 0
#ask user for password
password = input("Enter a password:\n")
#loops to check if password contains lowercase
for i in password:
    if i.islower():
        #adds point if contains a lowercase
        points += 1
        #ends loop
        break
#loops check if password contains uppercase
for i in password:
    if i.isupper():
        #adds one point if contains a uppercase
        points += 1
        #ends loop
        break
# make a list of special characters
special = "!@#$%^&*()_+-=[]{}|;:,.<>?"
# repeatedly looping to check if the password shares a character with the list of special characters
for i in password:
    if i in special:
        # adds 1 point if cotains a number
        points += 1
        #ends loop
        break
# loops to check if it contains a number
for i in password:
    if i.isdigit():
        #adds 1 point if it cotains a number
        points += 1
        #ends loop
        break
# checks if password is longer than 8 digits
if len(password) >= 8:
    #adds point if longer than 8 digits
    points += 1
print(points)
#tells user how strog their password is base off of their point score
if points == 5:
    print("Very Strong")
elif points == 4:
    print("Stong")
elif points == 3:
    print("Medium")
elif points == 2:
    print("Weak")
elif points == 1:
    print("Poor")
else:
    print("No.")