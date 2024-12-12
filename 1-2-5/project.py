import turtle as trtl
import random as rand

#variable creation and named them all
painter = trtl.Turtle()
wn = trtl.Screen()
wn.title("Pong Game")
wn.setup(width = 1000, height = 600)
painter.screen.bgcolor('black')
painter.speed('fastest')

#This is for the creation of the middle lines of the ping game which show which side its on
def middle_lines():
    painter.color('white')
    painter.hideturtle()
    painter.penup()
    painter.setpos(0,300 )
    painter.setheading(270)
    painter.pensize(5)

for _ in range (30):
        painter.pendown()
        painter.forward(10)
        painter.penup()
        painter.forward(10)









wn.listen()
wn.mainloop()