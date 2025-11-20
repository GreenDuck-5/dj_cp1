# DJ, 1st, Flexible Calculator
nums = []
def nums_sum(*nums):
    print(f"Calculating sum of: {nums}")
    print(f"Result: {sum(nums)}\n")
def nums_average(*nums):
    total = 0
    for num in nums:
        total += num
    average = total / (nums(len))
    print(f"Calculating average of: {nums}")
    print(f"Result: {average}")
def nums_min(*nums):
    mins = min(nums)
    print(f"Calculating min of: {nums}")
    print(f"Result: {mins}\n")
def nums_max(*nums):
    maxs = max(nums)
    print(f"Calculating max of: {nums}")
    print(f"Result: {maxs}\n")
def nums_product(*nums):
    total = 1
    for num in nums:
        total*num
    print(f"Calculating poduct of: {nums}")
    print(f"Result: {total}\n")
while True:
    print("Enter a number (or type 'done' to finish)")
    while True:
        num = input("Number: ")
        if num.isdigit == False and num != "done":
            print("Please enter a valid number or 'done' to finish.")
            continue
        elif num == "done":
            break
        else:
            nums.append(num)

    print("Welcome to the Flexible Calculator!\n\nAvailable operations: sum, average, max, min, product")
    operation = input("Which operation would you like to perform?:\n")

    if operation in ["sum", "average", "max", "min", "product"]:
        while True:
            if operation == "sum":
                nums_sum(*nums)
                break
            elif operation == "average":
                nums_average(*nums)
                break
            elif operation == "max":
                nums_max(*nums)
                break
            elif operation == "min":
                nums_min(*nums)
                break
            elif operation == "product":
                nums_product(*nums)
                break
            else:
                print("Please enter valid input:")
                break
        if operation in ["sum", "average", "max", "min", "product"]:
            break
        