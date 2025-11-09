#TODO 1: To setup the screen and creating a snake body
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=550, height=550)
screen.bgcolor("black")
screen.title("My Snake Game")

starting_positions = [(0,0), (-20, 0), (-40, 0)]

for position in starting_positions:
    new_segment = Turtle(shape="square")
    new_segment.color("white")
    new_segment.goto(position)














screen.exitonclick()
