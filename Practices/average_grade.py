#DJ, 1st, Average Grade

cs_grade = float(input("What is your grade percentage in CS 1400 A?"))
math_grade = float(input("What is your grade percentage in Secondary Math 1A Honors?"))
wc_grade = float(input("What is your grade percentage in World Civilizations?"))
advisory_grade = float(input("What is your grade percentage in 5th Advisory 9?"))
english_grade = float(input("What is your grade percentage in English 9A Honors?"))
art_grade = float(input("What is your grade percentage in Drawing 1 CE?"))
bio_grade = float(input("What is your grade percentage in Biology?"))

grade_total = float(cs_grade+math_grade+wc_grade+advisory_grade+english_grade+art_grade+bio_grade)
not_average_grade = (grade_total /7)
average_grade = round(not_average_grade,2)

print("Your average grade is",average_grade)

name = "Clang"
