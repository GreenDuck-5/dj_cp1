# DJ, 1st, Text Based Adventure
import time as t
import random as r

phoenix_brooks = {
	"Health": 25,
	"Morale": 10,
	"Honor": 15,
	"Money": 100,
}
availible_weapons = ("Fist", "Pistol", "Boot")

saloon_visited = False
inn_visited = False
casino_visited = False
mine_visited = False
station_visited = False
bank_visited = False
store_visited = False
jail_visited = False
shooting_range_visited = False
saloon_fight = False
jail_break = False

fist = {
    "Damage": 5,
    "Range": 1,
    "Accuracy": {
        "Upper Body": {
            "Head": 60,
            "Right Shoulder": 80,
            "Left Shoulder": 80,
            "Throat": 50,
            "Chest": 95,
            "Stomach": 90
        },
        "Lower Body": {
            "Right Thigh": 40,
            "Left Thigh": 40,
            "Right Shin": 20,
            "Left Shin": 20,
            "Left Foot": 5,
            "Right Foot": 5
        }
    }
}

pistol = {
    "Damage": 20,
    "Range": 45,
    "Accuracy": {
        "Upper Body": {
            "Head": 70,
            "Right Shoulder": 80,
            "Left Shoulder": 80,
            "Throat": 45,
            "Chest": 95,
            "Stomach": 80
        },
        "Lower Body": {
            "Right Thigh": 20,
            "Left Thigh": 20,
            "Right Shin": 10,
            "Left Shin": 10,
            "Left Foot": 30,
            "Right Foot": 30
        }
    }
}

rifle = {
    "Damage": 20,
    "Range": 1375,
    "Accuracy": {
        "Upper Body": {
            "Head": 70,
            "Right Shoulder": 80,
            "Left Shoulder": 80,
            "Throat": 45,
            "Chest": 95,
            "Stomach": 80
        },
        "Lower Body": {
            "Right Thigh": 20,
            "Left Thigh": 20,
            "Right Shin": 10,
            "Left Shin": 10,
            "Left Foot": 30,
            "Right Foot": 30
        }
    }
}

shotgun = {
    "Damage": 30,
    "Range": 90,
    "Accuracy": {
        "Upper Body": {
            "Head": 95,
            "Right Shoulder": 90,
            "Left Shoulder": 90,
            "Throat": 90,
            "Chest": 95,
            "Stomach": 90
        },
        "Lower Body": {
            "Right Thigh": 50,
            "Left Thigh": 50,
            "Right Shin": 10,
            "Left Shin": 10,
            "Left Foot": 30,
            "Right Foot": 30
        }
    }
}

boot = {
    "Damage": 10,
    "Range": 1.5,
    "Accuracy": {
        "Upper Body": {
            "Head": 10,
            "Right Shoulder": 15,
            "Left Shoulder": 15,
            "Throat": 10,
            "Chest": 15,
            "Stomach": 50
        },
        "Lower Body": {
            "Right Thigh": 70,
            "Left Thigh": 70,
            "Right Shin": 90,
            "Left Shin": 90,
            "Left Foot": 95,
            "Right Foot": 95
        }
    }
}

def introduction(phoenix_brooks):
    print("Old Man: ‘Howdy, Phoenix! Welcome to Ember Bend! It’s a neat little town, at least it was. But that was before the new sheriff came into town, 15 years he’s made this place a living hell. But I’m sure you knew that. That’s why you’re here, Mr. Brooks, no?’")
    t.sleep(1.5)
    while True:
        choice_one = input("1.) Yes. For honor.\n2.) No. For money.\n3.) Yes. For you.\n")
        if choice_one == "1":
            print("Phoenix: ‘Of course, only a man with no honor would abandon his home town when it is in need.’")
            t.sleep(1)
            phoenix_brooks["Honor"] += 5
            print("The old man will remember that.")
            t.sleep(1)
            print("Old Man: ‘Atta boy. I raised you right, that’s evident to me.’")
            t.sleep(1)
            break
        elif choice_one == "2":
            print("Phoenix: ‘I am not here for you old man. I am here to make money, and if I stop the sheriff while I'm at it, that’s fine. But it is not my goal.")
            t.sleep(1)
            phoenix_brooks["Honor"] -= 5
            print("The old man will remember that.")
            t.sleep(1)
            break
        elif choice_one == "3":
            print("Phoenix: ‘Yes. I am here for you, my friend. It has been too long. How you been?’")
            t.sleep(1)
            print("Old Man: ‘Thank you.’")
            phoenix_brooks["Morale"] += 5
            print("The old man will remember that.")
            t.sleep(1)
            break
        else:
            print("Please enter valid input.")
            continue
    return

def saloon():
    print("You walk up to the saloon, the massive sign at the front reads: ‘The High Noon Saloon’\nYou have seen this building many times, but never in it.\nYou never liked the yelling and crashing.")
    t.sleep(2)
    print("Opening the saloon doors, you can now see what it’s like.\nIt’s loud, but it’s just people having a good time.")
    t.sleep(2)
    print("You walk up to the bartender, asking for a drink.")
    t.sleep(1)
    print("Bartender: ‘5 coins’")
    t.sleep(1)
    while True:
        choice_two = input(f"1.) Pay: You have {phoenix_brooks["Money"]} coins\n2.) Punch him\n3.) Haggle\n")
        if choice_two == "1":
            phoenix_brooks["Money"] -= 5
            print("You pay for the drink. It's some good orange juice. You are now fully healed.")
            print("You walk out, feeling satisfied.")
            phoenix_brooks["Health"] = 25
            saloon_visited = True
            return
        elif choice_two == "2":
            print("Where would you like to hit:")
            return
        elif choice_two == "3":
            print("Phoenix: ‘I can do 3’\nBartender: ‘4’")
            while True:
                choice_three = input("1.) Take the deal\n2.) Leave\n3.) Punch him\n")
                if choice_three == "1":
                    print("Phoenix: ‘Aight, that works.’")
                    phoenix_brooks["Health"] = 25
                    phoenix_brooks["Money"] -= 4
                    saloon_visited = True
                    return
                elif choice_three == "2":
                    print("Phoenix: ‘Nah, I'll pass.’")
                    print("You leave.")
                    saloon_visited = True
                    return
                elif choice_three == "3":
                    print("fight")
                    return
                else:
                    print("Please enter valid input")
                continue
        else:
            print("Please enter valid input")
            continue
def inn():
    print("inn")

def casino():
    print("casino")

def mine():
    print("mine")

def station():
    print("station")

def bank():
    print("bank")

def store():
    print("store")

def jail():
    print("jail")

def shooting_range():
    print("shooting range")

def sheriff_fight():
    pass

def bandit_fight():
    pass

def location_move():
    print("Which would you like you like to go to?")
    print("1.) Saloon\n2.) Inn\n3.) Casino\n4.) Mine\n5.) Train Station\n6.) Bank\n7.) General Store\n8.) Jail\n9.) Shooting Range")
    while True:
        new_loc = input().strip()
        if new_loc == "1":
            saloon()
            break
        elif new_loc == "2":
            inn()
            break
        elif new_loc == "3":
            casino()
            break
        elif new_loc == "4":
            mine()
            break
        elif new_loc == "5":
            station()
            break
        elif new_loc == "6":
            bank()
            break
        elif new_loc == "7":
            store()
            break        
        elif new_loc == "8":
            jail()
            break
        elif new_loc == "9":
            shooting_range()
            break
        else:
            print("Please enter valid input.")
            continue

introduction(phoenix_brooks)
location_move()
print("jkgsadk")