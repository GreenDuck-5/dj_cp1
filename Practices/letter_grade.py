#DJ, 1st, letter grade
while True:    
    
    grade_percent = input("What is your grade percent:\n").strip()
    if grade_percent.replace(".","").isdigit():
        grade_percent = float(grade_percent)
        break
    else:
        print("Please enter a number.")


if grade_percent <= 100 and grade_percent >= 92:
    print("You have an A")
elif grade_percent <= 92 and grade_percent >= 90:
    print("You have an A-")
elif grade_percent <= 90 and grade_percent >= 87:
    print("You have an B+")
elif grade_percent <= 87 and grade_percent >= 82:
    print("You have an B")
elif grade_percent <= 82 and grade_percent >= 80:
    print("You have an B-")
elif grade_percent <= 80 and grade_percent >= 77:
    print("You have an C+")
elif grade_percent <= 77 and grade_percent >= 72:
    print("You have an C")
elif grade_percent <= 72 and grade_percent >= 70:
    print("You have an C-")
elif grade_percent <= 70 and grade_percent >= 67:
    print("You have an D+")
elif grade_percent <= 67 and grade_percent >= 64:
    print("You have an D")
elif grade_percent <= 64 and grade_percent >= 55:
    print("You have an D-")
elif grade_percent <= 55 and grade_percent >= 0:
    print("You have an F")
else:
    print("How")