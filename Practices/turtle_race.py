#DJ, 1st, Turtle Race
import turtle
import random
import time
def screen_setup():
    global t1_name
    global t2_name
    global t3_name
    global t4_name
    global t5_name
    global t1
    global t2
    global t3
    global t4
    global t5
    screen = turtle.Screen()
    screen.setup(600,400)
    screen.title("Turtle Race")
    screen.bgcolor("gray")
    t1 = turtle.Turtle()
    t1.hideturtle()
    t2 = turtle.Turtle()
    t2.hideturtle()
    t3 = turtle.Turtle()
    t3.hideturtle()
    t4 = turtle.Turtle()
    t4.hideturtle()
    t5 = turtle.Turtle()
    t5.hideturtle()
    t1.color("RoyalBlue4")
    t1.shape("turtle")
    t1.teleport(-250,150)
    t2.color("orchid")
    t2.shape("turtle")
    t2.teleport(-250,75)
    t3.color("PaleTurquoise1")
    t3.shape("turtle")
    t3.teleport(-250,0)
    t4.color("PaleGreen")
    t4.shape("turtle")
    t4.teleport(-250,-75)
    t5.color("purple")
    t5.shape("turtle")
    t5.teleport(-250,-150)
    t1_name = turtle.textinput("Turtle One Name", "Lets name the turtles! What would you like to name the first Turtle?").title().strip()
    t2_name = turtle.textinput("Turtle Two Name", "What would you like to name the second Turtle?").title().strip()
    t3_name = turtle.textinput("Turtle Three Name", "What would you like to name the third Turtle?").title().strip()
    t4_name = turtle.textinput("Turtle Four Name", "What would you like to name the fourth Turtle?").title().strip()
    t5_name = turtle.textinput("Turtle Five Name", "What would you like to name the fifth Turtle?").title().strip()


while True:
    wager = turtle.textinput("Turtle Gamble", f"Lets wager! Which turtle do you want to bet on?\n1.) {t1_name}\n2.) {t2_name}\n3.) {t3_name}\n4.) {t4_name}\n5.) {t5_name}").title().strip()
    if wager == t1_name:
        break
    elif wager == t2_name:
        break
    elif wager == t3_name:
        break
    elif wager == t4_name:
        break
    elif wager == t5_name:
        break
    else:
        continue
tokens = 10
while True:
    gamble = turtle.textinput("Gamble Amount", f"How many tokens would you like to gamble?\nYou have {tokens} tokens.")
    if gamble <= tokens:
        break
    else:
        continue
winner = False
while winner == False:
    t1_pos = 0
    t1_move = random.randint(5,10)
    t1.forward(t1_move)
    t1_pos += t1_move
    if t1_pos == 550:
        winner = True
    else:
        pass
    t2_pos = 0
    t2_move = random.randint(5,10)
    t2.forward(t2_move)
    t2_pos += t2_move
    if t2_pos == 550:
        winner = True
    else:
        pass
    t3_pos = 0
    t3_move = random.randint(5,10)
    t3.forward(t3_move)
    t3_pos += t3_move
    if t3_pos == 550:
        winner = True
    else:
        pass
    t4_pos = 0
    t4_move = random.randint(5,10)
    t4.forward(t4_move)
    t4_pos += t4_move
    if t4_pos == 550:
        winner = True
    else:
        pass
    t5_pos = 0
    t5_move = random.randint(5,10)
    t5.forward(t5_move)
    t5_pos += t5_move
    if t5_pos == 550:
        winner = True
    else:
        pass