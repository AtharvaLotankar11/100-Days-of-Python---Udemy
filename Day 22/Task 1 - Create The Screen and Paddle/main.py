#TODO 1: To Create the Screen
#TODO 2: To create a paddle
#TODO 3: To Create another Paddle

from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong - The Arcade Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

screen.listen()

#for right paddle use up and down arrows
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

#for left paddle to move vertically - use w and s
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    screen.update()


screen.exitonclick()