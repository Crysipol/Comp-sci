#Name:Kevin Paute
#Email:Kevin.paute88@myhunter.cuny.edu

import turtle
import random

istab = turtle.Turtle()
istab.speed(10)

for _ in range(100):
    istab.forward(10)
    w = random.randrange(0, 360)
    istab.right(w)
