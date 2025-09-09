#DJ, 1st, basic calculator
running = True

while running:
    run = input("Would you like you to run the program?: ").lower().strip()
    if run == "no":
        running = False

    else:

        number_one = int(input("Number 1: ").strip())
        number_two = int(input("Number 2: ").strip())

        addition = int((number_one + number_two))
        subtraction = int((number_one - number_two))
        multiplication = int((number_one * number_two))
        division = int((number_one / number_two))
        integer_division = int((number_one // number_two))
        modulo =  int((number_one % number_two))

        print(f"{number_one} + {number_two} = {addition}")
        print(f"{number_one} - {number_two} = {subtraction}")
        print(f"{number_one} * {number_two} = {multiplication}")
        print(f"{number_one} / {number_two} = {division}")
        print(f"{number_one} // {number_two} = {integer_division}")
        print(f"{number_one} % {number_two} = {modulo}")

name = "Clang"