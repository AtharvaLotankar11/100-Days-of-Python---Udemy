#Draw different shapes: Triangle, Square, Pentagon...,Decagon
from turtle import Turtle, Screen

my_turtle = Turtle()
my_turtle.shape("turtle")

angle = 360

def triangle():
    for i in range(3):
        my_turtle.forward(100)
        my_turtle.right(angle // 3)
        my_turtle.color("black", "lime")

def square():
    for i in range(4):
        my_turtle.forward(100)
        my_turtle.right(angle // 4)
        my_turtle.color("blue", "lime")

def pentagon():
    for i in range(5):
        my_turtle.forward(100)
        my_turtle.right(angle // 5)
        my_turtle.color("red", "lime")

def hexagon():
    for i in range(6):
        my_turtle.forward(100)
        my_turtle.right(angle // 6)
        my_turtle.color("lime", "lime")

def heptagon():
    for i in range(7):
        my_turtle.forward(100)
        my_turtle.right(angle // 7)
        my_turtle.color("brown", "lime")

def octagon():
    for i in range(8):
        my_turtle.forward(100)
        my_turtle.right(angle // 8)
        my_turtle.color("coral", "lime")

def nonagon():
    for i in range(9):
        my_turtle.forward(100)
        my_turtle.right(angle // 9)
        my_turtle.color("cyan", "lime")

def decagon():
    for i in range(10):
        my_turtle.forward(100)
        my_turtle.right(angle // 10)
        my_turtle.color("pink", "lime")

triangle()
square()
pentagon()
hexagon()
heptagon()
octagon()
nonagon()
decagon()

my_screen = Screen()
my_screen.exitonclick()
