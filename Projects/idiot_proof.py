#DJ, 1st, Idiot Proof
name = "Clang"
first_name = input("Enter first name: ").title().strip()
last_name = input("Enter last name: ").title().strip()
full_name = (first_name,last_name)


phone_number_p_one = input("Enter the first 3 digits of your phone number: ").strip()
phone_number_p_two = input("Enter the second 3 digits of your phone number: ").strip()
phone_number_p_three = input("Enter the last 4 digits of your phone number: ").strip()
phone_number = phone_number_p_one+phone_number_p_two+phone_number_p_three



gpa = float(input("Enter GPA: ").strip())




print("Name:" , full_name)
print("Phone Number:" , phone_number)
print("GPA: " , gpa)



