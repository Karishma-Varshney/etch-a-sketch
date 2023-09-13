from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

# game starts from here
def forwards():
    tim.forward(50)

def backwards():
    tim.backward(50)

def counter_clockwise():
    tim.right(10)

def clockwise():
    tim.left(10)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(key="w", fun=forwards)
screen.onkey(key="s", fun=backwards)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()