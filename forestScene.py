# ForestScene.py, Peter Ayral
from basicShapes import drawRectangle
from basicShapes import drawTriangle
import turtle
import random

def drawTree(t,height,color):
    '''drawing trunk'''
    t.setheading(0)
    trunkwidth = .05*height
    trunkheight=(0.3*height)
    ogx=t.xcor()
    ogy=t.ycor()
    drawRectangle(t,trunkwidth,trunkheight,0,"#972A29","#972A29")
    t.up()
    t.left(90)
    t.forward(trunkheight)
    t.left(90)
    '''calculating distances'''
    branchlength=.4*height
    over=.5*(branchlength-trunkwidth)
    branchheight= (branchlength*(3**0.5))/2
    betweenbranches=((.7*height)-branchheight)/2
    '''drawing branches'''
    t.forward(over)
    t.left(180)
    t.down()
    for num in range(3):
        drawTriangle(t,branchlength,color, color)
        t.up()
        t.left(90)
        t.forward(betweenbranches)
        t.right(90)
    t.goto(ogx,ogy)
def checkTreeHeight(t):
    t.up()
    t.goto(0,-200)
    t.down()
    drawRectangle(t, 200, 200, 0 , "red","")
    t.seth(0)
    drawTree(t, 200, "green")
def drawForest(t):
    t.up()
    t.goto(-400, -100)
    numoftrees=random.randint(10,20)
    density=800/numoftrees
    for i in range(numoftrees):
        t.up()
        t.seth(0)
        t.setx(-400)
        t.forward((i*density) +random.randint(-35,35))
        t.right(90)
        t.sety(-100)
        t.forward(random.randint(-25,25))
        t.left(90)
        t.down()
        shadesOfGreen =["#006400", "#556b2f", "#8fbc8f", "#2e8b57", "#3cb371", "#20b2aa", "#32cd32"] 
        color= random.choice(shadesOfGreen)
        drawTree(t, random.randint(200,300), color)
def drawHut(t):
    '''drawing walls'''
    t.pensize(2)
    startx=t.xcor()
    starty=t.ycor()
    for i in range(10):
        drawRectangle(t, 12.5 , 75, 0, "black","#972A29")
        t.up()
        t.sety(starty)
        t.forward(random.randint(4,10))
        t.right(90)
        t.forward(random.randint(-1,1))
        t.left(90)
        t.down()
    endx=t.xcor()+12.5
    middle=(startx + endx)/2
    '''drawing roof'''
    t.up()
    t.goto(middle,starty+100)
    t.down()
    for i in range(15):
        t.seth(0)
        angle=100+(i*12)
        plywoodlen=random.randint(70,80)
        drawRectangle(t,7.5,plywoodlen,angle,"black","#972A29")

def drawVillage(t):
    t.up()
    t.goto(-300, -200)  
    for i in range(5):
        t.up()
        t.seth(0)
        t.setx(-300+(i*120))
        t.forward(random.randint(-25,25))
        t.right(90)
        t.sety(-200)
        t.forward(random.randint(-10,10))
        t.left(90)
        t.down()
        drawHut(t)
def drawScene(t):
    drawForest(t)
    drawVillage(t)

if __name__=="__main__":
    peter=turtle.Turtle()
    peter.speed(0)
    drawScene(peter)
