import turtle
import random

elsa = turtle.Turtle()
# List of colors for the pattern
colors = ["cyan", "purple", "white", "blue"]
# Set the background color of the turtle screen to grey
turtle.Screen().bgcolor("grey")
elsa.color("cyan")

# Loop to draw the pattern
for i in range(10):
    # Loop to draw each shape in the pattern
    for i in range(2):
        elsa.forward(100)
        elsa.right(60)
        elsa.forward(100)
        elsa.right(120)
    elsa.right(36)
    elsa.color(random.choice(colors))