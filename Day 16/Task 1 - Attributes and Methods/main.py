#import turtle
#timmy = turtle.Turtle() //to access turtle module with className Turtle
import turtle

from turtle import Turtle, Screen
# object = className() - OOP Formula
timmy = Turtle()
print(timmy)

#change shape of timmy as cursor to timmy as actual turtle
timmy.shape("turtle")

#Pause 1 - To change color of Turtle
timmy.color("Coral", "chartreuse")

#Pause 2 - Move the turtle forward by 100 spaces
timmy.forward(100)

#let us represent Screen() className - for window of Turtle
my_screen = Screen()

#object.attributeName
print(f"Screen Dimensions by Screen() is: {my_screen.canvheight} x {my_screen.canvwidth}")

my_screen.exitonclick() #will continue to run until we click to exit


