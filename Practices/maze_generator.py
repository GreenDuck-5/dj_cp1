#DJ, 1st, Maze Generator
#import libraries to use
import turtle
import random
#set the turtle speed and making it's shape a turtle because turtles are awesome
turtle.speed(0)
turtle.shape("turtle")
#setting size of cells and grid size, being rows by cols
cell = 20
rows = 25
cols = 25
#setting variables that subtract how many rows actually generate
rows_less = 2
cols_less = 0
#building the edge
#teleporting to the point to start
turtle.teleport(-cols*cell/2,rows*cell/2)
#drawng a line as long as necssary, based off what the row lngth and cell size it
turtle.forward(cell*rows)
turtle.right(90)
#giving an enterence/exit
turtle.forward((cell*cols)-(cell*2))
turtle.penup()
turtle.forward(cell*2)
turtle.pendown()
turtle.right(90)
#same as befor
turtle.forward(cell*rows)
turtle.right(90)
turtle.forward((cell*cols)-(cell*2))
#setting wall drawing function
def draw_wall(x, y, direction):
    turtle.penup()
    #going to cordanates based of the math below in the for loop
    turtle.goto(x, y)
    turtle.setheading(direction)
    turtle.pendown()
    #drawing the wall, moving forward however far "cell" is
    turtle.forward(cell)
    turtle.penup()
#making the collum generate for every row
for duck in range(rows-rows_less):
    #generating collum row
    for goose in range(cols-cols_less):
        #measring center of cell then center of screen, cetering evrything
        x = goose*cell-cols*cell/2
        y = duck*cell-rows*cell/2
        #randomly picking wether to run the wall building(1 in 3)
        if random.choice([True, False, False, True, False, True, False, False, True, False, False]):
            #building a vertrical wall(90)
            draw_wall(x+cell,y,90)
        if random.choice([True, False, False, True, False, True, False, False, True, False, False]):
            #building a hoizontal wall(0)
            draw_wall(x,y+cell,0)
turtle.hideturtle()
#doesnt end the program till user picks to
turtle.done()