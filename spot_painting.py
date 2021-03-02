import colorgram
import turtle as t
import random

turtle = t.Turtle()
t.colormode(255)
screen = t.Screen()

# Extract 25 colors from an image.
colors = colorgram.extract('Ellipticine.png', 25)

# colorgram.extract returns Color objects, which let you access
# RGB, HSL, and what proportion of the image was that color.

# create empty color list
rgb_color_list = []

# append rgb colors to color list
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r , g , b)
    rgb_color_list.append(new_color)

# make the turtle invisible
turtle.hideturtle()

# speed up turtle's animation speed
turtle.speed('fastest')

#Turtle will move around the screen, but will not draw
turtle.penup()

# setup 800x800 screen
screen.setup(800,800)

# turtle's x position
pos_x =  - screen.window_width() / 2  + 75 

# turtle's y position
pos_y = - screen.window_height() / 2  + 75


for row in range(7):
    for column in range(7):
        # turtle is moved to given position
        turtle.goto(pos_x + column * 100, pos_y + row * 100)
        # draw a dot with diameter size 50
        turtle.dot(50 , random.choice(rgb_color_list))
        

# terminate program when mouse is clicked
screen.exitonclick()


