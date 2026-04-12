#PS 1st turtle race

import random
import turtle as Bob

Finish = False
winner = ""
screen = Bob.Screen()
screen.setup(1000,1000)
screen.title("The Amazing Turtle Race!")

writingturtle = Bob.Turtle()
turtle1 = Bob.Turtle()
turtle2 = Bob.Turtle()
turtle3 = Bob.Turtle()
turtle4 = Bob.Turtle()
turtle5 = Bob.Turtle()

writingturtle.color("black")
turtle1.shape("turtle")
turtle1.color("blue")
turtle2.shape("turtle")
turtle2.color("red")
turtle3.shape("turtle")
turtle3.color("green")
turtle4.shape("turtle")
turtle4.color("yellow")
turtle5.shape("turtle")
turtle5.color("magenta")

writingturtle.penup()
turtle1.penup()
turtle2.penup()
turtle3.penup()
turtle4.penup()
turtle5.penup()

#setup
writingturtle.goto(-450,450)
writingturtle.pendown()
writingturtle.forward(800)
writingturtle.right(90)
writingturtle.forward(500)
writingturtle.right(90)
writingturtle.forward(800)
writingturtle.penup()
writingturtle.goto(-450,50)
writingturtle.pendown()
writingturtle.right(180)
writingturtle.forward(800)
writingturtle.penup()
writingturtle.goto(-450,150)
writingturtle.pendown()
writingturtle.forward(800)
writingturtle.penup()
writingturtle.goto(-450,250)
writingturtle.pendown()
writingturtle.forward(800)
writingturtle.penup()
writingturtle.goto(-450,350)
writingturtle.pendown()
writingturtle.forward(800)

writingturtle.penup()
writingturtle.goto(300,450)
writingturtle.right(90)
writingturtle.pendown()
writingturtle.forward(500)
writingturtle.penup()
writingturtle.goto(1000,1000)
#position
turtle1.goto(-400,400)
turtle2.goto(-400,300)
turtle3.goto(-400,200)
turtle4.goto(-400,100)
turtle5.goto(-400,0)

#put pendown for racing turtles
turtle1.pendown()
turtle2.pendown()
turtle3.pendown()
turtle4.pendown()
turtle5.pendown()


#race

while Finish == False:
    turtle1.forward(random.randint(1,25))
    if turtle1.xcor() >= 300.0:
        Finish == True
        winner = "Turtle 1"
        print(F"{winner} wins!")
        Bob.done()
        Bob.exitonclick()
    turtle2.forward(random.randint(1,25))
    if turtle2.xcor() >= 300.0:
        Finish == True
        winner = "Turtle 2"
        print(F"{winner} wins!")
        Bob.done()
        Bob.exitonclick()
    turtle3.forward(random.randint(1,25))
    if turtle3.xcor() >= 300.0:
        Finish == True
        winner = "Turtle 3"
        print(F"{winner} wins!")
        Bob.done()
        Bob.exitonclick()
    turtle4.forward(random.randint(1,25))
    if turtle4.xcor() >= 300.0:
        Finish == True
        winner = "Turtle 4"
        print(F"{winner} wins!")
        Bob.done()
        Bob.exitonclick()
    turtle5.forward(random.randint(1,25))
    if turtle5.xcor() >= 300.0:
        Finish == True
        winner = "Turtle 5"
        print(F"{winner} wins!")
        Bob.done()
        Bob.exitonclick()
Bob.done()
