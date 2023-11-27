#Name: Kevin Paute
#Date: October 2, 2023

import turtle
toast = turtle.Turtle()

for i in range(5):
    A = int(input("Enter a number:"))
    toast.left(A)
    toast.forward(100)

turtle.exitonclick() 