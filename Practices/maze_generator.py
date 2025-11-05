#DJ, 1st, Maze Generator
#import libraries to use
import turtle
import random
#set the turtle speed and making it's shape a turtle because turtles are awesome
turtle.speed(0)
turtle.shape("turtle")
#setting size of cells and grid size, being rows by cols
cell = 30
rows = 25
cols = 25
#building the edge
#teleporting to the point to start
turtle.teleport(-cols*cell/2,rows*cell/2)
#drawing a line as long as necessary, based off what the row length and cell size it
turtle.forward(cell*rows)
turtle.right(90)
#giving an enterence/exit
turtle.forward((cell*cols)-cell)
turtle.penup()
turtle.forward(cell)
turtle.pendown()
turtle.right(90)
#same as before
turtle.forward(cell*rows)
turtle.right(90)
turtle.forward((cell*cols)-cell)
#setting wall drawing function
def draw_wall(x, y, direction):
    turtle.penup()
    #going to cordanates based of the math below in the for loop
    turtle.goto(x, y)
    #setting angle of turtle movement
    turtle.setheading(direction)
    turtle.pendown()
    #drawing the wall, moving forward however far "cell" is
    turtle.forward(cell)
    turtle.penup()
#making the collum generate for every row
for i in range(rows):
    #generating collum row
    for j in range(cols):
        #measuring center of cell then center of screen, centering everything
        x = j*cell-cols*cell/2
        y = i*cell-rows*cell / 2
        #randomly picking whether to run the wall building(1 in 3)
        if random.choice([True, False, False]):
            #building a vertrical wall(90)
            draw_wall(x+cell,y,90)
        if random.choice([True, False, False]):
            #building a horizontal wall(0)
            draw_wall(x,y+cell,0)
#doesn't end the program till user picks to
turtle.done()