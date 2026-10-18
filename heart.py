import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("A Little Heart")
 
t = turtle.Turtle()
t.speed(1)
t.hideturtle()
t.color("#ffb6cd")


for scale in range(11, 17):
    t.penup()

    for i in range(121):
        angle = i * (math.pi * 2) / 120

        x = 16 * (math.sin(angle) ** 3) * scale
        y = (13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)) * scale

        t.goto(x, y)

        if i == 0:
            t.pendown()

    t.penup()

t.goto(0, -15)
t.write("I love you", align="center", font=("Arial", 12, "bold"))

turtle.done()

