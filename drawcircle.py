"""
Define a function drawCircle. 
This function should expect a Turtle object, 
the coordinates of the circle’s center point, 
and the circle’s radius as arguments. 
The function should draw the specified circle. 
The algorithm should draw the circle’s circumference by turning 3 degrees and moving a given distance 120 times. 
Calculate the distance moved with the formula 2.0 * π * radius / 120.0.
"""
from turtle import Turtle
import math

def drawCircle(t, x, y, radius):
    distance = 2.0 * math.pi * radius / 120.0
    angle = 3
    t.up()
    t.goto(x, y)
    t.setheading(270)
    t.forward(radius)
    t.setheading(0)
    t.down()
    for count in range(120):
        t.forward(distance)
        t.left(angle)

def main():
    t = Turtle()
    x = int(input("Enter x coordinate of center point: "))    
    y = int(input("Enter y coordinate of center point: "))
    radius = int(input("Enter the radius: "))
    drawCircle(t, x, y, radius)
    distanceMoved = 2.0 * math.pi * radius
    print("Total distance moved: " + str(distanceMoved))

main()