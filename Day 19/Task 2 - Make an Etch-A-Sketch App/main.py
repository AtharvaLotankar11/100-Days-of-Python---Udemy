#Develop a Make-an-Etch-A-Sketch-App
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def forward():
    tim.forward(30)

def backward():
    tim.backward(30)

def counter_clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear() #to clear the drawing
    tim.penup()
    tim.home() #to return to origin
    tim.pendown()


screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()