# DJ, 1st, Flexible Calculator
print("Welcome to the Flexible Calculator!\n\nAvailable operations: sum, average, max, min, product")
operation = input("Which operation would you like to perform?:\n")
nums = []
def nums_sum():
    print(f"Calculating sum of: {nums}")
    print(f"Result: {sum(nums)}\n")
def nums_average():
    total = 0
    for num in nums:
        total += num
    average = total / (nums(len))
    print(f"Calculating average of: {nums}")
    print(f"Result: {average}")
def nums_min():
    mins = min(nums)
    print(f"Calculating min of: {nums}")
    print(f"Result: {mins}\n")
def nums_max():
    maxs = max(nums)
    print(f"Calculating max of: {nums}")
    print(f"Result: {maxs}\n")
def nums_product():
    total = nums[0]
    for num in nums:
        total*num
    print(f"Calculating poduct of: {nums}")
    print(f"Result: {total}\n")