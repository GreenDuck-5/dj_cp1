#DJ, 1st, Menu

# menu items
menu = {
    # mains
        #item:price
    "mains" : {
        "Soft Taco": 2.18,
        "Crunchy Taco": 2.18,
        "Soft Taco Supreme": 3.40,
        "Crunchy Taco Supreme": 3.40,
        "Nacho Cheese Doritos Locos Taco": 3.04,
        "Nacho Cheese Doritos Locos Taco Supreme": 4.01,
        "Bean Burrito": 2.74,
        "Beefy 5-Layer Burrito": 3.94,
        "Burrito Supreme": 5.14,
        "Grilled Cheese Burrito": 5.48,
        "Cheese Quesadilla": 5.50,
        "Steak Quesadilla": 5.98,
        "Chicken Quesadilla": 5.98,
        "Power Menu Bowl": 8.62,
        "Power Menu Bowl Veggie": 8.62,
    },
    # drinks
        #item:price
    "drinks" : {
        "Pepsi": 2.39,
        "Cherry Pepsi": 2.39,
        "Mountain Dew": 2.39,
        "Mountain Dew Zero": 2.39,
        "Mountain Dew Baja Blast": 2.39,
    },
    # sides
        #item:price
    "sides" : {
        "Large Nacho Fries": 3.19,
        "Nacho Fries": 2.29,
        "Cheesy Fiesta Potatoes": 2.59,
        "Chips and Guacamole": 3.39,
        "Black Beans and Rice": 2.69,
    },
    # desserts
        #item:price
    "dessert" : {
        "Cinnamon Twists": 1.29,
        "Cinnabon Delights 12 Pack": 7.19,
        "Milk Bar Birthday Cake Churros (2 Pack)": 2.99,
        "Baja Blast Pie": 10.92
    }
}

#setting user order
user_order = {}

def main_order(user_order,menu):
    #ask user what main they want
        #Loop through the mains, listing them all for user
    item_number = 1
    print("What whould you like for your main?")
    for item, price in menu["mains"].items():
        print(f"{item_number}.) {item} : ${price}")
        item_number += 1
    #let them pick one, add to list of user order
    while True:
        while True:
            user_main = input("Please pick one:\n")
            if user_main.isdigit():
                break
        if user_main == "1":
            user_order["Soft Taco"] = 2.18
        elif user_main == "2":
            user_order["Crunchy Taco"] = 2.18
        elif user_main == "3":
            user_order["Soft Taco Supreme"] = 3.40
        elif user_main == "4":
            user_order["Crunchy Taco Supreme"] = 3.40
        elif user_main == "5":
            user_order["Nacho Cheese Doritos Locos Taco"] = 3.04
        elif user_main == "6":
            user_order["Nacho Cheese Doritos Locos Taco Supreme"] = 4.01
        elif user_main == "7":
            user_order["Bean Burrito"] = 2.74
        elif user_main == "8":
            user_order["Beefy 5-Layer Burrito"] = 3.94
        elif user_main == "9":
            user_order["Burrito Supreme"] = 5.14
        elif user_main == "10":
            user_order["Grilled Cheese Burrito"] = 5.48
        elif user_main == "11":
            user_order["Cheese Quesadilla"] = 5.50
        elif user_main == "12":
            user_order["Steak Quesadilla"] = 5.98
        elif user_main == "13":
            user_order["Chicken Quesadilla"] = 5.98
        elif user_main == "14":
            user_order["Power Menu Bowl"] = 8.62
        elif user_main == "15":
            user_order["Power Menu Bowl Veggie"] = 8.62
        else:
            continue
        break

def drink_order(user_order,menu):
    #ask user what drink they want
    item_number = 1
    print("What whould you like for your drink?")
        #Loop through the drinks, listing them all for user
    for item, price in menu["drinks"].items():
        print(f"{item_number}.) {item} : ${price}")
        item_number += 1
    #let them pick one, add to list of user order
    while True:
        while True:
            user_drink = input("Please pick one:\n")
            if user_drink.isdigit():
                break
        if user_drink == "1":
            user_order["Pepsi"] = 2.39
        elif user_drink == "2":
            user_order["Cherry Pepsi"] = 2.39
        elif user_drink == "3":
            user_order["Mountain Dew"] = 2.39
        elif user_drink == "4":
            user_order["Mountain Dew Zero"] = 2.39
        elif user_drink == "5":
            user_order["Mountain Dew Baja Blast"] = 2.39
        else:
            continue
        break

def side_order(user_order,menu):
    #ask user what sides(2) they want
    item_number = 1
    print("What whould you like for your first side?")
        #Loop through the sides, listing them all for user
    for item, price in menu["sides"].items():
        print(f"{item_number}.) {item} : ${price}")
        item_number += 1
    #let them pick two, add to list of user order
    while True:
        while True:
            user_side_one = input("Please pick one:\n")
            if user_side_one.isdigit():
                break
        if user_side_one == "1":
            user_order["Large Nacho Fries"] = 3.19
        elif user_side_one == "2":
            user_order["Nacho Fries"] = 2.29
        elif user_side_one == "3":
            user_order["Cheesy Fiesta Potatoes"] = 2.59
        elif user_side_one == "4":
            user_order["Chips and Guacamole"] = 3.39
        elif user_side_one == "5":
            user_order["Black Beans and Rice"] = 2.69
        else:
            continue
        break
    #ask user what sides(2) they want
    item_number = 1
    print("What whould you like for your first side?")
        #Loop through the sides, listing them all for user
    for item, price in menu["sides"].items():
        print(f"{item_number}.) {item} : ${price}")
        item_number += 1
    #let them pick two, add to list of user order
    while True:
        while True:
            user_side_two = input("Please pick one:\n")
            if user_side_two.isdigit():
                break
        if user_side_two == "1":
            user_order["Large Nacho Fries"] = 3.19
        elif user_side_two == "2":
            user_order["Nacho Fries"] = 2.29
        elif user_side_two == "3":
            user_order["Cheesy Fiesta Potatoes"] = 2.59
        elif user_side_two == "4":
            user_order["Chips and Guacamole"] = 3.39
        elif user_side_two == "5":
            user_order["Black Beans and Rice"] = 2.69
        else:
            continue
        break

#ask user what dessert they want
    #Loop through the dessert, listing them all for user
#let them pick one, add to list of user order

#list the users order, let them pick whether correct or not
    # if not correct, restart at the beginning
    # if correct, give them the bill



#other ideas
    #taxes are 4.55 percent
    #maybe make it a rougelike where they have to eat everyday, and the only way to make money is gambling
    #make it so that the player can run the resturant, people are buying and the player has to restock
    #have the ability to invest in the resturant
    #add tip option
    #add round up for the hospitalized kids
    #add different menus for different times of day