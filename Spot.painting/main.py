# import colorgram

# rgb_colors = []
# colors = colorgram.extract("image.jpg", 25)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_colour = (r, g, b)
#     rgb_colors.append(new_colour)

# print(rgb_colors)

import turtle as turtle_module 
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()

color_list = [
    (255,0,0), (255,22,12), (255,83,73), (124,13,14),
    (255,99,71), (255,127,80), (205,92,192), (240,28,128),
    (233,150,122),(250,128,114),(255,134,116),(255,160,122),
    (255,69,0),(252,210,153),(255,140,0),(218,165,32),
    (255,223,0),(153,101,21),(238,232,170),(19,183,107),
    (240,230,140),(128,18,0)
]

tim.setheading(225)
tim.forward(250)
tim.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
