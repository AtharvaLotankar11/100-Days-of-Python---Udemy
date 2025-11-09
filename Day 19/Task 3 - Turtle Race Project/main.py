#Turtle Race Project
import random
from turtle import Turtle, Screen

is_race_on = False

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []  # This should be initialized outside the loop

for turtle_index in range(6):  # You can omit the 0
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])  # Set the starting position of each turtle
    all_turtles.append(new_turtle)  # Add the new turtle to the list

if user_bet:
    is_race_on = True

while is_race_on:
    for trtle in all_turtles:  # Now this loop will iterate over all the turtles
        if trtle.xcor() > 230:  # Check if any turtle reaches the finish line
            is_race_on = False
            winning_color = trtle.pencolor()
            if winning_color == user_bet:
                print(f"You have won! The {winning_color} turtle is the winner!")
            else:
                print(f"You have lost! The {winning_color} turtle is the winner!")

        rand_dist = random.randint(0, 10)  # Move the turtle by a random distance
        trtle.forward(rand_dist)

screen.exitonclick()
