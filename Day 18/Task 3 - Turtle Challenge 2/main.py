#Draw a Dashed Line
from turtle import Turtle, Screen

my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("black", "lime")

def dashed():
    my_turtle.forward(10)
    my_turtle.penup()
    my_turtle.forward(10)
    my_turtle.pendown()

for i in range(0, 10):
    dashed()

my_screen = Screen()
my_screen.exitonclick()
