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
        "Power Menu Bowl Veggie": 8.62
    },
    # drinks
        #item:price
    "drinks" : {
        "Pepsi": 2.39,
        "Diet Pepsi": 2.39,
        "Pepsi Zero Sugar": 2.39,
        "Cherry Pepsi": 2.39,
        "Mountain Dew": 2.39,
        "Mountain Dew Zero": 2.39,
        "Mountain Dew Baja Blast": 2.39,
        "Mountain Dew Baja Blast Zero Sugar": 2.39,
        "Mug Root Beer": 2.39,
        "Starry": 2.39,
        "G2 Gatorade Fruit Punch": 2.39,
        "Dole Lemonade Strawberry Squeeze": 2.39,
        "Brisk Mango Fiesta": 2.39,
        "Brisk Dragon Paradise Sparkling Iced Tea": 2.39,
        "Lipton Unsweetened Iced Tea": 2.39,
        "Tropicana Orange Juice": 2.29,
        "Limonada Freeze": 3.49,
        "Wild Strawberry Freeze": 3.49,
        "Strawberry Limonada Freeze": 3.49,
        "Vanilla Cream Limonada Freeze": 3.49,
        "Iced Coffee (Regular)": 1.99,
        "Premium Hot Coffee": 1.99,
        "White Monster" : 1.99
    },
    # sides
        #item:price
    "sides" : {
        "Large Nacho Fries": 3.19,
        "Nacho Fries": 2.29,
        "Cheesy Fiesta Potatoes": 2.59,
        "Chips and Guacamole": 3.39,
        "Black Beans": 2.39,
        "Black Beans and Rice": 2.69,
        "Pintos N Cheese": 2.59,
    },
    # desserts
        #item:price
    "dessert" : {
        "Cinnamon Twists": 1.29,
        "Cinnabon Delights 2 Pack": 2.39,
        "Cinnabon Delights 12 Pack": 7.19,
        "Milk Bar Birthday Cake Churros (2 Pack)": 2.99
    }
}

#ask user what main they want
print("What whould you like for your main?")
for item, price in menu["mains"]:
    print(f"{item}: ${price}")
    #Loop through the mains, listing them all for user
#let them pick one, add to list of user order

#ask user what drink they want
    #Loop through the drinks, listing them all for user
#let them pick one, add to list of user order

#ask user what sides they want(2)
    #Loop through the sides, listing them all for user
#let them pick one, add to list of user order

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
    #add round up for the kids
    #add different menus for different times of day