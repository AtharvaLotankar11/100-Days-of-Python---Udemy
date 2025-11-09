#TODO 3: Creating a Snake Class & Move to OOP
from turtle import Turtle, Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=550, height=550)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) #animation turned off

snake = Snake()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

screen.exitonclick()
