#Nikolei Advani, 9/8/16
#This program draws four, equally spaced octagons, and fills each with a different color (red, blue, violet, yellow)
import turtle

#this function draws octagons
def octagonor():
    for x in range(8):
        turtle.forward(75)
        turtle.left(45)

#this function changes position
def move(x,y):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

#OCTAGON RED
turtle.begin_fill()
turtle.color("red")
octagonor()
turtle.end_fill()
move(200,0)

#OCTAGON BLUE
turtle.begin_fill()
turtle.color("blue")
octagonor()
turtle.end_fill()
move(200,-200)

#OCTAGON VIOLET
turtle.begin_fill()
turtle.color("violet")
octagonor()
turtle.end_fill()
move(0,-200)

#OCTAGON YELLOW
turtle.begin_fill()
turtle.color("yellow")
octagonor()
turtle.end_fill()

turtle.exitonclick()

