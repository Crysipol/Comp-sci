#Name: Kevin Paute
#Email: Kevin.paute88@myhunter.cuny.edu
#Date: September 18,2023
#This program stamps turtles while creating an pentagon 

import turtle
cat = turtle.Turtle()
cat.shape("turtle")
cat.color("#6495ED")

for i in range(5):
    cat.forward(100)
    cat.left(360/5)
    cat.stamp()
    
