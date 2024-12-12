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
    for middle_lines in range (30):
        painter.pendown()
        painter.forward(10)
        painter.penup()
        painter.forward(10)
middle_lines()

#This is for the first paddle that's used in the game just to create it
paddle_a = trtl.Turtle()
paddle_a.speed('fastest')
paddle_a.color('white')
paddle_a.shapesize(stretch_wid = 6, stretch_len = 1)
paddle_a.penup()
paddle_a.goto(-450,0)

#This is for the second paddle that's used in the game just to create it
paddle_b = trtl.Turtle()
paddle_b.speed('fastest')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid = 6, stretch_len = 1)
paddle_b.penup()
paddle_b.goto(450,0)




wn.listen()
wn.mainloop()