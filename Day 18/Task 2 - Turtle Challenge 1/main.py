#Generate Draw a Square
#Alt: from turtle import * (* means all)
from turtle import Turtle, Screen

square_turtle = Turtle()
square_turtle.shape("turtle")
square_turtle.color("black", "lime")

def square():
    square_turtle.forward(100)
    square_turtle.right(90)

for i in range(0, 4):
    square()

my_screen = Screen()
my_screen.exitonclick()

import heroes
print(heroes.gen())