# from turtle import Turtle, Screen
# import random


# timmy_the_turtle = Turtle()
# timmy_the_turtle.shape("turtle")
# timmy_the_turtle.color("orange") 

# for _ in range(40):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.color("white")
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.color("black")


# for _ in range(15):
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.penup()
#     timmy_the_turtle.forward(10)
#     timmy_the_turtle.pendown()

# for _ in range(4):
#     timmy_the_turtle.forward(100)
#     timmy_the_turtle.right(90)
#     for _ in range(5):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(72)
    
# colours = ["red",  "blue", "green", "yellow", "pink" , "black"]

# def draw_shape(num_slides):
#     angle = 360 / num_slides
#     for _ in range(num_slides):
#         timmy_the_turtle.forward(100)
#         timmy_the_turtle.right(angle)

# for shape_slide_n in range(3 , 11):
#     timmy_the_turtle.color(random.choice(colours))
#     draw_shape(shape_slide_n)






# import turtle as t
# import random


# tim = t.Turtle()
# t.colormode(255)

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color

# # colours = ["red",  "blue", "green", "yellow", "pink" , "black"]
# directions = [0, 90, 180, 270]
# tim.pensize(15)
# tim.speed("fastest")

# for _ in range(200):
#     tim.color(random_color())
#     tim.forward(30)
#     tim.setheading(random.choice(directions))



# import turtle as t
# import random

# tim = t.Turtle()
# t.colormode(255)

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color

# tim.speed("fastest")


# def draw_graph(size_of_gap):
#     for _ in range(int(360 / size_of_gap)):
#         tim.color(random_color())
#         tim.circle(100)
#         tim.setheading(tim.heading() + 10)

# draw_graph(5)

# screen = t.Screen()
# screen.exitonclick()

