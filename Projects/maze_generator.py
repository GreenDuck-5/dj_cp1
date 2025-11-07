#DJ, 1st, Maze Generator

# Just a note, this is impossible to generate it to be impossible, at least I believe so, in all my testing it has never generated an impossible maze

#import libraries(extra functions to use) to use
import turtle
import random

#set the turtle speed and making it's shape a turtle because turtles are awesome
turtle.shape("turtle")
screen = turtle.Screen()
screen.tracer(0)

#setting size of cells and grid size, being rows by cols
cell = 15
rows = 40
cols = 40

#building the edge

def build_outer_wall(cell,rows,cols):
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

def build_maze(cell,rows,cols):
    #making the collum generate for every row
    for i in range(rows-1):
        #generating collum row
        for j in range(cols-1):
            #measring center of cell then center of screen, cetering evrything
            x = j*cell-cols*cell/2
            y = i*cell-rows*cell/2
            #randomly picking wether to run the wall building(4 in 11)
            if random.choice([True, False, False, True, False, True, False, False, True, False, False]):
                #building a vertrical wall(90) on the right side of the cell
                draw_wall(x+cell,y,90)
            if random.choice([True, False, False, True, False, True, False, False, True, False, False]):
                #building a hoizontal wall(0) on the top of the cell
                draw_wall(x,y+cell,0)
    #blocking off the corner, just a failsafe for a too easy maze
    draw_wall(x+cell,y+cell,0)

#calling the functions to happen
build_outer_wall(cell,rows,cols)
build_maze(cell,rows,cols)

#hides the turtle
screen.tracer(1)
turtle.hideturtle()

#doesnt end the program till user picks to
turtle.done()