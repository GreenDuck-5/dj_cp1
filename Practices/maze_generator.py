#DJ, 1st, Maze Generator
#import libraries to use
import turtle
import random
turtle.speed(0)
turtle.hideturtle()
cell = 30
rows = 25
cols = 25
turtle.teleport(-375,375)
turtle.forward(cell*cols)
turtle.right(90)
turtle.forward((cell*rows)-cell)
turtle.penup()
turtle.forward(cell)
turtle.pendown()
turtle.right(90)
turtle.forward(cell*cols)
turtle.right(90)
turtle.forward((cell*rows)-cell)
def draw_wall(x, y, direction):
    turtle.penup()
    turtle.goto(x, y)
    turtle.setheading(direction)
    turtle.pendown()
    turtle.forward(cell)
    turtle.penup()
for i in range(rows):
    for j in range(cols):
        x = j * cell - cols * cell / 2
        y = i * cell - rows * cell / 2
        if random.choice([True, False, False]):
            draw_wall(x + cell, y, 90)
        if random.choice([True, False, False]):
            draw_wall(x, y + cell, 0)
turtle.done()