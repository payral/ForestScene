# drawings.py, Peter Ayral
import turtle
import math

def drawRectangle(t, width, height, tilt, penColor, fillColor):
    t.color(penColor, fillColor)
    t.seth(tilt)
    t.begin_fill()
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.forward(width)
    t.left(90)
    t.forward(height)
    t.left(90)
    t.end_fill()

def drawTriangle(t, sidelength, penColor, fillColor):
    t.color(penColor, fillColor)
    t.begin_fill()
    t.forward(sidelength)
    t.left(120)
    t.forward(sidelength)
    t.left(120)
    t.forward(sidelength)
    t.left(120)
    t.end_fill()

def drawTwoTriangles(t):
    drawTriangle(t, 30, "green", "yellow")
    t.up()
    t.forward(100)
    t.down()
    drawTriangle(t, 70, "purple", "blue")


def drawTwoRectangles(t):
    drawRectangle(t, 50, 100, 0, "red", "")
    t.up()
    t.forward(100)
    t.down()
    drawRectangle(t, 100, 150, 22, "green", "yellow")

if __name__=="__main__":
    chris=turtle.Turtle()
