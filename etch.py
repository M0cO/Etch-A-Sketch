from turtle import Turtle, Screen

shelly = Turtle()
screen = Screen()

def forward():
    shelly.forward(20)

def backward():
    shelly.backward(20)

def up():
    shelly.left(10)

def down():
    shelly.right(10)

def curve_right():
    shelly.right(10)
    shelly.forward(10)

def curve_left():
    shelly.left(10)
    shelly.forward(10)

def clear():
    shelly.reset()

def movement():
    screen.listen()
    screen.onkey(key="w", fun=forward)
    screen.onkey(key="s", fun=backward)
    screen.onkey(key="a", fun=up)
    screen.onkey(key="d", fun=down)
    screen.onkey(key="c", fun=clear)
    screen.onkey(key="e", fun=curve_right)
    screen.onkey(key="q", fun=curve_left)

movement()
screen.exitonclick()
