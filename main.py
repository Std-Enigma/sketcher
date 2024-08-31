
from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()
turtle.color("white")
screen.bgcolor("black")

def go_forward():
    turtle.forward(10)

def go_backward():
    turtle.back(10)

def turn_right():
    turtle.right(5)

def turn_left():
    turtle.left(5)

def reset():
    turtle.clear()
    turtle.penup()
    turtle.home()
    turtle.pendown()

screen.listen()
screen.onkeypress(go_forward, "w")
screen.onkeypress(go_backward, "s")
screen.onkeypress(turn_left, "a")
screen.onkeypress(turn_right, "d")
screen.onkeypress(reset, "c")
screen.exitonclick()
