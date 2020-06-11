import turtle
import math
import random
import os

wn=turtle.Screen()
wn.bgcolor("black")

wn.tracer(3)

mypen=turtle.Turtle()
mypen.color('white')
mypen.penup()
mypen.setposition(-300,300)
mypen.pendown()
mypen.pensize(3)
for side in range(4):
    mypen.forward(600)
    mypen.right(90)
mypen.hideturtle()


player=turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)


score=0;

maxGoals=10
goals=[]

for count in range(maxGoals):
    goals.append(turtle.Turtle())
    goals[count].color("red")
    goals[count].shape("circle")
    goals[count].penup()
    goals[count].speed(0)
    goals[count].setposition(random.randint(-300, 300), random.randint(-300, 300))

speed=1

def turnleft():
    player.left(30)


def turnright():
    player.right(30)


def increasespeed():
    global speed
    speed += 1


def iscollision(t1, t2):
    d=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if d<20:
        return True
    else:
        return False





turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(increasespeed, "Up")


while True:
    player.forward(speed)

    if player.xcor() > 300 or player.xcor() < -300:
        player.right(180)
        #os.system("afplay bounce.mp36")

    
    if player.ycor() > 300 or player.ycor() < -300:
        player.right(180)
        #os.system("afplay bounce.mp36")

    
    for count in range(maxGoals):
        goals[count].forward(3)

        if goals[count].xcor() > 290 or goals[count].xcor() < -290:
            goals[count].right(180)
            #os.system("afplay bounce.mp36")
    
        
        if goals[count].ycor() > 290 or goals[count].ycor() < -290:
            goals[count].right(180)
            #os.system("afplay bounce.mp36")

        if iscollision(player, goals[count]):
            goals[count].setposition(random.randint(-300, 300), random.randint(-300, 300))
            goals[count].right(random.randint(0,360))
            #os.system("afplay collision.mp36")
            score += 1


            mypen.penup()
            mypen.hideturtle()
            mypen.setposition(-290, 310)
            scorestring="Score %s" %score
            mypen.write(scorestring,False,align="left",font=("arial",14,"normal"))

            

