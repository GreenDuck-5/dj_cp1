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
availible_locations = ("Saloon", "Inn", "Casino")

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
    print("Old Man: ‘Howdy, Phoenix! Welcome to Ember Bend! It’s a neat little town. At least it was. But that was before the new sheriff came into town, 15 years he’s made this place a living hell. But I’m sure you knew that. That’s why you’re here, Mr. Brooks, no?’")
    t.sleep(1.5)
    while True:
        choice_one = input("1.) Yes. For honor.\n2.) No. For money.\n3.) Yes. For you.\n")
        if choice_one == "1":
            print("Phoenix: ‘Of course, only a man with no honor would abandon his home town when it is in need’")
            t.sleep(1)
            phoenix_brooks["Honor"] += 5
            print("The old man will remember that.")
            t.sleep(1)
            print("Old Man: ‘Atta boy. I raised you right, that’s evident to me’")
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
            phoenix_brooks["Morale"] += 5
            print("The old man will remember that.")
            t.sleep(1)
            break
        else:
            print("Please enter valid input.")
            continue
    return

def saloon():
    pass

def inn():
    pass

def casino():
    pass

def mine():
    pass

def station():
    pass

def bank():
    pass

def store():
    pass

def jail():
    pass

def shooting_range():
    pass

def user_turn():
    pass

def sheriff_turn():
    pass

def bandits_turn():
    pass

def sheriff_fight():
    pass

def bandit_fight():
    pass

def location_move():
    print("Which would you like you like to go to?")
    num = 1
    for place in availible_locations:
        print(f"{num}.) {place}")
        num += 1
    new_loc = input().strip()