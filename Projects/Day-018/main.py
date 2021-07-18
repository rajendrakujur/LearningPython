
import turtle as t
import random

t.colormode(255)
color_list = [(248, 248, 245), (240, 249, 245), (249, 238, 245), (235, 242, 249), (237, 224, 80),
              (205, 4, 73), (236, 50, 130), (198, 164, 8), (111, 179, 218), (204, 75, 12), (219, 161, 103),
              (234, 224, 4), (11, 23, 63), (29, 189, 111), (22, 107, 174), (16, 28, 177), (216, 134, 179),
              (8, 186, 216), (229, 167, 200), (210, 25, 148), (122, 190, 160), (7, 49, 26), (34, 136, 72),
              (63, 20, 7), (126, 219, 234), (190, 14, 4), (109, 87, 215), (140, 217, 202), (238, 64, 34),
              (71, 10, 28), (10, 98, 50), (166, 181, 232), (237, 170, 159), (253, 5, 42), (9, 87, 103),
              (21, 35, 249), (63, 100, 8), (253, 9, 5), (0, 246, 244), (0, 250, 254)]

new_turtle = t.Turtle()
new_turtle.speed('fastest')
new_turtle.hideturtle()
new_turtle.penup()
new_turtle.setheading(225)
new_turtle.fd(275)
new_turtle.setheading(0)
for number_of_dots in range(1, 226):
    new_turtle.dot(20, random.choice(color_list))
    new_turtle.forward(30)
    if number_of_dots % 15 == 0:
        new_turtle.setheading(90)
        new_turtle.forward(30)
        new_turtle.setheading(180)
        new_turtle.forward(450)
        new_turtle.setheading(0)

screen = t.Screen()
screen.exitonclick()

