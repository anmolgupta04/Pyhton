from turtle import Turtle, Screen

tim = Turtle()
Screen = Screen()

def move_forwards():
    tim.forward(20)


Screen.listen()
Screen.onkey(key="space", fun= move_forwards)
Screen.exitonclick()
